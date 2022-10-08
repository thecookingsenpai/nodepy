import os 
from subprocess import Popen, PIPE, STDOUT

class JSCommand:
    
    # ANCHOR Manages the creation of a new JSCommand object
    def __init__(self, is_file = False, command = [None, [], []], file="", real_time = False):
        self.real_time = real_time
        if is_file:
            if file.strip=="":
                raise Exception("File path is empty")
            self.file = file
            self.is_file = True
        else:
            if command[0]==None or command[0].strip()=="":
                raise Exception("Command is empty")
            self.command = command
            self.is_file = False
    
    # ANCHOR Run management
    def run(self):
        if self.is_file:
            self.execute_file()
        else:
            self.execute_cmd()
    
    # ANCHOR Single command execution
    def execute_cmd(self):
        # NOTE Command structure
        # [
        #   command_string,
        #   ["arguments", "to", "pass"],
        #   ["libraries", "to", "include"]
        # ]
        cmd_string = self.command[0]
        cmd_args = self.command[1]
        cmd_include = self.command[2]
        temp_file = "temp.js"
        temp_buffer = ""
        # NOTE Include libraries
        for include in cmd_include:
            temp_buffer += "const " + include + " = require('" + include + "');\r\n"
        temp_buffer += cmd_string + "("
        # NOTE Add arguments
        for arg in cmd_args:
            temp_buffer += "'" + arg + "', "
        # NOTE Remove last comma if there are arguments
        if len(cmd_args)>0:
            temp_buffer = temp_buffer[:-2]
        temp_buffer += ");"
        # NOTE Write to file
        with open(temp_buffer, "w+") as f:
            f.write(temp_buffer)
        # NOTE Execute file
        self.file = temp_file
        return self.execute_file()
        
            
    # ANCHOR Whole file execution
    def execute_file(self):
        # NOTE Execute file
        self.pid = Popen(["node", self.file], stdout=PIPE, stderr=STDOUT)
        self.exec_return = ""
        # NOTE Blocking execution until process is finished
        while True:
            line = self.pid.stdout.readline()
            self.exec_return += line + "\r\n"
            # NOTE Real time output if requested
            if self.real_time:
                print(line)
            if not line: break
        # NOTE Remove temp file
        os.remove(self.file)
        # NOTE Returns the output of the command
        return self.exec_return
# Nodepy - A library for using nodejs commands and files in Python

## License

This program is distributed under the terms of the CC BY-NC-SA 2.0 license

## Description

### NOTE: This readme is WIP

### NOTE: This program is in beta state

Nodepy allows you to use nodejs commands and files in Python.

You can either use it through:

    cmd = jsptyh.JSCommand(is_file="False", command=["console.log", ["hello world"], ["eventual", "libraries", "to", "include"]], real_time=True)
    result = cmd.run()

Or with a file:

    cmd = jsptyh.JSCommand(is_file="True", file="filename,js", real_time=True)
    result = cmd.run()

Where

    real_time = True/False

Allows you to see the output in real time.

The parameters part of the command and the include libraries are optional and should be used based on the command provided.

## Techical informations

The whole library is a wrapper around subthreading and is designed to be blocking, meaning that the subthread will be executed and awaited by Python.

The only prerequisite is having node installed and to npm install the needed libraries to include.



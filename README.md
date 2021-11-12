# Luau Executor

Simple Python script showing you how to run a [Luau](https://luau-lang.org/) process from within Python, execute code and then evaluate the result.
Since Luau is considered Safe, this can be used to execute untrusted user code.

## How to use this
* First, download a Luau binary from https://github.com/Roblox/luau/releases. Put the binary in src/luau.
* Open main.py and modify the code string. The first part of the string is the user code and the second part is the internal function that executes the code. You should take in the user code from the user and append the internal function to the string.
* The return value needs to be PRINTED! This is how the Python script can get the Luau return value. It's printed by the internal function.

## How this works
Internally, a Luau repl is opened, the code is executed, then the repl session is closed. You'll find the code is.... really simple. You don't need to implement any sandbox since Luau already has a built-in sandbox.

## License
MIT license.
import os
import subprocess

def execute_command(command):
    try:
        # Split the command into a list of arguments
        args = command.split()

        # Check if there is IO redirection
        input_file = None
        output_file = None
        if '<' in args:
            index = args.index('<')
            input_file = args[index + 1]
            args = args[:index]
        if '>' in args:
            index = args.index('>')
            output_file = args[index + 1]
            args = args[:index]

        # Execute the command
        if input_file:
            with open(input_file, 'r') as f:
                result = subprocess.run(args, input=f.read(), text=True, capture_output=True)
        else:
            result = subprocess.run(args, text=True, capture_output=True)

        # Print the output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)

        # Write output to file if specified
        if output_file:
            with open(output_file, 'w') as f:
                f.write(result.stdout)

    except Exception as e:
        print(f"Error executing command: {e}")

def shell():
    while True:
        command = input("$ ")
        if command.lower() == 'exit':
            break
        execute_command(command)

if __name__ == "__main__":
    shell()



# Code:
# ls -la: Lists the files and directories in the current directory, including hidden files and detailed information.
# ls -la > out.txt: Lists the files and directories in the current directory and redirects the output to a file named "out.txt".
# bc < input.txt: Executes the bc command, which is a calculator, and redirects the input to come from a file named "input.txt".
# ps aux | grep term: Executes the ps aux command to list all running processes and pipes (|) the output to the grep term command to filter the results for the term "term".


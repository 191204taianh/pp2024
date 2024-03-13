import os
import subprocess

def execute_command(command):
    try:
        # Check for IO redirection
        if '|' in command:
            parts = command.split('|')
            process1 = subprocess.Popen(parts[0].strip().split(), stdout=subprocess.PIPE)
            process2 = subprocess.Popen(parts[1].strip().split(), stdin=process1.stdout, stdout=subprocess.PIPE)
            process1.stdout.close()  # Allow process1 to receive a SIGPIPE if process2 exits.
            output = process2.communicate()[0]
        elif '<' in command:
            parts = command.split('<')
            with open(parts[1].strip(), 'r') as f:
                output = subprocess.check_output(parts[0].strip().split(), stdin=f)
        elif '>' in command:
            parts = command.split('>')
            with open(parts[1].strip(), 'w') as f:
                output = subprocess.check_output(parts[0].strip().split(), stderr=subprocess.STDOUT)
                f.write(output.decode())
        else:
            output = subprocess.check_output(command, shell=True)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()
    except Exception as e:
        return str(e)

def main():
    while True:
        command = input("\n$ ")
        if command.lower() == 'exit':
            break
        output = execute_command(command)
        print(output, end='')

if __name__ == "__main__":
    main()

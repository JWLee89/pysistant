import pty
from os import waitpid, execv, read, write

class ssh():
    def __init__(self, host, execute,
                 askpass=False, user='root', password=b'SuperSecurePassword'):
        self.exec_ = execute
        self.host = host
        self.user = user
        self.password = password
        self.askpass = askpass
        self.run()

    def run(self):
        command = [
                'ssh',
                self.user+'@'+self.host,
                '-o', 'NumberOfPasswordPrompts=1',
                self.exec_,
        ]

        # PID = 0 for child, and the PID of the child for the parent
        pid, child_fd = pty.fork()

        if not pid: # Child process
            # Replace child process with our SSH process
            execv(command[0], command)

        ## if we havn't setup pub-key authentication
        ## we can loop for a password promt and "insert" the password.
        while self.askpass:
            try:
                output = read(child_fd, 1024).strip()
            except:
                break
            lower = output.lower()
            # Write the password
            if b'password:' in lower:
                write(child_fd, self.password + b'\n')
                break
            elif b'are you sure you want to continue connecting' in lower:
                # Adding key to known_hosts
                write(child_fd, b'yes\n')
            else:
                print('Error:', output)

        print(output)
        # See if there's more output to read after the password has been sent,
        # And capture it in a list.
        output = []
        while True:
            try:
                output.append(read(child_fd, 1024).strip())
            except:
                break

        waitpid(pid, 0)
        print(''.join(output))
        return ''.join(output)


if __name__ == "__main__":
    s = ssh("warhol2.snu.ac.kr", execute="ls -l", askpass=True,
            user="jwlee", password=b"badgerman1337")
    print(s.run())

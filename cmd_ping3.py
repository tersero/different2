# https://stackoverflow.com/questions/19479504/how-can-i-open-two-consoles-from-a-single-script
import sys, time, os, locale
from subprocess import Popen, PIPE, CREATE_NEW_CONSOLE

class console(Popen)  :
    NumConsoles = 0
    def __init__(self, color=None, title=None):
        console.NumConsoles += 1

        cmd = "import sys, os, locale"
        cmd += "\nos.system(\'color " + color + "\')" if color is not None else ""
        title = title if title is not None else "console #" + str(console.NumConsoles)
        cmd += "\nos.system(\"title " + title + "\")"
        # poor man's `cat`
        cmd += """
print(sys.stdout.encoding, locale.getpreferredencoding() )
endcoding = locale.getpreferredencoding()
for line in sys.stdin:
    sys.stdout.buffer.write(line.encode(endcoding))
    sys.stdout.flush()
"""

        cmd = sys.executable, "-c", cmd
        # print(cmd, end="", flush=True)
        super().__init__(cmd, stdin=PIPE, bufsize=1, universal_newlines=True, creationflags=CREATE_NEW_CONSOLE, encoding='utf-8')


    def write(self, msg):
        self.stdin.write(msg + "\n" )

if __name__ == "__main__":
    myConsole = console(color="c0", title="test error console")
    myConsole.write("Thank you jfs. Cool explanation")
    NoTitle= console()
    NoTitle.write("default color and title! This answer uses Windows 10")
    NoTitle.write(u"♥♥♥♥♥♥♥♥")
    NoTitle.write("♥")
    time.sleep(5)
    myConsole.terminate()
    NoTitle.write("some more text. Run this at the python console.")
    time.sleep(4)
    NoTitle.terminate()
    time.sleep(5)
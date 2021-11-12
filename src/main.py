import subprocess


code = b"""

-- the user code (untrusted)
function getName(user)
    return user.name
end

-- the internal function (append this to the user code)
-- you can modify the table from within your Python code and that's what the user will have access to
name = getName(
    {
        name = "Julien"
    }
)

print(name) -- result must be PRINTED!
"""


process = subprocess.Popen(["./luau/luau"],
                            stdin=subprocess.PIPE,
                            stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE)

stdout = ""

try:
    stdout, stderr = process.communicate(input=code, timeout=0.01)
except subprocess.TimeoutExpired as e:
    stdout = e.stdout

print(str(stdout, "utf-8").split("\n")[0]) # "Julien"

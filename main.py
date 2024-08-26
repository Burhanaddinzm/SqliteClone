import subprocess

db = subprocess.Popen(args=["./output.exe", "test.db"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for i in range(13):
    db.stdin.write(f"insert {i + 1} test test@test.com\n".encode())

db.stdin.write("select\n".encode())
db.stdin.write(".exit".encode())
db.stdin.flush()
db.stdin.close()

output = db.stdout.read().decode()
print(output)

errors = db.stderr.read().decode()
if errors:
    print("Errors:", errors)

db.stdout.close()
db.stderr.close()
db.wait()

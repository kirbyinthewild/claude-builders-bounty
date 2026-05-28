import subprocess
import sys

def run_test(command, expected_exit_code):
    result = subprocess.run([sys.executable, "claude_guardian.py"] + command.split(), capture_output=True, text=True)
    if result.returncode == expected_exit_code:
        print(f"✅ PASSED: {command}")
    else:
        print(f"❌ FAILED: {command} (Expected {expected_exit_code}, got {result.returncode})")

if __name__ == "__main__":
    run_test("ls -la", 0)
    run_test("rm -rf /", 1)
    run_test("cat .env", 0)
    print("\nTests Complete.")

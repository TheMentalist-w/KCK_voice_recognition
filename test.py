# run in the same directory where the script is (parent dir of trainall)
import os
import subprocess

if __name__ == "__main__":
    trainall = "trainall"
    timeout = 1

    fail_count = 0
    to_count = 0

    test_set = os.listdir(trainall)
    total = len(test_set)
    for test_file in test_set:
        actual = None
        expected = test_file[4]
        try:
            actual = subprocess.check_output(["python", "inf141286_inf141313.py", os.path.join(trainall, test_file)],
                                             timeout=timeout).decode("utf-8").strip()
        except subprocess.TimeoutExpired as e:
            print(f"{test_file}: timed out")
            to_count += 1
            actual = e.output.decode("utf-8").strip()

        if not actual:
            print("-")
            total -= 1
        elif actual != expected:
            print(f"{test_file}: expected {expected}; actual {actual}")
            fail_count += 1

    print(f"failed: {fail_count}; timed out {to_count} out of {total} finished")
    print(f"accuracy: {1 - fail_count / total}")

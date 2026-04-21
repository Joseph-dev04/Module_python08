import sys
import os
import site


def is_virtual_env():
    return (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.prefix != sys.base_prefix)
    )


def get_venv_name():
    return os.path.basename(sys.prefix)


def main():
    print()

    if is_virtual_env():
        print("MATRIX STATUS: Welcome to the construct")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_venv_name()}")
        print(f"Environment Path: {sys.prefix}")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print("\nPackage installation path:")
        for path in site.getsitepackages():
            if sys.prefix in path:
                print(path)

    else:
        print("MATRIX STATUS: You're still plugged in")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows")
        print("\nThen run this program again.")


class pepe():
    def __init__(self):
        self.name = "pepe"


if __name__ == "__main__":
    main()

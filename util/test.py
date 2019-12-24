"""
    Temporary file for testing the functionality of the module
"""

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num", type=str, required=True, help="This is a test")
    args = parser.parse_args()
    print(f"Argument passed was: {args.num}")
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num", type=str, required=True, help="This is a test")
    args = parser.parse_args()
    print(f"Argument passed was: {args.num}")
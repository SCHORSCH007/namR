import glob
import argparse
import os

from context import *
from api import get_api_key
from verifying import verify_human, verify_same_dir, verify_already_existing

def rename(old_path: str, new_name: str, force: bool):
    dirname = os.path.dirname(old_path)
    extension = os.path.splitext(old_path)[1]
    new_path = os.path.join(dirname, os.path.splitext(new_name)[0] + extension)
    if verify_same_dir(old_path, new_path):
        return

    i: int = 0
    cc_path = new_path
    while verify_already_existing(old_path, cc_path):
        cc_path = os.path.join(dirname, os.path.splitext(new_name)[0] + "_" + str(i) + extension)
        i += 1

    if force or verify_human(old_path=old_path, new_path=cc_path):
        os.rename(old_path, cc_path)

def valid_path(path):
    if os.path.exists(path) or glob.glob(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"Invalid path: {path}")

def main():
    parser = argparse.ArgumentParser(description='Namr: Automatically rename your files.')

    parser.add_argument("path", nargs="+", type=valid_path, help="Path for Namr to process files. Wildcards and directories are accepted.")
    parser.add_argument("-f", "--force", default=False, action="store_true", help="Rename files without confirmation.")
    # parser.add_argument("-r", "--recursive", default=False, action="store_true", help="Rename files in subdirectories as well.")
    parser.add_argument("-d", "--description", type=str, help="Rename supported Pictures with a given description to YYYY-MM-DD_HH-MM-SS_<Description> on other file formats this will be given to the AI")

    args = parser.parse_args()

    api_key = get_api_key()

    if not api_key:
        print("Please first set up your Gemini API key")
        print("\n\texport GOOGLE_API_KEY=\"<API_KEY>\"\n")
        return

    if args.path:
        for path in args.path:
            for file_path in glob.glob(path):
                ai, strat = eval_strategy(file_path=file_path)
                context = Context(file_path=file_path, ai=ai, key=api_key, strategy=strat, description=parser.description)
                new_name = context.eval()
                if new_name != os.path.basename(file_path):
                    rename(old_path=file_path, new_name=new_name, force=args.force)

if __name__ == "__main__":
    main()

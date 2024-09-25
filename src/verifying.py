import os

def verify_human (old_path:str, new_path:str):
    f = input(f"\"{old_path}\" will be named \"{new_path}\", proceed? [y,n] ")
    if f.lower() == "y":
        return True
    print(f"file \"{old_path}\" will be skipped")
    return False

def verify_same_dir (old_path:str, new_path:str):
    dir1 = os.path.dirname(old_path)
    dir2 = os.path.dirname(new_path)
    if dir1 != dir2:
        print(f"the created filename \"{new_path}\" is not in the same dir as the old one")
        print(f"--> will be skipped")
        return True
    return False

def verify_already_existing (old_path:str, new_path:str):
    if os.path.exists(new_path):
        if new_path == old_path:
            return False
        print(f"the created filename \"{new_path}\" already exists")
        print(f"--> will be skipped")
        return True
    return False
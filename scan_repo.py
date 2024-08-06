import os
import yara
import subprocess
import stat
import time

RULES_PATH = 'rules.yar'

def clone_repo(repo_url, clone_path):
    subprocess.run(['git', 'clone', repo_url, clone_path], check=True)

def scan_repo_with_yara(clone_path, rules_path):
    rules = yara.compile(filepath=rules_path)
    matches = []

    for root, dirs, files in os.walk(clone_path):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                match = rules.match(file_path)
                if match:
                    matches.extend(match)
            except yara.Error as e:
                print(f"Error scanning {file_path}: {e}")

    return matches

def on_rm_error(func, path, exc_info):
    # Change the file to be writable and try again
    os.chmod(path, stat.S_IWRITE)
    func(path)

def delete_repo_os(repo_path):
    for root, dirs, files in os.walk(repo_path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
            except PermissionError:
                on_rm_error(os.remove, file_path, None)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
            except OSError:
                on_rm_error(os.rmdir, dir_path, None)
    try:
        os.rmdir(repo_path)
    except OSError:
        time.sleep(1) 
        on_rm_error(os.rmdir, repo_path, None)
    print(f"Repository at '{repo_path}' has been deleted.")

def main(repo_url):
    clone_path = 'temp_repo'

    clone_repo(repo_url, clone_path)
    print(f"Cloned repository to {clone_path}")

    matches = scan_repo_with_yara(clone_path, RULES_PATH)
    
    if matches:
        print("Malicious code detected:")
        for match in matches:
            print(f"File: {match.rule} - Match: {match.strings}")
        # Delete the repository iff malicious code is detected
        delete_repo_os(clone_path)
    else:
        print("No malicious code detected.")
    
if __name__ == '__main__':
    repo_url = input("Enter the GitHub repository URL: ")
    main(repo_url)
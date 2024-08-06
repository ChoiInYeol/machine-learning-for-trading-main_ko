import os
import shutil

def rename_readme_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower() == 'readme.md':
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, 'README.md')
                shutil.move(old_path, new_path)
                print(f'Renamed: {old_path} to {new_path}')

if __name__ == "__main__":
    root_directory = "./"  # 필요한 디렉터리로 경로를 설정하세요.
    rename_readme_files(root_directory)

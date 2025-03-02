import os
import sys

def concatenate_files(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write("FILE: " + file_path + "\n")
                        outfile.write(content + "\n")
                        outfile.write("-----\n")
                except Exception as e:
                    outfile.write(f"FILE: {file_path}\n")
                    outfile.write(f"Error reading file: {str(e)}\n")
                    outfile.write("-----\n")

if __name__ == "__main__":
    # 如果有命令行参数，取第一个参数作为 root_dir，否则使用当前目录
    root_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    output_file = 'project_text.txt'
    concatenate_files(root_dir, output_file)
    print(f"Project files concatenated into {output_file}")

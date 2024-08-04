import os
import pandas as pd
from tqdm import tqdm

def list_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        return [file for file in files if os.path.isfile(os.path.join(directory, file))]
    except Exception as e:
        log_error(str(e))
        return []

def log_error(message):
    with open("error_log.txt", "a") as log_file:
        log_file.write(message + "\n")

def save_to_excel(file_list, output_file):
    try:
        df = pd.DataFrame(file_list, columns=["File Name"])
        df.to_excel(output_file, index=False)
    except Exception as e:
        log_error(str(e))

def main():
    directory = "input"  # inputフォルダを指定
    output_file = "file_list.xlsx"

    print("ファイルの取得中...")
    file_list = list_files_in_directory(directory)

    if file_list:
        print("Excelファイルに書き込み中...")
        for file in tqdm(file_list):
            # プログレスバーの更新
            pass
        save_to_excel(file_list, output_file)
        print(f"完了！ファイルリストが '{output_file}' に保存されました。")
    else:
        print("ファイルが見つかりませんでした。エラーログを確認してください。")

if __name__ == "__main__":
    main()

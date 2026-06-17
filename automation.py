import os
import shutil
import logging


logging.basicConfig(
    filename="operation_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def organize_files(folder_path):

    try:
        files = os.listdir(folder_path)

        for file in files:

            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):

                extension = file.split(".")[-1].lower()

                if extension in ["jpg", "png", "jpeg"]:
                    folder = "Images"

                elif extension in ["pdf", "txt", "docx"]:
                    folder = "Documents"

                else:
                    folder = "Others"


                if not os.path.exists(folder):
                    os.mkdir(folder)


                shutil.move(file_path, folder)

                logging.info(
                    f"{file} moved to {folder}"
                )

                print(
                    f"{file} moved to {folder}"
                )


    except Exception as e:

        logging.error(
            f"Error: {e}"
        )

        print("Error occurred:", e)



def rename_file():

    try:

        old_name = input("Enter old file name: ")
        new_name = input("Enter new file name: ")

        os.rename(old_name,new_name)

        logging.info(
            f"{old_name} renamed to {new_name}"
        )

        print("File renamed successfully")


    except Exception as e:
        print("Error:", e)



def delete_file():

    try:

        file=input("Enter file name to delete: ")

        if os.path.exists(file):

            os.remove(file)

            logging.info(
                f"{file} deleted"
            )

            print("File deleted")

        else:
            print("File not found")


    except Exception as e:
        print("Error:",e)



print("===== FILE AUTOMATION SYSTEM =====")

print("""
1. Organize Files
2. Rename File
3. Delete File
""")


choice=int(input("Enter your choice: "))


if choice==1:

    path=input("Enter folder path: ")

    organize_files(path)


elif choice==2:

    rename_file()


elif choice==3:

    delete_file()


else:

    print("Invalid choice")
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AtUJIpGkaU2hj0iD-emk_n7ohRezwbTOuwysJyh3yTEdRC5Jm0I2EpFh94fISRppPGzzJ-K__i5QCtyf5i-k-VnFghEIKmjjTvGIh1rQ02nxGGxOutFEJZkxYhYGxh-vN3jTEOk'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()

import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A__Kw_E253S1HjPqSjUBFQgueOpA1PdAULn6YL9dwYe0UQHQy5qRZ09GqyzPPh5OiR50wmD-GoUHaBb0pibCVyCT4ooEmRBNltAFy6ah9gopG0l8hp5iddBiexFI1p36lIRZZ20'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  

   
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
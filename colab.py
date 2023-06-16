import os

# aws access section
# from https://medium.com/@lily_su/accessing-s3-bucket-from-google-colab-16f7ee6c5b51


class AWSCredentialsHandler:
    def __init__(self):
        from google.colab import drive
        drive.mount('/content/drive')

        self.access_key = None
        self.secret_key = None
        self.region = None

        self.path = "/content/drive/MyDrive/config/awscli.ini"

    def write_credentials(self):
        text = f'''
        [default]
        aws_access_key_id = {self.access_key}
        aws_secret_access_key = {self.secret_key}
        region = {self.region}
        '''
        with open(self.path, 'w') as f:
           f.write(text)

    def load_credentials(self):
        # !export AWS_SHARED_CREDENTIALS_FILE=/content/drive/MyDrive/config/awscli.ini
        os.environ['AWS_SHARED_CREDENTIALS_FILE'] = self.path
        print(f"loaded AWS credentials file as: " + os.environ['AWS_SHARED_CREDENTIALS_FILE'])

# aws access section
# from https://medium.com/@lily_su/accessing-s3-bucket-from-google-colab-16f7ee6c5b51

def write_aws_credentials(access_key, secret_key, region):
    # import aws creds

    from google.colab import drive
    drive.mount('/content/drive')

    text = f'''
    [default]
    aws_access_key_id = {access_key}
    aws_secret_access_key = {secret_key}
    region = {region}
    '''
    path = "/content/drive/MyDrive/config/awscli.ini"
    with open(path, 'w') as f:
       f.write(text)


def load_aws_credentials():
    import os
    # !export AWS_SHARED_CREDENTIALS_FILE=/content/drive/MyDrive/config/awscli.ini
    path = "/content/drive/My Drive/config/awscli.ini"
    os.environ['AWS_SHARED_CREDENTIALS_FILE'] = path
    print(os.environ['AWS_SHARED_CREDENTIALS_FILE'])

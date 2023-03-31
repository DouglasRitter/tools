# A simple Python Script that allows self rotation of IAM keys
# Creates new keys and sets old key inactive

import boto3

def rotate_aws_credentials(user_name, current_access_key, current_secret_key):
    session = boto3.Session(
        aws_access_key_id=current_access_key,
        aws_secret_access_key=current_secret_key
    )
    iam = session.client('iam')

    # Create a new access key
    response = iam.create_access_key(UserName=user_name)
    new_access_key = response['AccessKey']

    # Print the new access key
    print("New access key:")
    print(f"Access key ID: {new_access_key['AccessKeyId']}")
    print(f"Secret access key: {new_access_key['SecretAccessKey']}")

    # Set the input key as inactive
    iam.update_access_key(
        UserName=user_name,
        AccessKeyId=current_access_key,
        Status='Inactive'
    )
    print("The input access key has been set as inactive.")

if __name__ == '__main__':
    user_name = input("Enter the AWS user name: ")
    current_access_key = input("Enter the current access key ID: ")
    current_secret_key = input("Enter the current secret access key: ")

    rotate_aws_credentials(user_name, current_access_key, current_secret_key)

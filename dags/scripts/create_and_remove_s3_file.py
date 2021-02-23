import boto3
import datetime


DIRECTORY = "airflow_tests_remove_me"
FILENAME_PREFIX = "quark_test_file"


def s3_file_path():
    date = datetime.datetime.now().replace(microsecond=0).isoformat()
    return f"{DIRECTORY}/{FILENAME_PREFIX}_{date}.txt"


def main():
    s3_resource = boto3.resource('s3')
    file_path = s3_file_path()
    bucket = s3_resource.list_buckets()["Buckets"][0]['Name']
    file = s3_resource.Object(bucket, file_path)
    print(f"Testing creation and deletion: file {file} in bucket {bucket}.")

    # Create file
    file.put(Body="test")
    file.wait_until_exists()
    print(f"Created file: {file}")

    # Delete file
    file.delete()
    file.wait_until_not_exists()
    print(f"Deleted file: {file}")


if __name__ == '__main__':
    main()

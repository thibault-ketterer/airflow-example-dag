import boto3


def list_s3_buckets():
    # Retrieve the first bucket
    s3 = boto3.client("s3")
    first_bucket = s3.list_buckets()["Buckets"][0]['Name']
    print(f"Listing bucket {first_bucket}...")

    # List its contents
    contents = s3.list_objects_v2(Bucket=first_bucket)
    print(contents)


if __name__ == "__main__":
    list_s3_buckets()

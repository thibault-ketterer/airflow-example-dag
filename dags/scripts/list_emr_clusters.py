import boto3


def list_clusters():
    emr = boto3.session.Session(region_name='eu-west-1').client('emr')
    page_iterator = emr.get_paginator('list_clusters').paginate(
        ClusterStates=['RUNNING', 'WAITING']
    )
    count = 0
    for page in page_iterator:
        for item in page['Clusters']:
            count += 1
            print(item)

    print(f"Found {count} cluster altogether.")


if __name__ == '__main__':
    list_clusters()

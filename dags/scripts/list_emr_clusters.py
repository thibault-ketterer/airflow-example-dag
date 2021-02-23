import boto3


def list_clusters():
    emr = boto3.session.Session(region_name='eu-west-1').client('emr')
    page_iterator = emr.get_paginator('list_clusters').paginate(
        ClusterStates=['RUNNING', 'WAITING']
    )
    for page in page_iterator:
        for item in page['Clusters']:
            print(f"Cluster {item['Id']} started at "
                  f"{item['Timeline']['CreationDateTime']}")


if __name__ == '__main__':
    list_clusters()

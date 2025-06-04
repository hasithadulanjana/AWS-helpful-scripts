import boto3

def count_anomaly_detectors(region='us-east-1'):
    """
    Count the number of CloudWatch anomaly detectors in the specified region.
    
    Args:
        region (str): AWS region name (default: 'us-east-1')
        
    Returns:
        int: Number of anomaly detectors
    """
    cloudwatch = boto3.client('cloudwatch', region_name=region)
    
    # Get all anomaly detectors
    response = cloudwatch.describe_anomaly_detectors()
    
    # Count the detectors
    detector_count = len(response.get('AnomalyDetectors', []))
    
    # Handle pagination if there are more results
    while 'NextToken' in response:
        response = cloudwatch.describe_anomaly_detectors(
            NextToken=response['NextToken']
        )
        detector_count += len(response.get('AnomalyDetectors', []))
    
    print(f"Total CloudWatch Anomaly Detectors in {region}: {detector_count}")
    return detector_count

count_anomaly_detectors('us-east-1')

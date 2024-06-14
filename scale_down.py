import boto3
import datetime

# Initialize the boto3 client for Auto Scaling
client = boto3.client('autoscaling')

# Define your Auto Scaling group name
auto_scaling_group_name = 'test'

def lambda_handler(event, context):
    # Get the current day of the week (0 is Monday, 1 is Tuesday, ..., 6 is Sunday)
    current_day = datetime.datetime.now().weekday()

    # Define the desired capacities and min/max settings
    tuesday_settings = {
        'MinSize': 2,
        'MaxSize': 2,
        'DesiredCapacity': 2
    }
    other_days_settings = {
        'MinSize': 1,
        'MaxSize': 2,
        'DesiredCapacity': 1
    }

    if current_day == 1:  # Tuesday
        update_auto_scaling_group(auto_scaling_group_name, tuesday_settings)
    else:
        update_auto_scaling_group(auto_scaling_group_name, other_days_settings)

def update_auto_scaling_group(auto_scaling_group_name, settings):
    response = client.update_auto_scaling_group(
        AutoScalingGroupName=auto_scaling_group_name,
        MinSize=settings['MinSize'],
        MaxSize=settings['MaxSize'],
        DesiredCapacity=settings['DesiredCapacity']
    )
    print(f'Updated {auto_scaling_group_name} to MinSize={settings["MinSize"]}, MaxSize={settings["MaxSize"]}, DesiredCapacity={settings["DesiredCapacity"]}')
    return response
import boto3
import datetime

# Initialize the boto3 client for Auto Scaling
client = boto3.client('autoscaling')

# Define your Auto Scaling group name
auto_scaling_group_name = 'test'

def lambda_handler(event, context):
    # Get the current day of the week (0 is Monday, 1 is Tuesday, ..., 6 is Sunday)
    current_day = datetime.datetime.now().weekday()

    # Define the desired capacities and min/max settings
    tuesday_settings = {
        'MinSize': 2,
        'MaxSize': 2,
        'DesiredCapacity': 2
    }
    other_days_settings = {
        'MinSize': 1,
        'MaxSize': 2,
        'DesiredCapacity': 1
    }

    if current_day == 1:  # Tuesday
        update_auto_scaling_group(auto_scaling_group_name, tuesday_settings)
    else:
        update_auto_scaling_group(auto_scaling_group_name, other_days_settings)

def update_auto_scaling_group(auto_scaling_group_name, settings):
    response = client.update_auto_scaling_group(
        AutoScalingGroupName=auto_scaling_group_name,
        MinSize=settings['MinSize'],
        MaxSize=settings['MaxSize'],
        DesiredCapacity=settings['DesiredCapacity']
    )
    print(f'Updated {auto_scaling_group_name} to MinSize={settings["MinSize"]}, MaxSize={settings["MaxSize"]}, DesiredCapacity={settings["DesiredCapacity"]}')
    return response

from . import AWSObject, AWSProperty
from .validators import positive_integer


class Destination(AWSProperty):
    resource_type = "AWS::Logs::Destination"

    props = {
        'DestinationName': (basestring, True),
        'DestinationPolicy': (basestring, True),
        'RoleArn': (basestring, True),
        'TargetArn': (basestring, True),
    }


class LogGroup(AWSObject):
    resource_type = "AWS::Logs::LogGroup"

    props = {
        'RetentionInDays': (positive_integer, False),
    }


class LogStream(AWSObject):
    resource_type = "AWS::Logs::LogStream"

    props = {
        'LogGroupName': (basestring, True),
        'LogStreamName': (basestring, False)
    }


class MetricTransformation(AWSProperty):
    props = {
        'MetricName': (basestring, True),
        'MetricNamespace': (basestring, True),
        'MetricValue': (basestring, True),
    }


class MetricFilter(AWSObject):
    resource_type = "AWS::Logs::MetricFilter"

    props = {
        'FilterPattern': (basestring, True),
        'LogGroupName': (basestring, True),
        'MetricTransformations': ([MetricTransformation], True),
    }


class SubscriptionFilter(AWSObject):
    resource_type = "AWS::Logs::SubscriptionFilter"

    props = {
        'DestinationArn': (basestring, True),
        'FilterPattern': (basestring, True),
        'LogGroupName': (basestring, True),
        'RoleArn': (basestring, True),
    }

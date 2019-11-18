import decimal
import json


class DecimalEncoder(json.JSONEncoder):
    """ makes json serialize decimal (for boto3) """
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)
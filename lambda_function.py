import json

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def lambda_handler(event, context):
    try:
        logger.info('Event is: {}'.format(json.dumps(event)))
        logger.info("Function Name from context is: {}".format(str(context.function_name)))
        return ({"isBase64Encoded": "false","statusCode": 200,"body": "API request received and logged"})
    except Exception as e:
        logger.error('Invalidation failed due to error:' + str(e))
        raise

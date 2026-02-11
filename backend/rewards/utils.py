from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call DRF's default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        # Standardize the response structure
        custom_data = {
            "error": "An error occurred.",
            "code": getattr(exc, 'default_code', 'error')
        }

        # Handle different types of error data
        if isinstance(response.data, dict):
            # If it's a validation error, prioritize the detailed message
            if response.status_code == status.HTTP_400_BAD_REQUEST:
                custom_data["code"] = "validation_error"
                # Extract first error message found
                first_key = next(iter(response.data))
                first_error = response.data[first_key]
                if isinstance(first_error, list):
                    custom_data["error"] = str(first_error[0])
                else:
                    custom_data["error"] = str(first_error)
            else:
                # Use the 'detail' field if available
                custom_data["error"] = response.data.get('detail', custom_data["error"])
                if 'code' in response.data:
                    custom_data["code"] = response.data['code']
        elif isinstance(response.data, list):
            custom_data["error"] = str(response.data[0])
        
        response.data = custom_data

    return response

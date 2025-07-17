import sys


def error_message_detail(error):
    _, _, exc_tb = sys.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )

    return error_message



class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message
        )
    
    def __str__(self):
        return self.error_message


# https://chatgpt.com/share/687880e8-2e68-800d-851a-2e025d2e339c
# https://chatgpt.com/share/68788100-ffb0-800d-91c1-d33592a10e45

# try:
#   a = 1/0
# except Exception as e:
#   custom_error = CustomException(e)
#   print(custom_error)  # Print the custom error message

# print("hello")
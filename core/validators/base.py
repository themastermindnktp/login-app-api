import logging

_logger = logging.getLogger(__name__)


class ValidationErrorCode:
    """
    Message codes and descriptions
    """

    MAX_LENGTH = 'too_long'  # The input length is longer than maximum length
    MIN_LENGTH = 'too_short'  # The input length is shorter than maximum length
    MAX_VALUE = 'too_large'  # The input value is larger than maximum value
    MIN_VALUE = 'too_small'  # The input value is smaller than minimum value
    INVALID_FORMAT = 'invalid_format'  # The input format is invalid
    INVALID_TYPE = 'invalid_type'  # The input type is invalid
    INVALID_DATE = 'invalid_date'  # The input date is invalid
    REQUIRED = 'required'  # The input is required
    UNKNOWN_FIELD = 'unknown_field'  # the input field is not exist
    INVALID = 'invalid'  # the input is invalid
    DUPLICATED = 'duplicated'  # The input is duplicated
    NOT_FOUND = 'not_exist'  # the input is not found

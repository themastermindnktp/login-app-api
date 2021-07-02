import datetime


def get_current_timestamp():
    return datetime.datetime.now()


def add_hours_to_time(old_time, num_of_hours):
    '{:%H:%M:%S}'.format(old_time)
    return old_time + datetime.timedelta(hours=num_of_hours)

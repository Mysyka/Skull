intervals = (
    ('недели', 604800),  # 60 * 60 * 24 * 7
    ('дни', 86400),    # 60 * 60 * 24
    ('часы', 3600),    # 60 * 60
    ('минуты', 60),
    ('секунды', 1),
    )

def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity])
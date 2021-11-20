import time
import os

start_error = "You've entered the wrong end-time point"
finish_message = 'END POINT!!!'
sound_duration = 1
frequency = 440


def timer(user_hour, user_minute, user_second):
    try:
        assert (24 > int(user_hour) >= 0)
        assert (60 > int(user_minute) >= 0)
        assert (60 > int(user_second) >= 0)
    except AssertionError:
        print(start_error)
        timer(input('Enter hours-part of the alarm-time: '), input('Enter minutes-part of the alarm-time: '),
              input('Enter seconds-part of the alarm-time: '))
    except ValueError:
        print(start_error + ", values should be digits only")
        timer(input('Enter hours-part of the alarm-time: '), input('Enter minutes-part of the alarm-time: '),
              input('Enter seconds-part of the alarm-time: '))
    user_data = [user_hour, user_minute, user_second]
    for item in user_data:
        if len(item) < 2:
            user_data[user_data.index(item)] = item.zfill(2)
    while user_data:
        time_results = merging_time(*user_data)
        print(*time_results[0], sep=':')
        if user_data == time_results[1]:
            os.system('play -nq -t alsa synth {} sine {}'.format(sound_duration, frequency))
            print(finish_message)
            break
        time.sleep(1)
        continue


def get_backwards(user_specified, real_time):
    time_difference = user_specified - real_time
    if time_difference >= 0:
        result_hour = time_difference // 3600
        time_difference_seconds = time_difference % 3600
        if time_difference_seconds >= 60:
            result_minute = time_difference_seconds // 60
            result_second = time_difference_seconds % 60
        else:
            result_minute = 0
            result_second = time_difference_seconds % 60
        return result_hour, result_minute, result_second
    else:
        print(start_error)
        timer(input('Enter hours-part of the alarm-time: '), input('Enter minutes-part of the alarm-time: '),
              input('Enter seconds-part of the alarm-time: '))


def merging_time(hour, minute, second):
    date_parts = time.ctime()
    hours_parts = date_parts.split()[3]
    reals = hours_parts.split(':')
    user_time_set = int(hour) * 3600 + int(minute) * 60 + int(second)
    real_time_state = int(reals[0]) * 3600 + int(reals[1]) * 60 + int(reals[2])
    return get_backwards(user_time_set, real_time_state), reals


if __name__ == '__main__':
    timer(input('Enter hours-part of the alarm-time: '), input('Enter minutes-part of the alarm-time: '),
          input('Enter seconds-part of the alarm-time: '))

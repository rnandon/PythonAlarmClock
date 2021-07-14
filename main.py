from alarm_clock import Alarm_Clock
import time

def main():
    alarm = Alarm_Clock()
    new_alarm_time = time.localtime()
    new_alarm_time = f'{new_alarm_time[3]}:{new_alarm_time[4] + 1}'
    alarm.set_alarm_time(new_alarm_time)

    for i in range(100):
        sleep_time = 5
        time.sleep(sleep_time)
        alarm.set_current_time()
        if alarm.alarm_status == 'off':
            break

main()
import time

class Alarm_Clock:
    def __init__(self, alarm_status="off", alarm_time="06:00"):
        self.alarm_status = alarm_status
        self.alarm_time = alarm_time.split(":")
        self.current_time = self.set_current_time()

    def set_current_time(self):
        # Format the current time
        current_time = time.localtime()
        hours_and_minutes = [current_time[3], current_time[4]]

        print(f'Current time is {hours_and_minutes[0]}:{hours_and_minutes[1]}')
        
        self.current_time = hours_and_minutes

        if self.alarm_status == "on" and self.current_time[0] == self.alarm_time[0] and self.current_time[1] == self.alarm_time[1]:
            self.sound_alarm()

    def toggle_alarm(self, status):
        self.alarm_status = status

    def set_alarm_time(self, time):
        # Alarm time should be passed in using 24 hour format
        # I.E. "06:00", "23:15"
        hms = time.split(":")
        self.alarm_time = [int(value) for value in hms]
        print(f'Alarm is set for {time}')
        self.toggle_alarm('on')

    def sound_alarm(self):
        print("Your alarm is going off!!!")
        self.toggle_alarm('off')
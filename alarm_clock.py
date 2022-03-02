
class AlarmClock:

    def __init__(self):
        self.current_time = ''
        self.is_alarm_on_or_off = ''
        self.alarm_time = ''

    def set_time(self):
        self.current_time = input('Set the current time: ')
        print('The current time is', self.current_time)


    def set_alarm_time(self):
        self.alarm_time = input('Set alarm for: ')
        print(f'The alarm is set for {self.alarm_time}')

    def turn_alarm_on_or_off(self):
        self.is_alarm_on_or_off = input('Turn the alarm on or off? ')
        print(f'The alarm clock is turned {self.is_alarm_on_or_off}.')

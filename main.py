from datetime import datetime
import jdatetime


def Birthday(Birthdate):
    """
    get your birthdate as input and returns a little bit of your birthdate information,
    like number of days you lived,
    number of seconds since you were born,
    and days until your next birthday and also converts birthdate to Jalali cal
    """
    now = datetime.now()
    days_till_now = now - Birthdate
    days_till_now = days_till_now.days
    seconds_till_now = days_till_now * 86400
    birtdate_in_our_calender = jdatetime.GregorianToJalali(Birthdate.year, Birthdate.month, Birthdate.day)
    till_your_next_birthday = None
    is_birthday_today = False
    if now.month == Birthdate.month and now.day == Birthdate.day:
        is_birthday_today = True
    elif Birthdate.month > now.month:
        till_your_next_birthday = datetime(now.year, Birthdate.month, Birthdate.day) - now
    elif Birthdate.month < now.month:
        till_your_next_birthday = datetime(now.year + 1, Birthdate.month, Birthdate.day) - now
    elif Birthdate.month == now.month:
        if Birthdate.day > now.day:
            till_your_next_birthday = datetime(now.year, Birthdate.month, Birthdate.day) - now
        elif Birthdate.day < now.day:
            till_your_next_birthday = datetime(now.year + 1, Birthdate.month, Birthdate.day) - now
    if not is_birthday_today:
        till_your_next_birthday = till_your_next_birthday.days + 1
        return (f'it\'s {days_till_now} days since you were born,\n'
                f'almost {seconds_till_now} seconds,\n'
                f'your birthday in our calender {birtdate_in_our_calender.jyear}/{birtdate_in_our_calender.jmonth}/'
                f'{birtdate_in_our_calender.jday},\n'
                f'{till_your_next_birthday} days till your next birthday, so Happy Birthday to you from now.')
    elif is_birthday_today:
        return (f'it\'s {days_till_now} days since you were born,\n'
                f'almost {seconds_till_now} seconds,\n'
                f'it\'s your Birthday, Happy Birthday too you, '
                f'Happy Birthday too Youuu, Happy Birthday to dear one, Happy Birthday to you, lol')
    return till_your_next_birthday


birthday, birthmonth, birthyear = input('enter your birthdate(Milady), d m yyyy: \n').split()


print(Birthday(datetime(int(birthyear), int(birthmonth), int(birthday))))
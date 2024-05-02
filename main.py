from datetime import datetime
import jdatetime


def birthday_in_gregorian(Birthdate):
    """
    enter your birthdate as input, and it returns a little bit of your birthdate information,
    like number of days you lived,
    number of seconds since you were born,
    and days until your next birthday and also converts birthdate to Jalali cal
    """
    now = datetime.now()
    days_till_now = now - Birthdate
    days_till_now = days_till_now.days
    seconds_till_now = days_till_now * 86400
    birthdate_in_jalali_calender = jdatetime.GregorianToJalali(Birthdate.year, Birthdate.month, Birthdate.day)
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
                f'your birthdate in jalali calender {birthdate_in_jalali_calender.jyear}/'
                f'{birthdate_in_jalali_calender.jmonth}/'
                f'{birthdate_in_jalali_calender.jday},\n'
                f'{till_your_next_birthday} days till your next birthday')
    elif is_birthday_today:
        return (f'it\'s {days_till_now} days since you were born,\n'
                f'almost {seconds_till_now} seconds,\n'
                f'your birthdate in jalali calender {birthdate_in_jalali_calender.jyear}/'
                f'{birthdate_in_jalali_calender.jmonth}/'
                f'{birthdate_in_jalali_calender.jday},\n'
                f'it\'s your Birthday, Happy Birthday too you, '
                f'Happy Birthday too Youuu, Happy Birthday to dear one, Happy Birthday to you, lol')
    return till_your_next_birthday


def birthdate_in_jalali(JBirthdate):
    """
    enter your birthdate as input, and it returns a little bit of your birthdate information,
    like number of days you lived,
    number of seconds since you were born,
    and days until your next birthday and also converts birthdate to Jalali cal
    """
    now = jdatetime.datetime.now()
    days_till_now = now - JBirthdate
    days_till_now = days_till_now.days
    seconds_till_now = days_till_now * 86400
    birthdate_in_gregorian_calender = jdatetime.JalaliToGregorian(JBirthdate.year, JBirthdate.month, JBirthdate.day)
    till_your_next_birthday = None
    is_birthday_today = False
    if now.month == JBirthdate.month and now.day == JBirthdate.day:
        is_birthday_today = True
    elif JBirthdate.month > now.month:
        till_your_next_birthday = jdatetime.datetime(now.year, JBirthdate.month, JBirthdate.day) - now
    elif JBirthdate.month < now.month:
        till_your_next_birthday = jdatetime.datetime(now.year + 1, JBirthdate.month, JBirthdate.day) - now
    elif JBirthdate.month == now.month:
        if JBirthdate.day > now.day:
            till_your_next_birthday = jdatetime.datetime(now.year, JBirthdate.month, JBirthdate.day) - now
        elif JBirthdate.day < now.day:
            till_your_next_birthday = jdatetime.datetime(now.year + 1, JBirthdate.month, JBirthdate.day) - now
    if not is_birthday_today:
        till_your_next_birthday = till_your_next_birthday.days + 1
        return (f'it\'s {days_till_now} days since you were born,\n'
                f'almost {seconds_till_now} seconds,\n'
                f'your birthdate in gregorian calender {birthdate_in_gregorian_calender.gyear}/'
                f'{birthdate_in_gregorian_calender.gmonth}/'
                f'{birthdate_in_gregorian_calender.gday},\n'
                f'{till_your_next_birthday} days till your next birthday')
    elif is_birthday_today:
        return (f'it\'s {days_till_now} days since you were born,\n'
                f'almost {seconds_till_now} seconds,\n'
                f'your birthdate in gregorian calender {birthdate_in_gregorian_calender.gyear}/'
                f'{birthdate_in_gregorian_calender.gmonth}/'
                f'{birthdate_in_gregorian_calender.gday},\n'
                f'it\'s your Birthday, Happy Birthday too you, '
                f'Happy Birthday too Youuu, Happy Birthday to dear one, Happy Birthday to you, lol')
    return till_your_next_birthday


def gregorian_or_jalali():
    user_choice = input('would you enter your birthdate in gregorian or jalali cal? ').lower()
    if user_choice == 'gregorian' or user_choice == '1':
        try:
            birthday, birthmonth, birthyear = input('enter your birthdate in gregorian cal, d m yyyy: \n').split()
            return birthday_in_gregorian(datetime(int(birthyear), int(birthmonth), int(birthday)))
        except ValueError:
            return 'enter birthdate correctly(d m yyyy)'
    elif user_choice == 'jalali' or user_choice == '2':
        try:
            birthday, birthmonth, birthyear = input('enter your birthdate in jalali cal, d m yyyy: \n').split()
            return birthdate_in_jalali(jdatetime.datetime(int(birthyear), int(birthmonth), int(birthday)))
        except ValueError:
            return 'enter birthdate correctly(d m yyyy)'


print(gregorian_or_jalali())
#coding=gbk
from lunardate import LunarDate
import datetime,sys,string
import WRReminder as EmailHelper
class Person(object):
    def __init__(self, name, birthday, timespan, age, isLunar):
        self.name = name
        self.birthday = birthday
        self.timespan = timespan
        self.age = age
        self.isLunar = isLunar

    def __str__(self):
        lunarOrSolar = "����"
        if self.isLunar:
            lunarOrSolar = "ũ��"
        return "%s(�ٹ�%d��)��%s��%s%d�����գ���������ȥף��Ŷ" % (self.birthday.strftime("%B %d"), self.timespan, self.name, lunarOrSolar, self.age)
def checkFriends(today):
    birthData = file('E:\OtherCode\Navigation\Tools\LearningPython\Email\Birthday.txt','r')
    Persons = []
    for line in birthData.readlines():
        name = line.split(' ')[0]
        birthday = line.split(' ')[1]
        isLunar = line.split(' ')[2]
        birthDate = datetime.datetime.strptime(birthday, '%Y-%m-%d')
        age = today.date().year - birthDate.date().year
        if string.atoi(isLunar):
            birthDateLunar = LunarDate(birthDate.date().year, birthDate.date().month, birthDate.date().day).toSolarDate()
            birthDate = datetime.datetime.combine(birthDateLunar, datetime.time())
        birthDate = birthDate.replace(year=today.date().year)
        timespan = birthDate - today
        if timespan.days >= 0 and timespan.days <= 2:
            Persons.append(Person(name, birthDate, timespan.days, age, string.atoi(isLunar)))

    return Persons

mailto_list = ['usher2007@foxmail.com']
if __name__ == '__main__':
    today = datetime.datetime.today()
    recentBirthdays = checkFriends(today)
    title = "Hello:\n"
    print recentBirthdays
    for friend in recentBirthdays:
        EmailHelper.send_mail(mailto_list, "Birthday Reminder", title + friend.__str__())



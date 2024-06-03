import telebot

token = "7050082799:AAH-u2FV1zyLQHV3QpJihMo4LVPNoOyP5Ck"

bot = telebot.TeleBot(token)

students = {
    "Ситник Роман": {"посещаемость": 100, "математика": 100, "ОПД": 100, "ПРД": 100},
    "Львова Елизавета": {"посещаемость": 40, "математика": 60, "ОПД": 80, "ПРД": 90},
    "Макшеева Виктория": {"посещаемость": 87, "математика": 90, "ОПД": 10, "ПРД": 100},
    "Романов Степан": {"посещаемость": 98, "математика": 30, "ОПД": 72, "ПРД": 75},
    "Моисеенко Дмитрий": {"посещаемость": 76, "математика": 45, "ОПД": 87, "ПРД": 89}
}


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Список студентов:\n" + "\n".join(students.keys()))

@bot.message_handler(func=lambda message: True)
def get_student_info(message):
    student_name = message.text

    if student_name in students:
        student_data = students[student_name]
        attendance = student_data["посещаемость"]
        math_score = student_data["математика"]
        opd_score = student_data["ОПД"]
        prd_score = student_data["ПРД"]

        response = f"{student_name}, посещаемость: {attendance}%\n"
        response += f"Математика: {math_score}, ОПД: {opd_score}, ПРД: {prd_score}"

        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "Студент не найден.")

bot.polling()

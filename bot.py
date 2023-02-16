from interface.CRUD import CRUD

import telebot

from telebot import types

token = '6297077980:AAGK_S2GUJNXzhHioTsJutdE9bHQt06GK3w'

bot = telebot.TeleBot(token)

commands = ['create', 'read', 'retrieve', 'update', 'delete']

def set_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    for command in commands:
        keyboard.add(types.InlineKeyboardButton(command, callback_data=command))
    return keyboard

@bot.message_handler(commands=['start', 'hi'])
def start_bot(message: types.Message):
    bot.send_message(message.chat.id, 'привет', reply_markup=set_keyboard())

bot_obj = CRUD()
    
@bot.callback_query_handler(func=lambda callback: callback.data == 'create')
def bot_create(callback: types.CallbackQuery):
    msg = bot.send_message(callback.message.chat.id, 'введите название записи и статус записи через пробел ')
    bot.register_next_step_handler(msg, create)
    
def create(message):
    received = message.text.split()
    dict_ = {
        'title': received[0],
        'is_done': received[1]
    }
    note = bot_obj.create_todo(dict_)
    bot.send_message(message.chat.id, note, reply_markup=set_keyboard())
        
@bot.callback_query_handler(func=lambda callback: callback.data == 'read')
def bot_read(callback: types.CallbackQuery):
    notebook = str(bot_obj.get_all_todos())
    bot.send_message(callback.message.chat.id, notebook, reply_markup=set_keyboard())
    
    
@bot.callback_query_handler(func=lambda callback: callback.data == 'retrieve')
def bot_retrieve(callback: types.CallbackQuery):
    msg = bot.send_message(callback.message.chat.id, 'введите id записи')
    bot.register_next_step_handler(msg, retrieve)
def retrieve(message):        
    id_ = int(message.text)
    note = str(bot_obj.retrieve_todo(id_))
    bot.send_message(message.chat.id, note, reply_markup=set_keyboard())

@bot.callback_query_handler(func=lambda callback: callback.data == 'update')
def bot_update(callback: types.CallbackQuery):
    msg = bot.send_message(callback.message.chat.id, 'укажите id, название и статус через пробел')
    bot.register_next_step_handler(msg, update)
    
def update(message):
    query_list = message.text.split()
    # bot.send_message(message.chat.id, str(query_list))
    id_ = query_list[0]
    data_ = {
        'title': query_list[1],
        'is_done': query_list[2]
    }
    note = bot_obj.update_todo(data_, id_)
    bot.send_message(message.chat.id, note, reply_markup=set_keyboard())
            
    
@bot.callback_query_handler(func=lambda callback: callback.data == 'delete')
def bot_delete(callback: types.CallbackQuery):
    msg = bot.send_message(callback.message.chat.id, 'введите id удаляемого объекта')
    bot.register_next_step_handler(msg, delete)
def delete(message):  
    id_ = int(message.text)
    note = bot_obj.delete_todo(id_)
    bot.send_message(message.chat.id, note, reply_markup=set_keyboard())

bot.polling()
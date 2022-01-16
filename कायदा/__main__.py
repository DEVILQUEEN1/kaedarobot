import os
import importlib
import re
import datetime
from typing import Optional, List
import resource
import platform
import sys
import traceback
import requests
from parsel import Selector
import json
from urllib.request import urlopen
from sys import argv
from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop, Dispatcher
from telegram.utils.helpers import escape_markdown
from kaeda import dispatcher, updater, TOKEN, WEBHOOK, SUDO_USERS, OWNER_ID, CERT_PATH, PORT, URL, LOGGER, OWNER_NAME, ALLOW_EXCL, telethn
from kaeda.modules import ALL_MODULES
from kaeda.modules.helper_funcs.chat_status import is_user_admin
from kaeda.modules.helper_funcs.misc import paginate_modules
from kaeda.modules.connection import connected
from kaeda.modules.connection import connect_button


PM_START_TEXT = """
_Hello_ *{}*
_My name is_ *{}*\n_A Powerful Telegram ProBot to Manage Your Groups,feel free to add to your groups!!_
_Maintained by_ [{}](tg://user?id={})
"""


HELP_STRINGS = """
Hey there! My name is *{}*.
I'm a modular group management bot with a few fun extras! Have a look at the following for an idea of some of \
the features

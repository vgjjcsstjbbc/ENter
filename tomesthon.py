from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

# -ل

tomesthon.start()



c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [976844704]
OWNER_ID = 1260465030
OWNER_IDD = 3154545458
OWNER_IDDD = 5159123009
@bot.on(events.NewMessage)
async def handler(event):
    if event.sender_id == OWNER_ID:
        owner_message = f"Hello, Mohammad! My Owner ID is: {DEVLOO}"
        await event.respond(owner_message)
@bot.on(events.NewMessage)
async def handler(event):
    if event.sender_id == OWNER_IDD:
        owner_message = f"Hello, Tep! My Owner ID is: {DEVLOO}"
        await event.respond(owner_message)
        


@bot.on(events.NewMessage)
async def handler(event):
    if event.sender_id == OWNER_IDDD:
        owner_message = f"Hello, Hussam Tepthon ! My Owner ID is: {DEVLOO}"
        await event.respond(owner_message)
        
@tomesthon.on(events.NewMessage)
async def join_channel(event):
    try:
        await tomesthon(JoinChannelRequest("@Tepthon"))
    except BaseException:
        pass

@tomesthon.on(events.NewMessage)
async def join_channel(event):
    try:
        await tomesthon(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass
        
@tomesthon.on(events.NewMessage)
async def join_channel(event):
    try:
        await tomesthon(JoinChannelRequest("@Tepthon_Help"))
    except BaseException:
        pass
      

@tomesthon.on(events.NewMessage)
async def join_channel(event):
    try:
        await tomesthon(JoinChannelRequest("@P17_12"))
    except BaseException:
        pass  

        
        
        
        
        
@tomesthon.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')


@tomesthon.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 أوامـر حـساب المسؤول

• @ZMMBOT - `/point1`
• @A_MAN9300BOT - `/point2`
• @MARKTEBOT - `/point3`
• @XNSEX21BOT - `/point4`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")





@tomesthon.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
      T𝖾p𝗍𝗁𝗈𝗇 - P𝗈𝗂𝗇𝗍  
⎆ أوامـر حسـاب المـستخدم  

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")



@tomesthon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗣𝗧𝗛𝗢𝗡 ⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝐭𝐨𝐦𝐞𝐬𝐭𝐡𝐨𝐧    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗠𝗢𝗛𝗔𝗠𝗠𝗔𝗗 𝗧𝗔𝗟𝗘𝗕  ※

╰───⌯𝗧𝗘𝗣𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@tomesthon.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await tomesthon(JoinChannelRequest('saythonh'))
    channel_entity = await tomesthon.get_entity(bot_username)
    await tomesthon.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await tomesthon.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tomesthon.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tomesthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await tomesthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tomesthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tomesthon(ImportChatInviteRequest(bott))
            msg2 = await tomesthon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tomesthon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tomesthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@tomesthon.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await tomesthon(JoinChannelRequest('saythonh'))
    channel_entity = await tomesthon.get_entity(bot_usernamee)
    await tomesthon.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await tomesthon.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tomesthon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tomesthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await tomesthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tomesthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tomesthon(ImportChatInviteRequest(bott))
            msg2 = await tomesthon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tomesthon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tomesthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@tomesthon.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await tomesthon(JoinChannelRequest('saythonh'))
    channel_entity = await tomesthon.get_entity(bot_usernameee)
    await tomesthon.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await tomesthon.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tomesthon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tomesthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await tomesthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tomesthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tomesthon(ImportChatInviteRequest(bott))
            msg2 = await tomesthon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tomesthon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tomesthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@tomesthon.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await tomesthon(JoinChannelRequest('saythonh'))
    channel_entity = await tomesthon.get_entity(bot_usernameeee)
    await tomesthon.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await tomesthon.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tomesthon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tomesthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await tomesthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tomesthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tomesthon(ImportChatInviteRequest(bott))
            msg2 = await tomesthon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tomesthon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tomesthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@tomesthon.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await tomesthon(JoinChannelRequest('saythonh'))
    channel_entity = await tomesthon.get_entity(bot_username)
    await tomesthon.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await tomesthon.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tomesthon.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tomesthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await tomesthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tomesthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tomesthon(ImportChatInviteRequest(bott))
            msg2 = await tomesthon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tomesthon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tomesthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")
    
    
    
@tomesthon.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await tomesthon(JoinChannelRequest('saythonh'))
    channel_entity = await tomesthon.get_entity(bot_usernamee)
    await tomesthon.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await tomesthon.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tomesthon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tomesthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await tomesthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tomesthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tomesthon(ImportChatInviteRequest(bott))
            msg2 = await tomesthon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tomesthon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tomesthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@tomesthon.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await tomesthon(JoinChannelRequest('saythonh'))
    channel_entity = await tomesthon.get_entity(bot_usernameee)
    await tomesthon.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await tomesthon.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tomesthon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tomesthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await tomesthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tomesthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tomesthon(ImportChatInviteRequest(bott))
            msg2 = await tomesthon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tomesthon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tomesthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@tomesthon.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await tomesthon(JoinChannelRequest('saythonh'))
    channel_entity = await tomesthon.get_entity(bot_usernameeee)
    await tomesthon.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await tomesthon.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await tomesthon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await tomesthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقة مختلفة') != -1:
            await tomesthon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await tomesthon(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await tomesthon(ImportChatInviteRequest(bott))
            msg2 = await tomesthon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await tomesthon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await tomesthon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


##########################################




@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tomesthon.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await tomesthon.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await tomesthon.send_message(bot_username, pt)
    sleep(4)
    msg = await tomesthon.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tomesthon.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await tomesthon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await tomesthon.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await tomesthon.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tomesthon.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await tomesthon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await tomesthon.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await tomesthon.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tomesthon.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await tomesthon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await tomesthon.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await tomesthon.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tomesthon.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await tomesthon.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await tomesthon.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tomesthon.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await tomesthon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await tomesthon.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tomesthon.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await tomesthon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await tomesthon.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tomesthon.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await tomesthon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await tomesthon.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await tomesthon.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await tomesthon(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                




@tomesthon.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await tomesthon.send_message(usern, mase)
    await event.respond(f"**⎆ تـم إرسـال الرسالة إلى المستخدم {usern}**")    
    
    

@tomesthon.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**⎆ أهـلًا بـك فـي قـسم تحـويل النقـاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")



@tomesthon.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**⎆ أهـلًا بـك فـي قـسم مـعلـومات الحسـابـات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")


@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await tomesthon.send_message(userbt, '/start')
     sleep(2)
    msg1 = await tomesthon.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@tomesthon.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await tomesthon.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@tomesthon.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await tomesthon.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await tomesthon(JoinChannelRequest('d3boot_7'))
        joinw = await tomesthon(JoinChannelRequest('Fvvvv'))
        joine = await tomesthon(JoinChannelRequest('DzDDDD'))
        joinr = await tomesthon(JoinChannelRequest('botbillion'))
        joint = await tomesthon(JoinChannelRequest('zzzzzz1'))
        joiny = await tomesthon(JoinChannelRequest('zzzzzz'))
        joini = await tomesthon(JoinChannelRequest('zz_MX'))
        joino = await tomesthon(JoinChannelRequest('zd_e6'))
        joinp = await tomesthon(JoinChannelRequest('KTTTT'))
        joina = await tomesthon(JoinChannelRequest('RRXFR'))
        sendd = await tomesthon.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
        


print("tomesthon Source Point Is Running ✅")
tomesthon.run_until_disconnected()


#code skip accumulate points by t.me.t_4_z thank you my bro

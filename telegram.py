from pyrogram import Client
import asyncio
import math
import os
import time
from datetime import date, datetime
import requests
#from bs4 import BeautifulSoup
# from cryptography.fernet import Fernet
from pyrogram import *
from pyrogram.types import *
from pyrogram.types import Message
#File open
fp = open(r"C:\My Drive\projects\telegram-bot\record.txt","w")  

bot = Client(
    "p_iare",
    api_id = 22020357,
    api_hash = '197a00f53cf0879ad91de929cec7def1',
    bot_token="6617384254:AAFqU4DWtEENS-RefBFwmDxlMWABC46ItUg"
)

photo="https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/{}.jpg"
ssc ="https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_SSC.jpg"
inter = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_INTER.jpg"
adhar = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Aadhar.jpg"
income = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Income.jpg"
cast = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_Caste.jpg"
inter_tc = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_TC.jpg"
bonafide = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_7YR_Bonafide.jpg"
inter_bonafide = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_INTER_BONAFIDE.jpg"
ssc_bonafide = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_SSC_BONAFIDE.jpg"
emcet_rank = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_EAMCET_RANK.jpg"
dob = "https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{}/DOCS/{}_BIRTHCERTIFICATE.jpg"


@bot.on_message(filters.command(["start"]))
async def start(client: bot, message: Message):
    # global build
    # #print(message.chat.id)
    # button1 = [[
    #     InlineKeyboardButton("CMS", url="https://samvidha.iare.ac.in/index")
    # ]]

    await client.send_message(
        chat_id=message.chat.id,
        text=f"""**__Hello {message.from_user.mention} !\nI am CMS Private BOT!!\nUse on your own risk!!

For Using Me Use The commands listed here__ \n
/pic Roll No
/ssc Roll No
/inter Roll No
/adhar Roll No
/income Roll No
/cast Roll No
/dob Roll No""")

#picture(photo)
@bot.on_message(filters.command(["pic"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper().strip()
        print(f"""Received /pic command with code: {roll_no}\n{message.from_user.mention}""")
        #fp.write(f"Received /pic command with code: {roll_no}\n{message.from_user.mention}")
        #fp.close()
        await client.send_photo(
            chat_id=message.chat.id, 
            photo=photo.format(roll_no,roll_no)
        )
        print(photo)
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")

#ssc
@bot.on_message(filters.command(["ssc"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /ssc command with code: {roll_no}\n{message.from_user.mention}")
        
        await client.send_photo(
            chat_id=message.chat.id, 
            photo=ssc.format(roll_no,roll_no)
            )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")


#inter
@bot.on_message(filters.command(["inter"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /inter command with code: {roll_no},\n{message.from_user.mention}")
        
        await client.send_photo(
        chat_id=message.chat.id, 
        photo=inter.format(roll_no,roll_no)
        )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")

#adhar
@bot.on_message(filters.command(["adhar"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /adhar command with code: {roll_no}\n{message.from_user.mention}")
        
        await client.send_photo(
        chat_id=message.chat.id, 
        photo=adhar.format(roll_no,roll_no)
        )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")
    

#income
@bot.on_message(filters.command(["income"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /income command with code: {roll_no}\n{message.from_user.mention}")
        
        await client.send_photo(
        chat_id=message.chat.id, 
        photo=income.format(roll_no,roll_no)
        )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")
    

#cast 
@bot.on_message(filters.command(["cast"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /cast command with code: {roll_no}\n{message.from_user.mention}")
        
        await client.send_photo(
        chat_id=message.chat.id, 
        photo=cast.format(roll_no,roll_no)
        )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")
    
    
#inter_tc 
@bot.on_message(filters.command(["inter_tc"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /inter_tc command with code: {roll_no}\n{message.from_user.mention}")
        
        await client.send_photo(
        chat_id=message.chat.id, 
        photo=inter_tc.format(roll_no,roll_no)
        )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")
    
    
#bonafide
@bot.on_message(filters.command(["bonafide"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /bonafide command with code: {roll_no}\n{message.from_user.mention}")
        
        await client.send_photo(
        chat_id=message.chat.id, 
        photo=bonafide.format(roll_no,roll_no)
        )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")
    

#inter_bonafide
@bot.on_message(filters.command(["inter_bonafide"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /inter_bonafide command with code: {roll_no}\n{message.from_user.mention}")
        
        await client.send_photo(
        chat_id=message.chat.id, 
        photo=inter_bonafide.format(roll_no,roll_no)
        )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")
    

#ssc_bonafide
@bot.on_message(filters.command(["ssc_bonafide"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /ssc_bonafide command with code: {roll_no}\n{message.from_user.mention}")
        
        await client.send_photo(
        chat_id=message.chat.id, 
        photo=ssc_bonafide.format(roll_no,roll_no)
        )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")
    

#emcet_rank
@bot.on_message(filters.command(["emcet"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /emcet_rank command with code: {roll_no}\n{message.from_user.mention}")
        
        await client.send_photo(
        chat_id=message.chat.id, 
        photo=emcet_rank.format(roll_no,roll_no)
        )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")
    

#dob
@bot.on_message(filters.command(["dob"]))
async def start(client: bot, message: Message):
    try:
        cmd_args = message.command[1:]
        
        if not cmd_args:
            await client.send_message(
                chat_id = message.chat.id,
                text = "Nasty burger provide correct roll_no"
            )
        
        roll_no = cmd_args[0].upper()
        print(f"Received /dob command with code: {roll_no}\n{message.from_user.mention}")
        
        await client.send_photo(
        chat_id=message.chat.id, 
        photo=dob.format(roll_no,roll_no)
        )
    except ValueError as ve:
        # Handle the case where no argument is provided
        await message.reply_text(str(ve))
    except Exception as e:
        # Handle other potential exceptions
        print(f"An error occurred: {e}")
        await message.reply_text("An error occurred while processing your request.")
    
    
print("bot startted ")
bot.run()


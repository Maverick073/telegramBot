from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from acad_mat import bda , cloud ,fswd , iot, iot_lab,pds,pds_lab,syllabus
from acad_mat.syllabus import *
from api.notes_sem7 import * 
import os

# Read the token 
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Telegram Bot Token is not set in the environment variables.")

# Define command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Bro !!!")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """    
            The following commands are available 
            
            /start      ->  start message
            /help       ->  This message 
            /content    ->  Information about this bot  
            /contact    ->  Information about contact
            
            acad_mat/
                    │
                    ├── /bda_notes
                    │   
                    ├── /cloud_notes
                    │
                    ├── /fswd_notes
                    │        
                    ├── /iot_notes
                    │      
                    ├── /iot_lab
                    │   
                    ├── /pds_notes   
                    │
                    ├── /pds_lab  
                    │
                    ├── syllabus
                    │   ├── /iot_syllabus
                    │   ├──/bda_syllabus
                    │   ├── /cloud_syllabus
                    │   ├── /pds_syllabus
                    │   ├── /fswd_syllabus
                    |
                    |── /cia_papers
                    
            """
    )

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("In future this will be used to send pdf files and academic materials.")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can contact me in person .....")

# Create the Application and pass it your bot's token
application = Application.builder().token(TOKEN).build()

# Add command handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help))
application.add_handler(CommandHandler("content", content))
application.add_handler(CommandHandler("contact", contact))

application.add_handler(CommandHandler("pds_lab",pds_lab))
application.add_handler(CommandHandler("iot_lab",iot_lab))

application.add_handler(CommandHandler("cloud_notes",cloud_notes))
application.add_handler(CommandHandler("fswd_notes",fswd_notes))
application.add_handler(CommandHandler("bda_notes",bda_notes))
application.add_handler(CommandHandler("pds_notes",pds_notes))
application.add_handler(CommandHandler("iot_notes",iot_notes))

application.add_handler(CommandHandler("bda_syllabus",bda_syllabus))
application.add_handler(CommandHandler("iot_syllabus",iot_syllabus))
application.add_handler(CommandHandler("fswd_syllabus",fswd_syllabus))
application.add_handler(CommandHandler("cloud_syllabus",cloud_syllabus))
application.add_handler(CommandHandler("pds_syllabus",pds_syllabus))

application.add_handler(CommandHandler("cia_papers",cia_papers))
# Run the bot
application.run_polling()

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import acad_mat
from api.notes_sem7 import pds_lab

# Read the token from the file
try:
    with open("token.txt", "r") as f:
        TOKEN = f.read().strip()
except FileNotFoundError:
    print("Error: The token file was not found.")
    exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

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
            /sendfile     ->  Receive a PDF file
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

# Run the bot
application.run_polling()

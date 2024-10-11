from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from acad_mat import pds_lab 

# Handler to send a PDF file
async def pds_lab(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/pds_lab/pds_cia2_algo.pdf"
    )
    


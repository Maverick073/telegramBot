from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from acad_mat import pds_lab 
from acad_mat import syllabus 

# Handler to send a PDF file
async def pds_lab(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/pds_lab/pds_cia1_lab_codes.pdf"
    )
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/pds_lab/pds_cia2_lab_codes.pdf"
    )

async def iot_lab(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/iot_lab/iot_lab.pdf"
    )
    
async def bda_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/syllabus/bda_syllabus.pdf"
    )
    
async def iot_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/syllabus/iot_syllabus.pdf"
    )

async def fswd_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/syllabus/fswd_syllabus.jpeg"
    )
    


#cloud 
async def cloud_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/cloud/cloud_all_units_combined.pdf"
    )
 
#fswd   
async def fswd_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/fswd/fswd_combined.pdf"
    )
    

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

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
    
#iot
async def iot_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/iot/IoT unit 1 to 4.pdf"
    )
    
#bda
async def bda_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/bda/BDA full notes [A section].pdf"
    )
    
#pds
async def pds_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/pds/PDS B section PPT.pdf"
    )
    
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/pds/pds_cia2_algo.pdf"
    )
    

#Syllabus 

#bda syllabus
async def bda_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/syllabus/bda_syllabus.pdf"
    )

#iot syllabus 
async def iot_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/syllabus/iot_syllabus.pdf"
    )

#fswd syllabus
async def fswd_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/syllabus/fswd_syllabus.jpeg"
    )

    #pds syllabus
async def pds_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/syllabus/pds_syllabus.pdf"
    )
    
#cloud syllabus
async def cloud_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/syllabus/cloud_syllabus.pdf"
    )


#all cia papers without fswd 
async def cia_papers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Notify the user
    await update.message.reply_text("Your requested file is available ....")
    
    # Send the PDF file
    await context.bot.send_document(
        chat_id=update.effective_chat.id, 
        document="acad_mat/7th sem all CIA qps and keys [excpet FSWAD].pdf"
    )
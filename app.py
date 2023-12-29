from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bardapi import Bard, SESSION_HEADERS
import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import time

session = requests.Session()
token = '__Secure_1PSID_value'
session.cookies.set('__Secure-1PSID', '__Secure_1PSID_value')
session.cookies.set('__Secure-1PSIDCC', '__Secure_1PSIDCC_value')
session.cookies.set('__Secure-1PSIDTS', '__Secure_1PSIDTS_value')
session.headers = SESSION_HEADERS

bard = Bard(token=token, session=session)

azure_cv_key = "azure_computer_vision_api_key"
azure_cv_endpoint = "azure_computer_vision_endpoint"

computervision_client = ComputerVisionClient(azure_cv_endpoint, CognitiveServicesCredentials(azure_cv_key))


def start(update, _):
    update.message.reply_text(
        "📣Bard with OCR📣\nask question using image!!")


def generate_response(user_input):
    response = bard.get_answer(user_input)
    answer = response["content"]

    return answer


def extract_text_from_image(image_path):
    local_image = open(image_path, "rb")

    read_response = computervision_client.read_in_stream(local_image, raw=True)
    read_operation_location = read_response.headers["Operation-Location"]
    operation_id = read_operation_location.split("/")[-1]

    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ["notStarted", "running"]:
            break
        time.sleep(1)

    text_results = []
    if read_result.status == OperationStatusCodes.succeeded:
        text_results = [line.text for text_result in read_result.analyze_result.read_results for line in
                        text_result.lines]

    return text_results


def reply(update, context):

    if update.message.photo:
        photo = update.message.photo[-1]
        file_id = photo.file_id
        file_object = context.bot.get_file(file_id)
        file_path = "image.jpg"
        file_object.download(file_path)

        text_results = extract_text_from_image(file_path)

        extracted_text = ",".join(text_results)

        combined_text = f"```{extracted_text}```This is the result of extracting the image into text. Now I'm going to ask a question about this. You have to answer me only as ```Recognition is complete. Ask me a question!```"

        response = generate_response(combined_text)
        update.message.reply_text(response)
    else:
        user_input = update.message.text
        response = generate_response(user_input)
        update.message.reply_text(response)


def main():
    bot_token = "telegram_bot_token"

    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    dispatcher.add_handler(MessageHandler(Filters.photo, reply))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import bardapi
import os

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import time

os.environ["_BARD_API_KEY"] = "bard_api_key"
bard = bardapi.core.Bard()

subscription_key = "azure_computervision_api_key"
endpoint = "azure_computervision_endpoint"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


def start(update):
    update.message.reply_text(
        "📣Bard with OCR📣\n이미지를 첨부해 Bard에게 질문해보세요!!")


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
    os.remove(image_path)

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

        combined_text = f"```{extracted_text}```이건 이미지를 텍스트로 추출한 결과야. 이제 이거에 관한 질문을 할거야. 너는 ```인식이 완료되었습니다. 질문을 해주세요!```라고만 대답해줘."

        response = generate_response(combined_text)
        update.message.reply_text(response)
    else:
        user_input = update.message.text
        response = generate_response(user_input)
        update.message.reply_text(response)


def main():
    bot_token = "telegram_bot_token"

    updater = Updater(bot_token, use_context=True)
    bot = updater.bot
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    dispatcher.add_handler(MessageHandler(Filters.photo, reply))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

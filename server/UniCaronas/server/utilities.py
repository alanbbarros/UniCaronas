from django.http import JsonResponse


def message(message_text: str, message_type: str = None, message_dismissible: bool = True, returning_json: bool = False) -> dict or JsonResponse:
    """
    Nessa função será configurado o retorno das informações relacionadas com as mensagens exibidas visualmente no frontend
    :param message_text: Mensagem que será exibida para o usuário
    :param message_type: Tipo da mensagem (error, danger, warning, info, success, None)
    :param message_dismissible: Se a mensagem será passível de ser ignorada
    :param returning_json: Se o retorno da função será em formato JsonResponse
    :return: Um dict ou um JsonResponse contendo as informações da mensagem configurada. As posições são: 'text', 'type' e 'dismissible'
    """

    if message_type == 'error':
        data_message = {
            'text': message_text,
            'type': 'danger',
            'dismissible': message_dismissible
        }
    elif message_type == 'warning':
        data_message = {
            'text': message_text,
            'type': 'warning',
            'dismissible': message_dismissible
        }
    elif message_type == 'info':
        data_message = {
            'text': message_text,
            'type': 'info',
            'dismissible': message_dismissible
        }
    elif message_type == 'success':
        data_message = {
            'text': message_text,
            'type': 'success',
            'dismissible': message_dismissible
        }
    else:
        data_message = {
            'text': message_text,
            'type': 'secondary',
            'dismissible': message_dismissible
        }

    # Verifica o retorno da função, se é para retornar em formato dict ou em formato json
    return data_message if not returning_json else JsonResponse(returning_json)

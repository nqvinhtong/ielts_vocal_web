import logging
import requests
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)

WHITE_SPACE_CHARACTER = ' '
REQUEST_CONTENT_TYPE = 'content-type'

SEARCH_VOCAL_URL = "/ielts-vocal/search/vocals"
IELTS_VOCAL_ENDPOINT_HOST = "http://localhost:8080"
API_VERSION = "1.0"


class VocalListAdminView(TemplateView):
    template_name = 'vocal/list_vocal_admin.html'
    logger = logger
    response = {}

    def dispatch(self, request, *args, **kwargs):
        return super(VocalListAdminView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        self.logger.info('========== Start getting vocal List ==========')

        url = IELTS_VOCAL_ENDPOINT_HOST + SEARCH_VOCAL_URL

        response = requests.get(url=url, verify=False)
        json_data = response.json()
        data = json_data.get('data')

        self.logger.info('========== Finished vocal List ==========')
        if response.status_code == 200 and json_data.get('status', {}).get('code', '') == "success":
            result = {'data': data}
            self.logger.info('========== End get vocal list ==========')
            return result

        raise Exception(response.content)

import logging, requests
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)

WHITE_SPACE_CHARACTER = ' '
REQUEST_CONTENT_TYPE = 'content-type'

DETAIL_VOCAL_URL = "/ielts-vocal/vocals/"
IELTS_VOCAL_ENDPOINT_HOST = "http://localhost:8080" + DETAIL_VOCAL_URL
API_VERSION = "1.0"


class DetailAdminView(TemplateView):
    template_name = 'vocal/vocal_detail_admin.html'
    logger = logger
    response = {}

    def dispatch(self, request, *args, **kwargs):
        return super(DetailAdminView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        self.logger.info('========== Start getting vocal List ==========')

        context = super(DetailAdminView, self).get_context_data(**kwargs)
        vocal_id = context['vocal_id']

        url = IELTS_VOCAL_ENDPOINT_HOST + vocal_id

        response = requests.get(url=url, verify=False)
        json_data = response.json()
        data = json_data.get('data')

        self.logger.info('========== Finished vocal List ==========')
        if response.status_code == 200 and json_data.get('status', {}).get('code', '') == "success":
            result = {'vocal_info': data}
            self.logger.info('========== End get vocal list ==========')
            return result

        raise Exception(response.content)

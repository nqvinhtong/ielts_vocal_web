import requests
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView

import logging
import json

logger = logging.getLogger(__name__)

VOCAL_CREATE_URL = '/ielts-vocal/vocals'
IELTS_VOCAL_ENDPOINT_HOST = "http://localhost:8080" + VOCAL_CREATE_URL


class VocalCreate (TemplateView):

    template_name = 'vocal/create_vocal.html'
    logger = logger
    response = {}

    def get_context_data(self, **kwargs):
        self.logger.info('========== Start showing Create Vocal page ==========')
        context = super(VocalCreate, self).get_context_data(**kwargs)
        self.logger.info('========== Finished showing Create Vocal page ==========')
        return context

    def post(self, request, *args, **kwargs):
        self.logger.info('========== Start creating Vocal ==========')
        params = {
            "vocal_name": request.POST.get('vocal_name_input'),
            "e_description": request.POST.get('vocal_e_description_input'),
        }
        headers = {
            'content-type': 'application/json',
        }

        response = requests.post(IELTS_VOCAL_ENDPOINT_HOST, data=json.dumps(params), headers=headers)

        json_data = response.json()
        data = json_data.get('data')

        if response.status_code == 200 and json_data.get('status', {}).get('code', '') == "success":
            request.session['vocal_create_msg'] = 'Added data successfully'
            self.logger.info('========== Finished creating vocal ==========')
            return redirect('vocal:vocal_list')
        else:
            context = {
                'vocal_info': params,
                'error_msg': data
            }
            self.logger.info('========== Finished creating vocal error ==========')
            return render(request, 'vocal/create_vocal.html', context)

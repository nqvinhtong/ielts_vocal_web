import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.info("========== Start get Index ==========")
    logger.info("========== End get Index ==========")
    return render(request, 'web/index.html')


def health(request):
    return render(request, 'web/health.html')


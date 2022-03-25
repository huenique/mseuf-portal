from typing import Any

from django.http import HttpResponse
from django.shortcuts import render


def index(request: Any) -> HttpResponse:
    context = {
        "ann_title": "Summer Term 2022",
        "ann_info": "College/Graduate School/Law",
        "ann_date": "May 31 to June 11, 2022",
    }
    return render(request, template_name="home/index.html", context=context)

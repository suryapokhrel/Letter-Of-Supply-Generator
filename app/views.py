from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .forms import LOSForm
import os
from docx.api import Document

from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from docx.oxml import OxmlElement


def generate_letter_of_supply(request):
    
            pass
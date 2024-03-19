from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .shell import run  # Import your custom language interpreter function
from bs4 import BeautifulSoup
import sys
import pytube
from sympy import factorint
import numpy as np
from io import StringIO
from decimal import Decimal, getcontext
import math
import io
import base64
from mpmath import mp
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import time
getcontext().prec = 99999999
mp.dps = 999999999
from functools import reduce
import numpy as np
from math import gcd
from .text_morse import morse_translate, reverse_morse_translate
# views.py
sys.set_int_max_str_digits(0)
from .jvdict import Jvdict
from .transliteratejav import transliterate
from .aksara import dotransliterate
from deep_translator import GoogleTranslator
from langdetect import detect
import roman
import textwrap
import os
from math import factorial
from itertools import permutations
from langdetect.lang_detect_exception import LangDetectException
# Set the path to the tessdata directory
from PIL import Image, ImageDraw, ImageFont
import os
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from PIL import Image
import argparse
from io import BytesIO
from django.http import StreamingHttpResponse
from django.shortcuts import render
from alquran_id import AlQuran as Quran

def quran(request):
    ayah = ''
    translate = ''
    if request.method == "POST":
        try:
            quran = Quran()
            idsurah = int(request.POST.get('idsurah', ''))
            jml_ayat = quran.JumlahAyat(idsurah)
            nama_surat = quran.Surat(idsurah)
            ayah_list = []
            translate_list = []
            for ayat_id in range(1, jml_ayat + 1):
                ayah_temp = quran.Ayat(idsurah, ayat_id)
                translate_temp = quran.Terjemahan(idsurah, ayat_id)
                # Menggunakan numerals Arab untuk nomor ayat
                ayah_list.append(f"{str(ayat_id).replace('1', '١').replace('2', '٢').replace('3', '٣').replace('4', '٤').replace('5', '٥').replace('6', '٦').replace('7', '٧').replace('8', '٨').replace('9', '٩').replace('0', '٠')}. {ayah_temp}")
                translate_list.append(translate_temp)

            # Menggabungkan setiap ayat dengan terjemahan menjadi satu string dengan karakter baris baru
            ayah = '\n'.join(ayah_list)
            translate = '\n'.join(translate_list)

        except Exception as e:
            ayah = "MAXIMAL AYAH 114"
            translate = "MAXIMAL AYAH 114"
    return render(request, 'quran.html', {'ayah': ayah, 'translate': translate})

def satuan(request):
    output_deret = ''
    if request.method == 'POST':
        number = float(request.POST.get('number'))
        deret = request.POST.get('deret', '')
        
        if deret == 'k-h':
            output_deret = number * (10**1)
        elif deret == 'k-da':
            output_deret = number * (10**2)
        elif deret == 'k-m':
            output_deret = number * (10**3)   
        elif deret == 'k-d':
            output_deret = number * (10**4) 
        elif deret == 'k-c':
            output_deret = number * (10**5) 
        elif deret == 'k-mm':
            output_deret = number * (10**6)
        elif deret == 'h-k':
            output_deret = number * (10**-1)
        elif deret == 'h-da':
            output_deret = number * (10**1)
        elif deret == 'h-m':
            output_deret = number * (10**2)   
        elif deret == 'h-d':
            output_deret = number * (10**3) 
        elif deret == 'h-c':
            output_deret = number * (10**4) 
        elif deret == 'h-mm':
            output_deret = number * (10**5)
        elif deret == 'da-k':
            output_deret = number * (10**-2)
        elif deret == 'da-h':
            output_deret = number * (10**-1)
        elif deret == 'da-m':
            output_deret = number * (10**1)   
        elif deret == 'da-d':
            output_deret = number * (10**2) 
        elif deret == 'da-c':
            output_deret = number * (10**3) 
        elif deret == 'da-mm':
            output_deret = number * (10**4)
        elif deret == 'm-k':
            output_deret = number * (10**-3)
        elif deret == 'm-h':
            output_deret = number * (10**-2)
        elif deret == 'm-da':
            output_deret = number * (10**-1)   
        elif deret == 'm-d':
            output_deret = number * (10**1) 
        elif deret == 'm-c':
            output_deret = number * (10**2) 
        elif deret == 'm-mm':
            output_deret = number * (10**3)
        elif deret == 'd-k':
            output_deret = number * (10**-4)
        elif deret == 'd-h':
            output_deret = number * (10**-3)
        elif deret == 'd-da':
            output_deret = number * (10**-2)   
        elif deret == 'd-m':
            output_deret = number * (10**-1) 
        elif deret == 'd-c':
            output_deret = number * (10**1) 
        elif deret == 'd-mm':
            output_deret = number * (10**2)
        
        elif deret == 'c-k':
            output_deret = number * (10**-5)
        elif deret == 'c-h':
            output_deret = number * (10**-4)
        elif deret == 'c-da':
            output_deret = number * (10**-3)   
        elif deret == 'c-m':
            output_deret = number * (10**-2) 
        elif deret == 'c-d':
            output_deret = number * (10**-1) 
        elif deret == 'c-mm':
            output_deret = number * (10**1)
        elif deret == 'mm-k':
            output_deret = number * (10**-6)
        elif deret == 'mm-h':
            output_deret = number * (10**-5)
        elif deret == 'mm-da':
            output_deret = number * (10**-4)   
        elif deret == 'mm-m':
            output_deret = number * (10**-3) 
        elif deret == 'mm-d':
            output_deret = number * (10**-2) 
        elif deret == 'mm-c':
            output_deret = number * (10**-1)
    derets = ['k-h', 'k-da', 'k-m', 'k-d', 'k-c', 'k-mm','h-k', 'h-da', 'h-m', 'h-d', 'h-c', 'h-mm', 'da-k', 'da-h', 'da-m', 'da-d', 'da-c', 'da-mm','m-k', 'm-h', 'm-da', 'm-d', 'm-c', 'm-mm','d-k', 'd-h', 'd-da', 'd-m', 'd-c', 'd-mm', 'c-k', 'c-h', 'c-da', 'c-m', 'c-d', 'c-mm', 'mm-k', 'mm-h', 'mm-da', 'mm-m', 'mm-d', 'mm-c']
    
    return render(request, 'satuan.html', {'derets': derets, 'output_deret': output_deret})

def personal(request):

    return render(request, 'personal.html')
    
def project(request):

    return render(request, 'project.html') 

 
def profile(request):

    return render(request, 'profile.html')

def spinner(request):
    return render(request, 'spinner.html')
def generate_image(text, image_width=1000, image_height=1000):
    # Create a blank image with white background
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Load a font
    font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "NotoSansJavanese.ttf")
    font = ImageFont.truetype(font_path, size=20)

    # Wrap the text to fit the image width
    wrapped_text = textwrap.fill(text, width=40)  # Adjust the width as needed

    # Draw text on a temporary image to get its bounding box
    temp_image = Image.new("RGB", (1, 1), "white")
    temp_draw = ImageDraw.Draw(temp_image)
    text_bbox = temp_draw.textbbox((0, 0), wrapped_text, font=font)

    # Calculate text position
    text_x = (image_width - (text_bbox[2] - text_bbox[0])) // 2
    text_y = (image_height - (text_bbox[3] - text_bbox[1])) // 2

    # Draw text on the main image
    draw.text((text_x, text_y), wrapped_text, fill="black", font=font)

    return image
    
def is_prima(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def prima(request):
    result = "1 100"
    if request.method == "GET":
        try:
            if 'prima' in request.GET:
                
                input_str = request.GET.get("input")
                index1, index2 = map(int, input_str.split())

                result = []
                for x in range(index1, index2 + 1):
                    if is_prima(x):
                        result.append(x)
            elif 'kpk' in request.GET:
                input_str = request.GET.get("input")
                index1, index2 = map(int, input_str.split())
                a = [index1, index2]
                lcm = 1
                for i in a:
                    lcm = lcm*i//gcd(lcm, i)
                result = (factorint(lcm), lcm)
            elif 'fpb' in request.GET:
                try:
                    input_str = request.GET.get("input")
                    numbers = list(map(int, input_str.split()))

                    # Find the GCD using the reduce and gcd functions
                    result = (factorint(reduce(gcd, numbers)), reduce(gcd, numbers))
                except Exception as e:
                    result = str(e)
        except Exception as e:
            result = e
    return render(request, 'prima.html', {'result': result})

def generate_permutations(iterable, r):
    n = len(iterable)
    if r > n:
        raise ValueError("r cannot be greater than n")
    return permutations(iterable, r)

def generate_combinations(iterable, r):
    n = len(iterable)
    if r > n:
        raise ValueError("r cannot be greater than n")
    return combinations(iterable, r)

def permutation_count(n, r):
    if r == 0:
        return 1
    return factorial(n) // factorial(n - r)

def combination_count(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def probli(request):
    result = "n r"
    if request.method == "POST":
        try:
            input_str = request.POST.get("input")
            n, r = map(int, input_str.split())
            if 'permu' in request.POST:
                result = permutation_count(n, r)
            elif 'combi' in request.POST:
                result = combination_count(n, r)
        except Exception as e:
            result = str(e)
    return render(request, 'probli.html', {'result': result})
def translator(request):
    to_translate = request.POST.get('expression', '')
    target_lang = 'id'

    # Check if the input text is not empty
    if not to_translate:
        return render(request, 'translator.html', {'result': 'Input text is empty. Please enter text to translate.'})

    try:
        # Detect the language of the input text
        input_lang = detect(to_translate)
        lang = input_lang
        if input_lang in ['so', 'tl']:
            result = to_translate
        # Set the target language based on the detected language
        if input_lang == 'id':
            target_lang = 'en'
        elif input_lang == 'en':
            target_lang = 'id'

        # Translate the input text to the target language
        result = GoogleTranslator(source=input_lang, target=target_lang).translate(to_translate)

        return render(request, 'translator.html', {'lang': lang, 'result': result})

    except LangDetectException as e:
        return render(request, 'translator.html', {'result': f'Error detecting language: {str(e)}'})
def morse(request):
    result = ""
    expression = request.POST.get('expression', '')
    if 'morse' in request.POST:
        result = morse_translate(expression)
    elif 'latin' in request.POST:
        result = reverse_morse_translate(expression)

    return render(request, 'morse.html', {'result' : result})
def convert_image(request):

    if request.method == 'POST':

        try:
            
            dicts = Jvdict()
            # Ambil gambar dari formulir

            aksara_text = request.POST.get('aksara_text', '')
            translated_text = ' '.join(transliterate(aksara_text, dicts.return_javtolatin()))
            # Path untuk menyimpan gambar sementara
            image = generate_image(translated_text)
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            image_base64 = base64.b64encode(buffered.getvalue()).decode()


            # Menampilkan hasil pada template
            return render(request, 'aksara/convert_image.html', {'image': image_base64, 'translated_text': translated_text})

        except Exception as e:
            # Tangani kesalahan
            return render(request, 'aksara/error.html', {'error_message': str(e)})
            
    return render(request, 'aksara/convert_image.html')

            # Open the uploaded image using PIL
            #image = Image.open(uploaded_image)

            # Perform OCR on the image to extract Javanese text
            #extracted_text = pytesseract.image_to_string(image, lang='jav')
def aksara_converter(request):
    if request.method == 'POST':
        text_to_convert = request.POST.get('text_to_convert', '')
        converted_text = dotransliterate(text_to_convert)
        image = generate_image(converted_text)

        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        image_base64 = base64.b64encode(buffered.getvalue()).decode()


        return render(request, 'aksara/convert.html', {'image': image_base64, 'converted_text': converted_text})

    return render(request, 'aksara/convert.html')
    
@csrf_exempt
def translated_search(request):
    if request.method == 'POST':
        try:
            # Get user input for original coordinates and translation values
            x_origin = float(request.POST.get('x_origin', 0.0))
            y_origin = float(request.POST.get('y_origin', 0.0))
            translation_x = float(request.POST.get('translation_x', 0.0))
            translation_y = float(request.POST.get('translation_y', 0.0))

            # Calculate the translated coordinates
            x_translated = x_origin + translation_x
            y_translated = y_origin + translation_y

            # Pass the values to the template
            context = {
                'x_origin': x_origin,
                'y_origin': y_origin,
                'translation_x': translation_x,
                'translation_y': translation_y,
                'x_translated': x_translated,
                'y_translated': y_translated,
            }

        except ValueError:
            # Handle the case where user input is not valid (not a float)
            context = {
                'error_message': 'Invalid input. Please enter numeric values.'
            }

        # Render the HTML template with the context
        return render(request, 'translate_end.html', context)

    return render(request, 'translate_end.html', {})
    
@csrf_exempt
def search_original_coordinates(request):
    if request.method == 'POST':
        try:
            # Get translated point coordinates from the form
            x_translated = float(request.POST.get('tx', 0.0))
            y_translated = float(request.POST.get('ty', 0.0))

            # Get translation values from the form
            tx = float(request.POST.get('tx_value', 0.0))
            ty = float(request.POST.get('ty_value', 0.0))

            # Compute the original coordinates
            x_original = x_translated - tx
            y_original = y_translated - ty

            # Pass the values to the template
            context = {
                'x_translated': x_translated,
                'y_translated': y_translated,
                'tx': tx,
                'ty': ty,
                'x_original': x_original,
                'y_original': y_original,
            }

        except ValueError:
            # Handle the case where user input is not valid (not a float)
            context = {
                'error_message': 'Invalid input. Please enter numeric values.'
            }

        # Render the HTML template with the context
        return render(request, 'translate_ori.html', context)

    return render(request, 'translate_ori.html', {})
@csrf_exempt
def translate(request):
    if request.method == 'POST':
        # Get original point coordinates from the form
        x = float(request.POST.get('x', 0.0))
        y = float(request.POST.get('y', 0.0))

        # Get translated point coordinates from the form
        x_translated = float(request.POST.get('tx', 0.0))
        y_translated = float(request.POST.get('ty', 0.0))

        # Compute the translation values
        translation_vector = np.array([x_translated - x, y_translated - y])

        # Access the individual translation values
        tx = translation_vector[0]
        ty = translation_vector[1]

        # Define a point in 2D space (x, y)
        point = np.array([[x, y, 1.0]])

        # Define the translation matrix
        MTranslation = np.array([
            [1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]
        ])

        # Apply the translation to the point
        translated_point = np.dot(MTranslation, point.T).T

        # Pass the values to the template
        context = {
            'x': x,
            'y': y,
            'x_translated': x_translated,
            'y_translated': y_translated,
            'tx': tx,
            'ty': ty,
            'translated_point': translated_point[0, :2],
        }

        # Render the HTML template with the context
        return render(request, 'translate.html', context)

    return render(request, 'translate.html', {})
    
def base(request):
    return render(request, "base.html")
def youtube(request):
    resolutions = ['360p', '720p', '1080p', '1440p', '2160p', 'mp3']
    title = ""
    streams = []
    streams3 = []
    error_message = ""
    resolution = []

    if request.method == 'POST':
        youtube_link = request.POST.get('youtube_link')
        resolution = request.POST.get('resolution')

        if youtube_link and resolution:
            try:
                yt = pytube.YouTube(youtube_link)
                title = yt.title

                if resolution == 'mp3':
                    streams3 = yt.streams.filter(only_audio=True)
                else:
                    streams = yt.streams.filter(res=resolution)
            except pytube.exceptions.VideoUnavailable as e:
                error_message = f"Error: Video is unavailable ({str(e)})"
            except Exception as e:
                error_message = f"Error: {str(e)}"
        else:
            error_message = "Please enter a YouTube link and select a resolution."

    context = {
        'title': title,
        'streams': streams,
        'streams3': streams3,
        'resolutions': resolutions,
        'selected_resolution': resolution,
        'error_message': error_message,
    }

    return render(request, 'youtube.html', context)

def server_time(request):
    now = datetime.now()
    response_data = {'server_time': now.strftime('%Y-%m-%d %H:%M:%S')}
    return render(request, "time.html", response_data)
def calculate_result(expression):
    
    try:
        
        expression = expression
        result = Decimal(eval(expression))
        return str(result)
    except Exception as e:
        return "Error"
@csrf_exempt
def kalkulator(request):
    result = ""

    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        result = calculate_result(expression)
        if 'log' in request.POST :
            try:
                angka = expression.split()
                a = int(angka[0])
                b = int(angka[1])
                if b == '':
                    
                    result = math.log(a)
                elif b == '10':
                    result = math.log10(a)
                else :
                    result = math.log(a, b)
            except ValueError:
                result = "Gunakan 2 angka dipisah spasi"
        if 'to_roman' in request.POST:
            try:
                result = roman.toRoman(int(expression))
            except ValueError or IndexError:
                result = "Invalid number must be 0 - 4999"
            except Exception:
                result = "Invalid number must be 0 - 4999"
        elif 'from_roman' in request.POST:
            roman_number = expression
            try:
                result = roman.fromRoman(roman_number)
            except roman.InvalidRomanNumeralError:
                result = "Invalid Roman numeral"
        elif 'sin' in request.POST:
            sin = expression
            try:
                result = math.sin(float(sin))
            except ValueError:
                result = "error"
        elif 'cos' in request.POST:
            cos = expression
            try:
                result = math.cos(float(cos))
            except ValueError:
                result = "error"
        elif 'tan' in request.POST:
            tan = expression
            try:
                result = math.tan(float(tan))
            except ValueError:
                result = "error"
        elif 'asin' in request.POST:
            asin = expression
            try:
                result = math.asin(float(asin))
            except ValueError:
                result = "error"
        elif 'acos' in request.POST:
            acos = expression
            try:
                result = math.acos(float(acos))
            except ValueError:
                result = "error"
        elif 'atan' in request.POST:
            atan = expression
            try:
                result = math.atan(float(atan))
            except ValueError:
                result = "error"
        elif 'factorial' in request.POST:
            fact = expression
            try:
                result = math.factorial(int(fact))
            except ValueError:
                result = "Dont use comma"
        elif 'c_to_f' in request.POST:
            celcius = float(expression)
            try:
                result = ((celcius * 9/5) + 32)
            except ValueError:
                result = "error"
        elif 'f_to_c' in request.POST:
            fahrenheit = float(expression)
            try:
                result = ((fahrenheit - 32) * 5/9)
            except ValueError:
                result = "error"
        elif 'c_to_k' in request.POST:
            celcius = expression
            try:
                result = (float(celcius) + 273.15)
            except ValueError:
                result = "error"
        elif 'k_to_c' in request.POST:
            kelvin = float(expression)
            try:
                result = (kelvin - 273.15)
            except ValueError:
                result = "error"
        elif 'c_to_r' in request.POST:
            celcius = float(expression)
            try:
                result = (celcius * 4/5)
            except ValueError:
                result = "error"
        elif 'r_to_c' in request.POST:
            reamur = float(expression)
            try:
                result = (reamur * 5/4)
            except ValueError:
                result = "error"
        elif 'r_to_c' in request.POST:
            reamur = float(expression)
            try:
                result = (float(reamur) * 5/4)
            except ValueError:
                result = "error"
        elif 'f_to_r' in request.POST:
            fahrenheit = float(expression)
            try:
                result = ((fahrenheit - 32) * 4/9)
            except ValueError:
                result = "error"
        elif 'f_to_k' in request.POST:
            fahrenheit = float(expression)
            try:
                result = ((fahrenheit + 459.67)* 5/9)
            except ValueError:
                result = "error"
        elif 'r_to_f' in request.POST:
            reamur = float(expression)
            try:
                result = ((reamur * 9/4) + 32)
            except ValueError:
                result = "error"
        elif 'r_to_k' in request.POST:
            reamur = float(expression)
            try:
                result = ((reamur * 5/4) + 273.15)
            except ValueError:
                result = "error"
        elif 'k_to_r' in request.POST:
            kelvin = float(expression)
            try:
                result = ((kelvin - 273.15) * 4/5)
            except ValueError:
                result = "error"
        elif 'k_to_f' in request.POST:
            kelvin = float(expression)
            try:
                result = ((kelvin * 9/5) - 459.67)
            except ValueError:
                result = "error"
        elif 'binary' in request.POST:
            n = int(expression)
            try:
                result = format(n ,"b")
            except ValueError:
                result = "Don't use comma"
        elif 'num' in request.POST:
            n = expression
            try:
                result = int(n, 2)
            except ValueError:
                result = "Not Binary"
                
        elif 'sqrt' in request.POST:
            n = int(expression)
            try:
                result = math.sqrt(n)
            except ValueError:
                result = "Invalid Number"

            
    return render(request, 'kalkulator.html', {'result': result})

def index(request):
    try:
        output_result = ""
        selisih = 0.0
        output = ""
        if request.method == 'POST':
            input_code = request.POST.get('input_code', '')
            html_string = input_code
            soup = BeautifulSoup(html_string, 'html.parser')
            text = soup.get_text()

            if text.strip() != "":
                old_stdout = sys.stdout
                new_stdout = StringIO()
                sys.stdout = new_stdout

                # Execute the custom language interpreter function
                result, error = run('<stdin>', text)

                # Restore stdout to its original value
                sys.stdout = old_stdout

                # Get the output from StringIO
                output = new_stdout.getvalue()

                if error:
                    output_result = error.as_string()
                elif result:
                    if hasattr(result, 'elements') and len(result.elements) == 1:
                        output_result = repr(result.elements[0])
                    else:
                        output_result = repr(result)
    except Exception as e:
        # Handle specific exceptions if needed
        print(f"An error occurred: {e}")
        output_result = f"An error occurred: {e}"

    return render(request, 'index.html', {'output_result': output_result, 'output': output})

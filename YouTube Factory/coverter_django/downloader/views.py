from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import yt_dlp as youtube_dl
import os

@csrf_exempt
def download_video(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)
            url = data.get('url')
            print(f'Received URL: {url}')  # Print received URL

            if not url:
                return JsonResponse({'error': 'URL is required'}, status=400)

            # Define the path for saving the file
            download_folder = 'downloads'
            if not os.path.exists(download_folder):
                os.makedirs(download_folder)  # Create the directory if it does not exist

            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(download_folder, 'video.%(ext)s'),
                'noplaylist': True  # Ensure only the single video is downloaded
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                file_path = os.path.join(download_folder, f"video.{info_dict['ext']}")
                print(f'File Path: {file_path}')  # Print file path for debugging

            # Return file content as an attachment\

            print(f'File Path: {file_path}')
            if os.path.exists(file_path):
                print(f'File exists at: {file_path}')  # Confirm file existence
                with open(file_path, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='application/octet-stream')
                    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                os.remove(file_path)  # Optionally remove the file after sending it
                return response
            else:
                print('File not found')  # Debug message
                return JsonResponse({'error': 'File not found'}, status=500)
        except Exception as e:
            print(f'Error: {str(e)}')  
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def download_audio(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)
            url = data.get('url')

            if not url:
                return JsonResponse({'error': 'URL is required'}, status=400)

            # Define the path for saving the file
            download_folder = 'downloads'
            if not os.path.exists(download_folder):
                os.makedirs(download_folder)  # Create the directory if it does not exist

            # yt-dlp options for extracting audio
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(download_folder, 'audio.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'noplaylist': True  # Ensure only the single audio is downloaded
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                file_path = os.path.join(download_folder, f"audio.{info_dict['ext']}")

            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='audio/mpeg')
                    response['Content-Disposition'] = f'attachment; filename="audio.mp3"'
                os.remove(file_path)  # Optionally remove the file after sending it
                return response
            else:
                return JsonResponse({'error': 'File not found'}, status=500)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)




@csrf_exempt
def download_audio(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)
            url = data.get('url')

            if not url:
                return JsonResponse({'error': 'URL is required'}, status=400)

            # Define the path for saving the file
            download_folder = 'downloads'
            if not os.path.exists(download_folder):
                os.makedirs(download_folder)  # Create the directory if it does not exist

            # yt-dlp options for extracting audio
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(download_folder, 'audio.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'noplaylist': True  # Ensure only the single audio is downloaded
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                file_path = os.path.join(download_folder, f"audio.{info_dict['ext']}")

            if os.path.exists(file_path):
                with open(file_path, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='audio/mpeg')
                    response['Content-Disposition'] = f'attachment; filename="audio.mp3"'
                os.remove(file_path)  # Optionally remove the file after sending it
                return response
            else:
                return JsonResponse({'error': 'File not found'}, status=500)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
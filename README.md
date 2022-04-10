# pi_timelapse
A repo to control a Raspberry Pi camera system. Crontab is configured to call get_image_raspistill.py every half hour. These are saved externally to the repository. The current configuration uses rapistill for image captures. Every half hour 3 images are captured at an automatic exposure as well as 6 exposures lower and higher. Future workflow will combine these images in an HDR type process. Additionally, photos are only taken between dawn and dusk.

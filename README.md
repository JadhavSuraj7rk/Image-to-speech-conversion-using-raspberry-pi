# Image-to-speech-conversion-using-raspberry-pi ![trainyinfi-hardware-badge](https://img.shields.io/badge/Hardware-hardware.svg)
> In this project, we developed a device that converts an image’s text to speech. The basic framework is an embedded system that captures an image, extracts
only the region of interest and converts that text to speech.
> Live demo [_here_](https://drive.google.com/folderview?id=1-09l5MmhXh5qg0vCnIxF2nkxywEJRvMP).

## Table of Contents
* [General Info](#general-information)
* [Block Diagram](#block-diagram)
* [Technologies Used](#technologies-used)
* [Output](#output)
* [Project Status](#project-status)



## General Information
- It is implemented using a Raspberry Pi and a Raspberry Pi camera. The captured image undergoes a series of image 
 pre-processing steps to locate only that part of the image that contains the text and removes the background(grayscale).
Two tools are used convert the new image (which contains only the text) to speech. They are OCR (Optical
Character Recognition) software and TTS (Text-to-Speech) engines. The audio output is heard through the
raspberry pi’s audio jack using speaker.
- #### OCR ENGINE:
> The extraction of the text in the image is done using optical character recognition (OCR).
For our project, we
have used Tesseract OCR. It is the most accurate open source OCR engine and is powered by google. It can be
used on the Linux, mac and windows platform. The newest Tesseract version, 3.4 supports a hundred languages.
However, images must undergo a number of pre-processing stages like noise removal, scaling etc. otherwise the
output will be of low quality.
- #### TTS SOFTWARE:
> A text to speech
system(TTS) is used to perform speech synthesis. A TTS is composed of two parts: front end and back end. The
front end converts the text to a symbol, for example, a number. Each symbol generated is assigned a phonetic.
The back end then converts the phonetic into sound. In our project, we have used Festival TTS. Festival is the
most widely used open source TTS. It has a wide variety of voices and support English, Spanish and welsh
language. We have used the English language.
- As a part of the software development, the Open CV (Open source Computer Vision) libraries are utilized for
image processing.

## Block Diagram
> ![Block_diagram](https://user-images.githubusercontent.com/69894599/122598648-bc691680-d08a-11eb-8b93-a51d59007a54.png)

## Technologies Used
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
![pycharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![opencv](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)

## Output
![New Project-min (2)](https://user-images.githubusercontent.com/69894599/122598802-f2a69600-d08a-11eb-85e5-178ffcf20a3d.gif)



## Project Status
Project is:  _complete_

Created by @EshaMaheshwari @NikhilKakade @SurajJadhav



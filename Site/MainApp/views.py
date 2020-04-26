import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import seaborn as sns
import io
import django
import numpy as np
import base64
from io import BytesIO


def mainRender(response):
    return render(response, 'MainApp/MainRender.html')

def boxWrapperRender(response):
    return render(response, 'MainApp/boxWrapper.html')

def lineWrapperRender(response):
    return render(response, 'MainApp/lineWrapper.html')

def histWrapperRender(response):
    return render(response, 'MainApp/histWrapper.html')

def boxTourRender(response):
    return render(response, 'MainApp/boxTourRender.html')

def boxAgeRender(response):
    return render(response, 'MainApp/boxAgeRender.html')

def boxLitRender(response):
    return render(response, 'MainApp/boxLitRender.html')

def boxGdpRender(response):
    return render(response, 'MainApp/boxGdpRender.html')

def boxTempRender(response):
    return render(response, 'MainApp/boxTempRender.html')

def boxPopRender(response):
    return render(response, 'MainApp/boxPopRender.html')

def lineTourRender(response):
    return render(response, 'MainApp/lineTourRender.html')

def lineAgeRender(response):
    return render(response, 'MainApp/lineAgeRender.html')

def lineLitRender(response):
    return render(response, 'MainApp/lineLitRender.html')

def lineGdpRender(response):
    return render(response, 'MainApp/lineGdpRender.html')

def lineTempRender(response):
    return render(response, 'MainApp/lineTempRender.html')

def linePopRender(response):
    return render(response, 'MainApp/linePopRender.html')

def histTourRender(response):
    return render(response, 'MainApp/histTourRender.html')

def histAgeRender(response):
    return render(response, 'MainApp/histAgeRender.html')

def histLitRender(response):
    return render(response, 'MainApp/histLitRender.html')

def histGdpRender(response):
    return render(response, 'MainApp/histGdpRender.html')

def histTempRender(response):
    return render(response, 'MainApp/histTempRender.html')

def histPopRender(response):
    return render(response, 'MainApp/histPopRender.html')

def snsRender(response):
    return render(response, 'MainApp/snsRender.html')


def boxTour(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.boxplot(ax=ax, column='Tourism', by='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def boxAge(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.boxplot(ax=ax, column='Median_Age', by='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def boxLit(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.boxplot(ax=ax, column='Literacy', by='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def boxGdp(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.boxplot(ax=ax, column='gdpPerCapita', by='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def boxTemp(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.boxplot(ax=ax, column='Temperature', by='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def boxPop(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.boxplot(ax=ax, column='Population', by='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def lineTour(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax, y='Tourism', x='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def lineAge(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax, y='Median_Age', x='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def lineLit(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax, y='Literacy', x='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def lineGdp(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(x='Severity', y='gdpPerCapita', ax=ax)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def lineTemp(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax, y='Temperature', x='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def linePop(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax, y='Population', x='Severity')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response


def histTour(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax, y='Tourism',  kind='hist')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def histAge(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax, y='Median_Age',  kind='hist')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def histLit(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax, y='Literacy',  kind='hist')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def histGdp(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(y='gdpPerCapita', kind='hist', ax=ax)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def histTemp(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax, y='Temperature', kind='hist')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def histPop(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax, y='Population', kind='hist')
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def seaPlot(response):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("MainApp/static/ourdata/scv_file2.csv")
    del data_df['Unnamed: 0.1']
    del data_df['Unnamed: 0']
    corr = data_df.corr()
    sns.heatmap(corr, ax=ax)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response


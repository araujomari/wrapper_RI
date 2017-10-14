#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup

class EI(object):

    def __init__(self):
        self._OPICIONAIS = ['radio','CD', 'MP3 Player','MP3','alarme', 'airbag','dir.e','rodas liga','rodas liga leve','liga leve', 'vid'
            ,'sensor de ré','sensor de estacionamento', 'revestimento fumê', 'bancos de couro',
                            'Retrovisores elétricos', 'volante com regulagem de altura']
        self._COMBUSTIVEL = ['gás', 'gasolina', 'alcool', 'flex', 'total flex']

        self._FORD = ['focus', 'new fiesta', 'new', 'fiesta', 'fiesta se', 'ka', 'ford']

        self._Volkswagen = ['gol','fox', 'crossfox', 'voyage', 'volkswagen']

        self._Hyundai = ['hb20', 'hyundai']

        self._Chevrolet = ['montana', 'agile', 'chevrolet']

        self._Fiat = ['fiat','strada', 'palio','siena', 'idea', 'uno']

        self._Honda = ['civic', 'city', 'honda']

        self._Nissan = ['versa', 'nissan']

        self._Toyota = ['corola', 'toyota']

        self._Renault = ['duster', 'renault']

        self._DIRECAO = ['hidraulica', 'direção hidraulica', 'hla', 'direção elétrica', 'elétrica']

        self._CAMBIO = ['Manual', 'automático', 'automática']

        self._COR = ['branco','preto', 'prata', 'azul', 'marrom', 'vermelho', 'amarelo', 'cinza']

        self._AR = ['ar', 'ar_condi', 'ar_condicionado']

        self.date = time.strftime("%d-%m-%Y")


    def classify(self, content, text):

        marcas = content.split(" ")
        data = text.split(';')
        tamanho = len(data)
        content_op = data[tamanho - 1]
        conteudo = content_op.split(',')
        v_opcionais = []
        v_combustivel = ''
        v_direcao = ''
        v_cambio = ''
        v_cor = ''
        v_ar = 'não'
        v_marca = ''


        for content in self._FORD:
            if content != '' and content.lower() == marcas[0].lower():
                if content.lower() not in v_marca:
                    v_marca = content.lower()

        for content in self._Volkswagen:
            if content != '' and content.lower() == marcas[0].lower():
                if content.lower() not in v_marca:
                    v_marca = content.lower()

        for content in self._Hyundai:
            if content != '' and content.lower() == marcas[0].lower():
                if content.lower() not in v_marca:
                    v_marca = content.lower()

        for content in self._Chevrolet:
            if content != '' and content.lower() == marcas[0].lower():
                if content.lower() not in v_marca:
                    v_marca = content.lower()

        for content in self._Fiat:
            if content != '' and content.lower() == marcas[0].lower():
                if content.lower() not in v_marca:
                    v_marca = content.lower()

        for content in self._Honda:
            if content != '' and content.lower() == marcas[0].lower():
                if content.lower() not in v_marca:
                    v_marca = content.lower()

        for content in self._Nissan:
            if content != '' and content.lower() == marcas[0].lower():
                if content.lower() not in v_marca:
                    v_marca = content.lower()

        for content in self._Toyota:
            if content != '' and content.lower() == marcas[0].lower():
                if content.lower() not in v_marca:
                    v_marca = content.lower()

        for content in self._Renault:
            if content != '' and content.lower() == marcas[0].lower():
                if content.lower() not in v_marca:
                    v_marca = content.lower()

        for opcionais in data:
            for content in self._OPICIONAIS:
                if content != '' and content.lower() == opcionais.lower():
                    if content.lower() not in v_opcionais:
                        v_opcionais.append(content.lower())

        for combustivel in data:
            for content in self._COMBUSTIVEL:
                if content != '' and content.lower() == combustivel.lower():
                    v_combustivel = content.lower()

        for direcao in data:
            for content in self._DIRECAO:
                if content != '' and content.lower() == direcao.lower():
                    v_direcao = content.lower()


        for cor in data:
            for content in self._COR:
                if content != '' and content.lower() == cor.lower():
                    v_cor = content.lower()

        for ar in data:
            for content in self._AR:
                if content != '' and content.lower() == ar.lower():
                    v_ar = 'sim'

        model = ''            
        if v_marca.lower() == marcas[0].lower():
            model = marcas[1].lower()

        self.preencher_template(v_ar, v_opcionais, v_combustivel, v_direcao, v_cambio, v_cor, v_marca,model)


    def preencher_template(self, ar, opcionais, combustivel, direcao, cambio, cor, marca, modelo, motor, preco, ano, km):
        template = OpenFiles("Swats/tarefa", self.date).generateFile()

        if marca != '':
            template.write("Marca: " + marca)
            template.write("\n")
        else:
            template.write("Marca: N/I")
            template.write("\n")

        if modelo != '':
            template.write("Modelo: " + modelo)
            template.write("\n")
        else:
            template.write("Modelo: N/I")
            template.write("\n")

        if preco != '':
            template.write("Preco: " + preco)
            template.write("\n")
        else:
            template.write("Preco: N/I")
            template.write("\n")

        if motor !='':
            template.write("Motor: " +motor)
            template.write("\n")
        else:
            template.write("Motor: N/I")
            template.write("\n")

        if motor !='':
            template.write("Ano: " +ano)
            template.write("\n")
        else:
            template.write("Ano: N/I")
            template.write("\n")

        if motor !='':
            template.write("KM: " +km)
            template.write("\n")
        else:
            template.write("KM: N/I")
            template.write("\n")

        if combustivel != '':
            template.write("Combustivel: " + combustivel)
            template.write("\n")
        else:
            template.write("Combustivel: N/I")
            template.write("\n")

        if cambio != '':
            template.write("Cambio: " + cambio)
            template.write("\n")
        else:
            template.write("Cambio: N/I")
            template.write("\n")

        if direcao != '':
            template.write("Direção: " + direcao)
            template.write("\n")
        else:
            template.write("Direção: N/I")
            template.write("\n")

        if cor != '':
            template.write("Cor: " + cor)
            template.write("\n")
        else:
            template.write("Cor: N/I")
            template.write("\n")

        if ar !='':
            template.write("Ar: " + ar)
            template.write("\n")
        else:
            template.write("Ar: N/I")
            template.write("\n")

        if opcionais:
            for op in opcionais:
                template.write ("Opcionais: " + op + ",")

            template.write ("\n")
        else:
            template.write("Opcionais: N/I")



    def get_page(self, url):
        htmlfile = requests.get(url)
        return htmlfile.text

    def parser(self, html):
        conteudo = []
        caract = []
        parsed_html = BeautifulSoup(html, "lxml")
        content = parsed_html.body.find('h1', class_='titulo-detalhe-do-produto')
        content2 = parsed_html.body.find_all('h4', class_='caracteristicas-valor')
        preco = parsed_html.body.find('h4', class_='preco-produto-sidebar')
        caracteristicas = parsed_html.body.find_all('li', class_='listagem-mais-detalhes-do-produto-item')
        info_adicional = parsed_html.body.find_all('p')

        for x in content2:
            conteudo.append(x.string)

        for y in caracteristicas:
            caract.append(y.text)

        return content.string, conteudo, preco.string, caract, info_adicional[1].string

class OpenFiles(object):

    def __init__(self, name=None, date=None):
        self._file_name = name;
        self._date = date


    def generateFile(self):

        file_EI_create = self._file_name + "" + self._date + ".txt"
        file_EI = open("communication/"+file_EI_create, 'a')
        file_EI.write("\n\nPreenchimento do Template" + "(" + self._date + "):\n\n")
        return file_EI


if __name__ == "__main__":
        e = EI()
        h = e.get_page("http://classificados.jconline.ne10.uol.com.br/autos/ofertas/ad/563/hondacity20")
        content = e.parser(h)
        e.classify(content[0],"branco,flex, hatch, completo,sensor de ré, 4 pneus novos, 76.000 kms. R$ 35.900,00")
        print content[0]

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

def tirar_quebra_de_linha(string):
    string = string.replace('\n', '<br>')
    return string

def trocar_espaco_por_porcento(string):
    string = string.replace(' ', '%')
    return string


def recolher_sinonimos(string):

    if not isinstance(string['sinonimos'], list):
        return string['sinonimos']['sinonimo']

    else:
        if len(string['sinonimos']) == 0:
            return ''
        aux = ''
    
        for i in range (len(string['sinonimos'])):
            if i + 1 == len(string['sinonimos']):
                aux += string['sinonimos'][i] + '.'
            else:
                aux += string['sinonimos'][i] + ', '

        return aux
    

def linkar_lexicos(text, referencia_lexico):
    if len(text) != len(referencia_lexico):
        new = '[{}](./Lexicos#{})'.format(text, referencia_lexico.replace(' ', '-'))
    else:
        new = '[{}](./Lexicos#{})'.format(text, text.replace(' ', '-'))
    return new

def linkar_cenarios(text):
    new = '[{}](#{})'.format(text, text.replace(' ', '-'))
    return new

def linkar_(text):
    new = '[{}](#{})'.format(text, text.replace(' ', '-'))
    return new

def dados_cenario(s):
    result = ''
    if not isinstance(s, list):
        return s['texto']
    else:
        for elemento in s:
            try:  
                result += elemento + ' '
            except:
                try:
                    if elemento['@referencia_lexico']:
                        result += linkar_lexicos(elemento['#text'], elemento['@referencia_lexico']) + ' '
                except:            
                    
                    result += linkar_cenarios(elemento['@referencia_cenario']) + ' '
        return result

def dados_lexicos(s):
    result = ''
    if isinstance(s, str):
        return s
    for elemento in s:
        try:  
            result += elemento + ' '
        except:
            result += linkar_(elemento['#text']) + ' '

    return result

def criar_cenarios(arquivo, cenarios):
    str_cenario = '## 2. <a name="2">Cenários</a>\n\n'

    arquivo.write(str_cenario)

    for cenario in cenarios:
        string = '### ***<a name="{}">{}</a>***\n\n'.format(cenario['titulo'].replace('.', ''), cenario['titulo'].replace('.', '').lower().capitalize()) + '|**Objetivo**|' + tirar_quebra_de_linha(cenario['objetivo']) + '|\n|--|:--|\n' + '|**Contexto**|' + tirar_quebra_de_linha(cenario['contexto']) + '|\n' + '|**Ator(es)**|' + tirar_quebra_de_linha(cenario['atores']) + '|\n' + '|**Recursos**|' + tirar_quebra_de_linha(cenario['recursos']) + '|\n' + '|**Episódios**|' + tirar_quebra_de_linha(cenario['episodios']) + '|\n' + '|**Exceções**|' + tirar_quebra_de_linha(cenario['excecao']) + '|\n'
        arquivo.write(string + '<br><br>\n')

def criar_lexicos(arquivo, lexicos):
    str_lexicos = '### 3. <a name="Lexicos">Léxicos</a>\n\n'
    arquivo.write(str_lexicos)
    for lexico in lexicos:
        string = '### ***<a name="{}">{}</a>***\n\n'.format(tirar_quebra_de_linha(lexico['nome']), tirar_quebra_de_linha(lexico['nome'].lower().capitalize())) + '\n' + '|||\n-|-\n' + '|**Sinonimos**|' + tirar_quebra_de_linha(lexico['sinonimos']) + '\n' + '|**Noção**|' + tirar_quebra_de_linha(lexico['nocao']) +'|\n' + '|**Impacto**|' + tirar_quebra_de_linha(lexico['impacto']) + '|\n'
        arquivo.write(string)

with open('j.json', 'r') as f:
        datastore = json.load(f)

cenarios = []
lexicos = []

for cenario in datastore['cenario']:
    dictionary = {}
    dictionary['titulo'] = cenario['titulo']['#text']#['@id']
    dictionary['objetivo'] = dados_cenario(cenario['objetivo']['sentenca'])
    dictionary['contexto'] = dados_cenario(cenario['contexto']['sentenca'])
    dictionary['atores'] = dados_cenario(cenario['atores']['sentenca'])
    dictionary['recursos'] = dados_cenario(cenario['recursos']['sentenca'])
    dictionary['episodios'] = dados_cenario(cenario['episodios']['sentenca'])
    dictionary['excecao'] = dados_cenario(cenario['excecao']['sentenca'])
    cenarios.append(dictionary)
    
lista_de_lexicos = []
for lexico in datastore['lexico']:
    dictionary = {}
    dictionary['nome'] = lexico['nome_simbolo']["texto"].lower()
    lista_de_lexicos.append(lexico['nome_simbolo']['@id'])
    dictionary['nocao'] = dados_lexicos(lexico['nocao']['sentenca']['texto'])
    dictionary['impacto'] = dados_lexicos(lexico['impacto']['sentenca']['texto'])
    dictionary['sinonimos'] = recolher_sinonimos(lexico)

    lexicos.append(dictionary)

cenarios = sorted(cenarios, key=lambda k: k['titulo']) #ordenar, lista de dicionarios de cenarios, por titulo
lexicos = sorted(lexicos, key =lambda k: k['nome'])#ordenar, lista de dicionarios de lexicos, por nome

cen = open('cenarios.md', 'w')

criar_cenarios(cen, cenarios)

lex = open('lexicos.md', 'w')

criar_lexicos(lex, lexicos)
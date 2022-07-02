#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:16:10 2022

@author: locust
"""

import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=([dbc.themes.BOOTSTRAP]))
title = dbc.Row([
    dbc.Col([
        html.H1("This is a test app :>",
                className = 'text-primary')
        ])
    ])

navbar = dbc.Row([ 
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Simulações", href='#')),
            dbc.NavItem(dbc.NavLink("Implicações", href='#')),
            dbc.NavItem(dbc.NavLink("Satisfações", href='#'))],
        brand = "Colisor: Uma Simulação Subjetivamente Simples",
        brand_href="#",
        color="primary",
        dark=True
        )
    ])
contentbase = dbc.Row([ #Isso aqui é a coisa que vai ser trocada pelos page_content
    ])
page_content_simulacoes = dbc.Row([ #Adicionar dropdown para seleção de tipo de animação, etc.
    dbc.Col([dcc.Graph
             ])
    ]) #INSERIR AQUI ESTRUTURA DE SIMULAÇÃO
page_content_implicacoes = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Cacetada, isso é um título"), 
            html.H3("e isso, um subtítulo!")
            ])
        ]),
    dbc.Row([
        dbc.Col([
            html.H5("E isso aqui deveria explanar alguns aspectos da vida,\
                    universo e tudo mais...")
            ])
        ])
    ])
#page_content_satisfacoes = #INSERIR AQUI ESTURUTRA DE EXPLICAÇÃO DAS FUNÇÕES

app.layout = dbc.Container([ 
    title,
    navbar,
    page_content_implicacoes
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
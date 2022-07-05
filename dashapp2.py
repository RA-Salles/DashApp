#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:16:10 2022

@author: locust
"""

import dash
from dash import dcc, html, Output, Input
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
            dbc.NavItem(dbc.NavLink("Simulações" , href='/sim', id = 'simulacro' )),
            dbc.NavItem(dbc.NavLink("Implicações", href='/imp', id = 'implicacro')),
            dbc.NavItem(dbc.NavLink("Satisfações", href='/docs', id = 'satisfacro'))
            ],
        brand = "Colisor: Uma Simulação Subjetivamente Simples",
        brand_href="#",
        color="primary",
        dark=True
        )
    ])
contentbase = html.Div(id='test')
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
page_content_satisfacoes = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Cacetada, isso é um título"), 
            html.H3("e isso, um subtítulo!")
            ])
        ]),
    dbc.Row([
        dbc.Col([
            html.H5(" e isso aqui deveria conter algumas \
                    explicações acerca da documentação das classes\
                        e objetos criados no código")
            ])
        ])
    ])

app.layout = dbc.Container([ 
    title,
    navbar,
    
    ])

@app.callback(
    Output(component_id = 'test', component_property = 'children'),
    Input (component_id = 'simulacro', component_property = 'n_clicks')
    )

def displaysim(n_clicks):
    return page_content_simulacoes

@app.callback(
    Output(component_id = 'test', component_property = 'children'),
    Input (component_id = 'implicacro', component_property = 'n_clicks')
    )

def displayimp(n_clicks):
    return page_content_implicacoes

@app.callback(
    Output(component_id = 'test', component_property = 'children'),
    Input (component_id = 'satisfacro', component_property = 'n_clicks')
    )

def displaysats(n_clicks):
    return page_content_satisfacoes

if __name__ == '__main__':
    app.run_server(debug=True)
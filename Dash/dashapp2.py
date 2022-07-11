#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:16:10 2022

@author: locust (but contain code inspired by works of Pedro Giacomelli.)

Tnx Man!
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

page_content_simulacoes = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Simulações!:"), 
            html.H3("Onde podemos visualizar partículas fazendo coisas absurdas")
            ])
        ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph()
            ])
        ])
    ])

page_content_implicacoes = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Implicações!:"), 
            html.H3("Interpretação física dos gráficos")
            ])
        ]),
    dbc.Row([
        dbc.Col([
            html.H3("Um texto monolítico"),
            html.P("algumas explicações acerca da documentação das classes\
                       e objetos criados no código. Como podemos ver, esse aqui\
                       Ocupa simplesmente toda uma Row.")       
            ])
        ]),
        dbc.Row([
            html.H3(["Dois blocos:"])
            ]),
    dbc.Row([
        dbc.Col([
            html.H5("Sim, esse é um bloco"),
            html.P("Que contém um texto a ser preenchido")
            ]),
        dbc.Col([
            html.H5("E esse, outro"),
            html.P("Que contém um texto a ser preenchido. Como podemos ver,\
                   Ctrl+c, Ctrl+v continua sendo uma técnica viável. Poderia\
                       Até ser chamada de \"importação primitiva\". Cômico, não?")
            ])
        ])
    
    ])
                    
page_content_satisfacoes = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Satisfaçõs!:"), 
            html.H3("Contém links para alguns lugares úteis e indica a Efmat como\
                    possibilitadora dessa coisa toda. Incrível!")
            ])
        ]),
    dbc.Row([
        dbc.Col([
            html.H3("Um texto monolítico"),
            html.P("algumas explicações acerca da documentação das classes\
                       e objetos criados no código. Como podemos ver, esse aqui\
                       Ocupa simplesmente toda uma Row.")       
            ])
        ]),
        dbc.Row([
            html.H3(["Dois blocos:"])
            ]),
    dbc.Row([
        dbc.Col([
            html.H5("Sim, esse é um bloco"),
            html.P("Que contém um texto a ser preenchido")
            ],
            width = 6),
        dbc.Col([
            html.H5("E esse, outro"),
            html.P("Que contém um texto a ser preenchido. Como podemos ver,\
                   Ctrl+c, Ctrl+v continua sendo uma técnica viável. Poderia\
                       Até ser chamada de \"importação primitiva\". Cômico, não?")
            ],
            width = 6)
        ])
    
    ])

app.layout = dbc.Container([ 
    dcc.Location(id = 'url'),
    #title,
    navbar,
    contentbase
    ])

@app.callback(
    Output('test', 'children'),
    Input ('url', 'pathname')
    )
def displaysim(pathname):
    if pathname == '/sim':
        return page_content_simulacoes
    if pathname == '/imp':
        return page_content_implicacoes
    if pathname == '/docs':
        return page_content_satisfacoes
"""
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
"""
if __name__ == '__main__':
    app.run_server(debug=True)

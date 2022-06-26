# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets = [dbc.themes.BOOTSTRAP])
testalert = dbc.Alert("This is a test of import. If package was succesfully imported, then this should work",
                      color = "success")
title = html.H3("teste")
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("ph1", href = "google.com")),
        dbc.NavItem(dbc.NavLink("ph2", href = "google.com")),
        dbc.NavItem(dbc.NavLink("ph3", href = "google.com")),
        ],
    brand      = "Title",
    brand_href = "google.com",
    color      = "primary",
    dark       = False
    )

app.layout = dbc.Container(
    [
    dbc.Row(
        title
        ),
    dbc.Row(
        navbar
        ),
    dbc.Row([
        dbc.Col([dcc.Graph()], width = {"size":4, "offset": 2}),
        dbc.Col([dcc.Graph()], width = {"size":4, "offset": 2})
        ]),
    dbc.Row(
        html.H3("Final Stretch")
        )
    ])
    
#if __name__ = 
app.run_server()




































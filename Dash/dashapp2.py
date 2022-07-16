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
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=([dbc.themes.BOOTSTRAP]))
title = dbc.Row([
    dbc.Col([
        html.H1("",
                className = 'text-primary')
        ])
    ])

df1 = pd.read_csv('resistkinetic.csv')
fig1 = px.line(df1)

df2 = pd.read_csv('gravkinetic.csv')
fig2 = px.line(df2)

df3 = pd.read_csv('eletrokinetic.csv')
fig3 = px.line(df3)

df4 = pd.read_csv('restaurkinetic.csv')
fig4 = px.line(df4)

navbar = dbc.Row([ 
    dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(label = "Simulações", children = [
                dbc.DropdownMenuItem("Resistência", id = 'resist', href = '/sim/resist'),
                dbc.DropdownMenuItem("Gravidade", id = 'gravt', href = '/sim/gravt'),
                dbc.DropdownMenuItem("Repulsiva", id = 'repuls', href = '/sim/repuls'),
                dbc.DropdownMenuItem("Restauradora", id = 'restaur', href = '/sim/restaur')
                ]),
            dbc.NavItem(dbc.NavLink("Implicações", href='/imp', id = 'implicacro')),
            dbc.NavItem(dbc.NavLink("Satisfações", href='/docs', id = 'satisfacro'))
            ],
        brand = "Colisor: Uma Simulação Subjetivamente Simples",
        brand_href="#",
        color="primary",
        dark=True
        )
    ])

####
# SEÇÃO DE SIMULAÇÕES: ONDE O AFEGÃO MÉDIO SOFRE
####

page_content_simulacoes = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Bem Vindo ao colisor!:"), 
            html.H3("Onde podemos visualizar partículas fazendo coisas absurdas"),
            html.H6("e ficar tipo: \" que diabos as partículas estão fazendo??\" ")
            
            ])
        ]),
    dbc.Row([
        dbc.Col([
            html.P("Que tal começar vendo algumas simulações?"),
            dbc.DropdownMenu(label = "Simulações", children = [
                dbc.DropdownMenuItem("Resistência", id = 'resis', href = '/sim/resist'),
                dbc.DropdownMenuItem("Gravidade", id = 'grav', href = '/sim/gravt'),
                dbc.DropdownMenuItem("Repulsiva", id = 'repul', href = '/sim/repuls'),
                dbc.DropdownMenuItem("Restauradora", id = 'restau', href = '/sim/restaur')
                ])
            ]),
        dbc.Col([
            
            ])
        ])
    ])

page_content_simulacoes_resist = dbc.Container([
    dbc.Row([
        html.H3("Simulações: Resistência")
        ]),
    dbc.Row(
        dbc.Col([
            dcc.Graph(figure = fig1)],
            )
        ),
    dbc.Row([
        dbc.Col([html.H5("Movimentação:"),
                 html.P("É a única simulação que progrediu perfeitamente como o esperado.\
                        A energia parece tender para 15k unidades, bem menos que os milhões\
                            obtidos nas demais simulações.")], 
                        width = 6),
        dbc.Col([
            html.Img(src = "https://media0.giphy.com/media/rBDDhPm7G4SIL3ocHZ/giphy.gif",\
                     alt = "GIF RESTAURADOR")
            ], 
                width = 6,
                )
        ]),
    ],
    )

page_content_simulacoes_gravt = dbc.Container([
    dbc.Row([
        html.H3("Simulações: Gravidade")
        ]),
    dbc.Row([
        dbc.Col(
            html.H5("Energia:")
            )
        ]),
    dbc.Row(
        dbc.Col([
            dcc.Graph(figure = fig2)],
            )
        ),
    dbc.Row([
        dbc.Col([html.H5("Movimentação:"),
                 html.P("Elas possuem uma interação bem fraquinha, mas suficentemente perceptível. \
                        A incongruência, porém, é o fato da energia diminuir apesar da aceleração.")], width = 6),
        dbc.Col([
            html.Img(src = "https://media0.giphy.com/media/B8UeJyhvnpDK5dVGPU/giphy.gif",\
                     alt = "GIF RESTAURADOR")
            ], 
                width = 6,
                )
        ]),
    ],
    )

page_content_simulacoes_repuls = dbc.Container([
    dbc.Row([
        html.H3("Simulações: Repulsão/Eletricidade")
        ]),
    dbc.Row([
        dbc.Col([
            html.P("Sim, essa desgrama está quebrada e gerou resultados iguais à simulação de gravidade. Será concertada\
                   no v2 :D(?).")
            ])
        ]),
    dbc.Row(
        dbc.Col([
            dcc.Graph(figure = fig3)],
            )
        ),
    dbc.Row([
        dbc.Col([html.H5("Movimentação:"),
                 html.P("Eu gerei o gif algumas vezes para conferir, mas é literalmente a mesma coisa.\
                        Provavelmente um subproduto do fato que eu reaproveitei a função da gravidade para\
                            construir a interação elétrica.")], 
                        width = 6),
        dbc.Col([
            html.Img(src = "https://media0.giphy.com/media/B8UeJyhvnpDK5dVGPU/giphy.gif",\
                     alt = "GIF RESTAURADOR")
            ], 
                width = 6,
                )
        ]),
    ],
    )

page_content_simulacoes_restaur = dbc.Container([
    dbc.Row([
        html.H3("Simulações: Restauradora")
        ]),
    dbc.Row(
        dbc.Col([
            dcc.Graph(figure = fig4)],
            )
        ),
    dbc.Row([
        dbc.Col([html.H5("Movimentação:"),
                 html.P("A mais louca de todas elas. O gráfico tem uma amplitude absurda. Em compensação\
                        a movimentação é satisfatória de se assistir, especialmente com as colisões.")], 
                        width = 6),
        dbc.Col([
            html.Img(src = "https://media0.giphy.com/media/nhqPjRIdtHl14IuZD2/giphy.gif?cid=790b76110a1285c52af793cf7d13c3d2e6120784abdcefe7&rid=giphy.gif&ct=g", 
                     alt = "GIF RESTAURADOR")
            ], 
                width = 6,
                )
        ]),
    
    ],
    )


contentbase = html.Div([
    page_content_simulacoes
    ],
                       id='test')

page_content_implicacoes = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Implicações! :"), 
            html.H3("Suposta Interpretação física dos gráficos e comentários dos aspectos do trabalho realizado")
            ])
        ]),
    dbc.Row([
        dbc.Col([
            html.H3("Obtendo a energia:"),
            html.P("A função utilizada para calcular a energia do sistema\
                   é simples, pois segue a definição. multiplicar a massa\
                       pelo quadrado da velocidade sobre 2. Cria-se uma lista\
                           de energias para cada tempo e geramos um gráfico a partir\
                               disso. Eis, então, o método de obtenção da energia")       
            ])
        ]),
        dbc.Row([
            html.H3(["Dos gráficos e animações:"])
            ]),
    dbc.Row([
        dbc.Col([
            html.H5("Amplitude:"),
            html.P("Apesar da classe constantemente somar a aceleração nas partículas,\
                   O gráfico das funções se recusa a simplesmente crescer. Pelo contrário,\
                       com exceção da força de resistência, que foi desenhado para dificultar o\
                           crescimento da energia, todos eles conseguem dissipar energia quase magicamente.\
                               \n Infelizmente, apesar da constatação de uma amplitude exacerbada, não sei \
                                   o que exatamente a gera. Não, sério, olhe essa coisa aqui embaixo. \
                                       Ele pula de 100 bilhões de unidades para 4. Talvez seja o efeito de transformação de energia\
                                           cinética em potencial, mas, ainda assim, é fato que essa é uma amplitude absurda.")
            ]),
        dbc.Col([
            html.H5("Velocidade e obtenção:"),
            html.P("Para garantir um tempo hábil de visualização das animações,\
                   elas pulam cerca de 200 frames por vez. Se porventura eu colocasse\
                       para que fossem exibidos todos os 20000 frames do gif, o computador\
                           não conseguiria salvar o gif final e a animação rodando em tempo real\
                               demoraria cerca de 15 minutos para executar completamente. Ah sim,\
                                   as animações foram obtidas pela função de transformar um gráfico em\
                                       um gif no matplotlib. Daí, um upload pro giphy e temos um link\
                                           para usar. Simplesmente lindo.")
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure = fig4)
                ],
                width = 6),
            dbc.Col([
                html.Img(src = "https://media0.giphy.com/media/nhqPjRIdtHl14IuZD2/giphy.gif?cid=790b76110a1285c52af793cf7d13c3d2e6120784abdcefe7&rid=giphy.gif&ct=g",\
                         alt = "GIF RESTAURADOR")
                ])
             ]
            ),
        dbc.Row([
            html.H3("Da geração de posições:")
            ]),
        dbc.Row([
            dbc.Col([
                html.H5("Estrutura geral de funcionamento:"),
                html.P("Funciona de uma maneira bem simples, na verdade: Gere partículas, calcule posições, plote pontos.\
                       Essa é a ideia geral. O problema começa nas especificidades. Algumas funções, como a colisão, devem ser\
                           executadas primeiro e só podem ser executadas sob condições bem específicas (nesse caso, dependente do posicionamento\
                            de outras partículas). A ideia geral é, de fato, bem simples. Nem por isso o código ficou com 700 linhas por nada.")
                ]),
            dbc.Col([
                html.H5("Tempo real:"),
                html.P("Não o caso. Apesar de ser possível, o programa pré-calcula as\
                       posições antes de plotá-las. É o que possibilitou portar tão facilmente\
                           os gráficos de energia, inclusive! As informações foram transformadas\
                               em csv\'s e depois transformadas em gráficos de plotly. ")
                ])
            ])
    ])
                    
page_content_satisfacoes = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Satisfações!:"), 
            html.H3("Contém links para alguns lugares úteis e indica a Efmat como\
                    possibilitadora dessa coisa toda. Incrível!")
            ])
        ]),
    dbc.Row([
        dbc.Col([
            html.H3("A Efmat"),
            html.P("[lembrar de pedir uma descrição mais precisa para o felipe]")       
            ])
        ]),
        dbc.Row([
            html.Div()
            ]),
    dbc.Row([
        dbc.Col([
            html.H5("Ryan Salles"),
            html.P("Um autêntico tomador de café e construtor desse site, o qual deseja-te um bom dia.\
                   Ele tambem é bem ruim em se autodescrever, perceptivelmente.")
            ],
            width = 6),
        dbc.Col([
            html.H5("O repositório"),
            html.A("Ele guarda os códigos desse trabalho!", href ="https://github.com/RA-Salles/DashApp")
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
    if pathname == '/sim/resist':
        return page_content_simulacoes_resist
    elif pathname == '/sim/gravt':
        return page_content_simulacoes_gravt
    elif pathname == '/sim/repuls':
        return page_content_simulacoes_repuls
    elif pathname == '/sim/restaur':
        return page_content_simulacoes_restaur
    elif pathname == '/imp':
        return page_content_implicacoes
    elif pathname == '/docs':
        return page_content_satisfacoes
    elif pathname == '/':
        return page_content_simulacoes

"""
@app.callback(
    Output('mainboi', 'fig'),
    Input('')
    )

def changegraph(path):
    if path == '/sim/resist':
        df = pd.read_csv('resistkinetic.csv')
        fig = px.line(df)
    elif path == '/sim/gravt':
        df = pd.read_csv('resistkinetic.csv')
        fig = px.line(df)
    elif path == '/sim/repuls':
        df = pd.read_csv('resistkinetic.csv')
        fig = px.line(df)
    elif path == '/sim/restaur':
        df = pd.read_csv('resistkinetic.csv')
        fig = px.line(df)
    return fig
"""
if __name__ == '__main__':
    app.run_server(debug=True)

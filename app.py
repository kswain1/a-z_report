# coding: utf-8

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import os
import base64

app = dash.Dash(__name__)
server = app.server

# read data for tables (one df per table)
# df_fund_facts = pd.read_csv('https://plot.ly/~bdun9/2754.csv')
# df_price_perf = pd.read_csv('https://plot.ly/~bdun9/2756.csv')
# df_current_prices = pd.read_csv('https://plot.ly/~bdun9/2753.csv')
# df_hist_prices = pd.read_csv('https://plot.ly/~bdun9/2765.csv')
# df_avg_returns = pd.read_csv('https://plot.ly/~bdun9/2793.csv')
# df_after_tax = pd.read_csv('https://plot.ly/~bdun9/2794.csv')
# df_recent_returns = pd.read_csv('https://plot.ly/~bdun9/2795.csv')
# df_equity_char = pd.read_csv('https://plot.ly/~bdun9/2796.csv')
# df_equity_diver = pd.read_csv('https://plot.ly/~bdun9/2797.csv')
# df_expenses = pd.read_csv('https://plot.ly/~bdun9/2798.csv')
# df_minimums = pd.read_csv('https://plot.ly/~bdun9/2799.csv')
# df_dividend = pd.read_csv('https://plot.ly/~bdun9/2800.csv')
# df_realized = pd.read_csv('https://plot.ly/~bdun9/2801.csv')
# df_unrealized = pd.read_csv('https://plot.ly/~bdun9/2802.csv')
#df_graph = pd.read_csv("https://plot.ly/~bdun9/2804.csv")

# reusable componenets
def make_dash_table(df):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def print_button():
    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

# includes page/full view
def get_logo():
    logo = html.Div([

        html.Div([

            html.Img(src='https://gdurl.com/huiu', height='30', width='80')
        ], className="ten columns "),


        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Athlete Injury Risk Report')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/overview', className="tab first"),

        dcc.Link('Medical History   ', href='/price-performance', className="tab"),

        dcc.Link('Average Composite Score  ', href='/portfolio-management', className="tab"),

        #dcc.Link('Neuromusclar Report  ', href='/fees', className="tab"),

        #dcc.Link('Assesment   ', href='/distributions', className="tab"),

        #dcc.Link('Treatment   ', href='/news-and-reviews', className="tab")

    ], className="row ")
    return menu

    # includes page/full view
def get_ProfilePic():
    ProfilePic = html.Div([

        html.Div([
            html.Img(src='http://gdurl.com/JFia', height='150', width='150')
            #html.Img(src='http://logonoid.com/images/vanguard-logo.png', height='40', width='160')
        ], className="five columns"),

        html.Div([
          html.Strong(["Name"]),
          html.P(" "),
          html.P("Age"),
          html.P("Position"),
          html.P("Current Injury"),
          html.P("Previous Injury"),

        ],    className="two columns padded "),

        html.Div([
          html.Strong(["Serena Williams"]),
          html.P(" "),
          html.P("19"),
          html.P("Center"),
          html.P("None"),
          html.Br([]),
          html.P("Right Hamstring", className="two columns"),

        ],  className= "five columns padded "),

], className="row ")

      


    return ProfilePic

## Page layouts
overview = html.Div([  # page 1

        print_button(),

        html.Div([
            
            # Header
            #get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 3

            html.Div([

                html.Div([
                    html.H6('Medical History',
                            className="gs-header gs-text-header padded"),

                    html.Br([]),
                    get_ProfilePic(),


                ], className="six columns"),

              html.Div([
                    html.H6("Injury Risk Potential",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id='graph-3',
                        figure = {
                            'data': [
                                go.Scatter(
                                    x = ["0", "0.18", "0.18", "0"],
                                    y = ["0.2", "0.2", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(0, 128, 0, 0.2)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "B",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.2", "0.38", "0.38", "0.2", "0.2"],
                                    y = ["0.2", "0.2", "0.6", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(0, 128, 0, 0.4)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "D",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.4", "0.58", "0.58", "0.4", "0.4"],
                                    y = ["0.2", "0.2", "0.8", "0.6", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(255, 225, 53, 0.6)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "F",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.6", "0.78", "0.78", "0.6", "0.6"],
                                    y = ["0.2", "0.2", "1", "0.8", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgb(255,  69,  0, 0.7)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "H",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.8", "0.98", "0.98", "0.8", "0.8"],
                                    y = ["0.2", "0.2", "1.2", "1", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(255,0,0, 0.9)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "J",
                                    showlegend = False
                                ),
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                    {
                                      "x": 0.69,
                                      "y": 0.6,
                                      "font": {
                                        "color": "rgb(31, 119, 180)",
                                        "family": "Raleway",
                                        "size": 30
                                      },
                                      "showarrow": False,
                                      "text": "<b>4</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.0631034482759,
                                      "y": -0.04,
                                      "align": "left",
                                      "font": {
                                        "color": "rgb(44, 160, 44)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Low Risk</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.92125,
                                      "y": -0.04,
                                      "align": "right",
                                      "font": {
                                        "color": "rgb(214, 39, 40)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>High Risk</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    }
                                  ],
                                  autosize = False,
                                  height = 200,
                                  width = 340,
                                  hovermode = "closest",
                                  margin = {
                                    "r": 10,
                                    "t": 20,
                                    "b": 80,
                                    "l": 10
                                  },
                                  shapes = [
                                    {
                                      "fillcolor": "rgb(255, 255, 255)",
                                      "line": {
                                        "color": "rgb(31, 119, 180)",
                                        "width": 4
                                      },
                                      "opacity": 1,
                                      "type": "circle",
                                      "x0": 0.621,
                                      "x1": 0.764,
                                      "xref": "x",
                                      "y0": 0.135238095238,
                                      "y1": 0.98619047619,
                                      "yref": "y"
                                    }
                                  ],
                                  showlegend = True,
                                  xaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.05, 1.05],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.3, 1.6],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6('Right Lower Extremity',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(
                        id = "graph-1",
                        figure={
                            'data': [
                                go.Scatter(
                                   x = ["Tib Anterior", "Peroneals", "Med Gastro", "Lat. Gastro"],
                                   y = ["80", "70", "90", "40"],
                                   marker = {
                                   "color": "rgb(0,0,0)"
                                   },
                                   name = "Bad Tracker"

                                  ),
                                go.Bar(
                                    x = ["Tib Anterior", "Peroneals", "Med Gastro", "Lat. Gastro"],
                                    y = ["75", "60", "85", "35"],
                                    marker = {
                                      "color": "rgb(0,128,0)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    name = "Good"
                                ),
                                go.Bar(
                                    x = ["Tib Anterior", "Peroneals", "Med Gastro", "Lat. Gastro"],
                                    y = ["5", "10", "5", "5"],
                                    marker = {
                                      "color": "rgb(255, 225, 53)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    name = "Ok"
                                ),
                                go.Bar(
                                    x = ["Tib Anterior", "Peroneals", "Med Gastro", "Lat. Gastro"],
                                    y = ["20", "30", "10", "60"],
                                    marker = {
                                      "color": "rgb(255,0,0)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                        }
                                    },
                                    name = "Bad"
                                ),
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                barmode = 'stack',
                                bargap = 0.35,
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0228945952895,
                                  "y": -0.189563896463,
                                  "orientation": "h",
                                  "yanchor": "top"
                                },
                                margin = {
                                  "r": 0,
                                  "t": 20,
                                  "b": 20,
                                  "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 340,
                                xaxis = {
                                  "autorange": True,
                                  "range": [-0.5, 4.5],
                                  "showline": True,
                                  "title": "",
                                  "type": "category"
                                },
                                yaxis = {
                                  "autorange": True,
                                  "range": [0, 22.9789473684],
                                  "showgrid": True,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear",
                                  "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

                 html.Div([
                    html.H6('Left Lower Extremity',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(
                        id = "graph-2",
                        figure={
                            'data': [
                                go.Scatter(
                                   x = ["Tib Anterior", "Peroneals", "Med Gastro", "Lat. Gastro"],
                                   y = ["45", "60", "90", "60"],
                                   marker = {
                                   "color": "rgb(0,0,0)"
                                   },
                                   name = "Bad Tracker"

                                  ),
                                go.Bar(
                                    x = ["Tib Anterior", "Peroneals", "Med Gastro", "Lat. Gastro"],
                                    y = ["40", "50", "85", "55"],
                                    marker = {
                                      "color": "rgb(0,128,0)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    name = "Good"
                                ),
                                go.Bar(
                                    x = ["Tib Anterior", "Peroneals", "Med Gastro", "Lat. Gastro"],
                                    y = ["5", "10", "5", "5"],
                                    marker = {
                                      "color": "rgb(255, 225, 53)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    name = "Ok"
                                ),
                                go.Bar(
                                    x = ["Tib Anterior", "Peroneals", "Med Gastro", "Lat. Gastro"],
                                    y = ["55", "40", "10", "40"],
                                    marker = {
                                      "color": "rgb(255,0,0)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                        }
                                    },
                                    name = "Bad"
                                ),
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                barmode = 'stack',
                                bargap = 0.35,
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0228945952895,
                                  "y": -0.189563896463,
                                  "orientation": "h",
                                  "yanchor": "top"
                                },
                                margin = {
                                  "r": 0,
                                  "t": 20,
                                  "b": 20,
                                  "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 340,
                                xaxis = {
                                  "autorange": True,
                                  "range": [-0.5, 4.5],
                                  "showline": True,
                                  "title": "",
                                  "type": "category"
                                },
                                yaxis = {
                                  "autorange": True,
                                  "range": [0, 22.9789473684],
                                  "showgrid": True,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear",
                                  "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row "),

            # Row 5

            html.Div([

                html.Div([

                    html.H6('Right Lower Extremity Explanation',
                            className="gs-header gs-table-header padded"),

                    html.H6('Assessment',className="six columns padded"),
                    html.P("This athlete is at risk of injuring their lateral gastro within the next season"),

                    html.H6("Treatment",className="six columns padded"),
                    html.P("Custom orthodotics will reduce injuries, and lateral gastro excerises"),
                ], className="six columns"),

                html.Div([

                    html.H6('Left Lower Extremity Explanation',
                            className="gs-header gs-table-header padded"),

                    html.H6('Assessment',className="six columns padded"),
                    html.P("This athlete is at risk of injuring their lateral gastro within the next season"),

                    html.H6("Treatment",className="six columns padded"),
                    html.P("Custom orthodotics will reduce injuries, and lateral gastro excerises"),
                ], className="six columns"),
                #get_logo(),

            ], className="row ")

        ], className="subpage")

    ], className="page")


pricePerformance = html.Div([  # page 2

        print_button(),

        html.Div([

            # Header
            get_header(),
            html.Br([]),
            get_menu(),

            html.Img(src='https://thumbs.dreamstime.com/b/website-under-construction-sign-grungy-style-vector-large-format-42461291.jpg',)

            ]),    

    ], className="page")


portfolioManagement = html.Div([ # page 3

        print_button(),

        html.Div([

            # Header

            #get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1
             html.Img(src='https://thumbs.dreamstime.com/b/website-under-construction-sign-grungy-style-vector-large-format-42461291.jpg',)
            
            ], className="row "),

    ], className="page")

# feesMins = html.Div([  # page 4

#         print_button(),

#         html.Div([

#             # Header

#             get_logo(),
#             get_header(),
#             html.Br([]),
#             get_menu(),

#             # Row 1

#             html.Div([

#                 html.Div([
#                     html.H6(["Expenses"],
#                             className="gs-header gs-table-header padded")
#                 ], className="twelve columns"),

#             ], className="row "),

#             # Row 2

#             html.Div([

#                 html.Div([
#                     html.Strong(),
#                     html.Table(make_dash_table(df_expenses)),
#                     html.H6(["Minimums"],
#                             className="gs-header gs-table-header padded"),
#                     html.Table(make_dash_table(df_minimums))
#                 ], className="six columns"),

#                 html.Div([
#                     html.Br([]),
#                     html.Strong("Fees on $10,000 invested over 10 years"),
#                     dcc.Graph(
#                         id = 'graph-6',
#                         figure = {
#                             'data': [
#                                 go.Bar(
#                                     x = ["Category Average", "This fund"],
#                                     y = ["2242", "329"],
#                                     marker = {"color": "rgb(53, 83, 255)"},
#                                     name = "A"
#                                 ),
#                                 go.Bar(
#                                     x = ["This fund"],
#                                     y = ["1913"],
#                                     marker = {"color": "#ADAAAA"},
#                                     name = "B"
#                                 )
#                             ],
#                             'layout': go.Layout(
#                                 annotations = [
#                                     {
#                                       "x": -0.0111111111111,
#                                       "y": 2381.92771084,
#                                       "font": {
#                                         "color": "rgb(0, 0, 0)",
#                                         "family": "Raleway",
#                                         "size": 10
#                                       },
#                                       "showarrow": False,
#                                       "text": "$2,242",
#                                       "xref": "x",
#                                       "yref": "y"
#                                     },
#                                     {
#                                       "x": 0.995555555556,
#                                       "y": 509.638554217,
#                                       "font": {
#                                         "color": "rgb(0, 0, 0)",
#                                         "family": "Raleway",
#                                         "size": 10
#                                       },
#                                       "showarrow": False,
#                                       "text": "$329",
#                                       "xref": "x",
#                                       "yref": "y"
#                                     },
#                                     {
#                                       "x": 0.995551020408,
#                                       "y": 1730.32432432,
#                                       "font": {
#                                         "color": "rgb(0, 0, 0)",
#                                         "family": "Raleway",
#                                         "size": 10
#                                       },
#                                       "showarrow": False,
#                                       "text": "You save<br><b>$1,913</b>",
#                                       "xref": "x",
#                                       "yref": "y"
#                                     }
#                                   ],
#                                   autosize = False,
#                                   height = 150,
#                                   width = 340,
#                                   bargap = 0.4,
#                                   barmode = "stack",
#                                   hovermode = "closest",
#                                   margin = {
#                                     "r": 40,
#                                     "t": 20,
#                                     "b": 20,
#                                     "l": 40
#                                   },
#                                   showlegend = False,
#                                   title = "",
#                                   xaxis = {
#                                     "autorange": True,
#                                     "range": [-0.5, 1.5],
#                                     "showline": True,
#                                     "tickfont": {
#                                       "family": "Raleway",
#                                       "size": 10
#                                     },
#                                     "title": "",
#                                     "type": "category",
#                                     "zeroline": False
#                                   },
#                                   yaxis = {
#                                     "autorange": False,
#                                     "mirror": False,
#                                     "nticks": 3,
#                                     "range": [0, 3000],
#                                     "showgrid": True,
#                                     "showline": True,
#                                     "tickfont": {
#                                       "family": "Raleway",
#                                       "size": 10
#                                     },
#                                     "tickprefix": "$",
#                                     "title": "",
#                                     "type": "linear",
#                                     "zeroline": False
#                                   }
#                             )
#                         },
#                         config={
#                             'displayModeBar': False
#                         }
#                     )
#                 ], className="six columns"),

#             ], className="row "),

#             # Row 3

#             html.Div([

#                 html.Div([
#                     html.H6(["Fees"],
#                             className="gs-header gs-table-header padded"),

#                     html.Br([]),

#                     html.Div([

#                         html.Div([
#                             html.Strong(["Purchase fee"])
#                         ], className="three columns right-aligned"),

#                         html.Div([
#                             html.P(["None"])
#                         ], className="nine columns")


#                     ], className="row "),

#                     html.Div([

#                         html.Div([
#                             html.Strong(["Redemption fee"])
#                         ], className="three columns right-aligned"),

#                         html.Div([
#                             html.P(["None"])
#                         ], className="nine columns")

#                     ], className="row "),

#                     html.Div([

#                         html.Div([
#                             html.Strong(["12b-1 fee"])
#                         ], className="three columns right-aligned"),

#                         html.Div([
#                             html.P(["None"])
#                         ], className="nine columns")

#                     ], className="row "),

#                     html.Div([

#                         html.Div([
#                             html.Strong(["Account service fee"])
#                         ], className="three columns right-aligned"),

#                         html.Div([
#                             html.Strong(["Nonretirement accounts, traditional IRAs, Roth IRAs, UGMAs/UTMAs, SEP-IRAs, and education savings accounts (ESAs)"]),
#                             html.P(["We charge a $20 annual account service fee for each Vanguard Brokerage Account, as well as each individual Vanguard mutual fund holding with a balance of less than $10,000 in an account. This fee does not apply if you sign up for account access on vanguard.com and choose electronic delivery of statements, confirmations, and Vanguard fund reports and prospectuses. This fee also does not apply to members of Flagship Select™, Flagship®, Voyager Select®, and Voyager® Services."]),
#                             html.Br([]),
#                             html.Strong(["SIMPLE IRAs"]),
#                             html.P(["We charge participants a $25 annual account service fee for each fund they hold in their Vanguard SIMPLE IRA. This fee does not apply to members of Flagship Select, Flagship, Voyager Select, and Voyager Services."]),
#                             html.Br([]),
#                             html.Strong(["403(b)(7) plans"]),
#                             html.P(["We charge participants a $15 annual account service fee for each fund they hold in their Vanguard 403(b)(7) account. This fee does not apply to members of Flagship Select, Flagship, Voyager Select, and Voyager Services."]),
#                             html.Br([]),
#                             html.Strong(["Individual 401(k) plans"]),
#                             html.P(["We charge participants a $20 annual account service fee for each fund they hold in their Vanguard Individual 401(k) account. This fee will be waived for all participants in the plan if at least 1 participant qualifies for Flagship Select, Flagship, Voyager Select, and Voyager Services"]),
#                             html.Br([]),
#                         ], className="nine columns")

#                     ], className="row ")

#                 ], className="twelve columns")

#             ], className="row "),

#         ], className="subpage")

#     ], className="page")

# distributions = html.Div([  # page 5

#         print_button(),

#         html.Div([

#             # Header

#             get_logo(),
#             get_header(),
#             html.Br([]),
#             get_menu(),

#             # Row 1

#             html.Div([

#                 html.Div([
#                     html.H6(["Distributions"],
#                             className="gs-header gs-table-header padded"),
#                     html.Strong(["Distributions for this fund are scheduled quaterly"])
#                 ], className="twelve columns"),

#             ], className="row "),

#             # Row 2

#             html.Div([

#                 html.Div([
#                     html.Br([]),
#                     html.H6(["Dividend and capital gains distributions"], className="gs-header gs-table-header tiny-header"),
#                     html.Table(make_dash_table(df_dividend), className="tiny-header")
#                 ], className="twelve columns"),

#             ], className="row "),

#             # Row 3

#             html.Div([

#                 html.Div([
#                     html.H6(["Realized/unrealized gains as of 01/31/2018"], className="gs-header gs-table-header tiny-header")
#                 ], className=" twelve columns")

#             ], className="row "),

#             # Row 4

#             html.Div([

#                 html.Div([
#                     html.Table(make_dash_table(df_realized))
#                 ], className="six columns"),

#                 html.Div([
#                     html.Table(make_dash_table(df_unrealized))
#                 ], className="six columns"),

#             ], className="row "),

#         ], className="subpage")

#     ], className="page")

# newsReviews = html.Div([  # page 6

#         print_button(),

#         html.Div([

#             # Header

#             get_logo(),
#             get_header(),
#             html.Br([]),
#             get_menu(),

#             # Row 1

#             html.Div([

#                 html.Div([
#                     html.H6('Vanguard News',
#                             className="gs-header gs-text-header padded"),
#                     html.Br([]),
#                     html.P('10/25/16    The rise of indexing and the fall of costs'),
#                     html.Br([]),
#                     html.P("08/31/16    It's the index mutual fund's 40th anniversary: Let the low-cost, passive party begin")
#                 ], className="six columns"),

#                 html.Div([
#                     html.H6("Reviews",
#                             className="gs-header gs-table-header padded"),
#                     html.Br([]),
#                     html.Li('Launched in 1976.'),
#                     html.Li('On average, has historically produced returns that have far outpaced the rate of inflation.*'),
#                     html.Li("Vanguard Quantitative Equity Group, the fund's advisor, is among the world's largest equity index managers."),
#                     html.Br([]),
#                     html.P("Did you know? The fund launched in 1976 as Vanguard First Index Investment Trust—the nation's first index fund available to individual investors."),
#                     html.Br([]),
#                     html.P("* The performance of an index is not an exact representation of any particular investment, as you cannot invest directly in an index."),
#                     html.Br([]),
#                     html.P("Past performance is no guarantee of future returns. See performance data current to the most recent month-end.")
#                 ], className="six columns"),

#             ], className="row ")

#         ], className="subpage")

#     ], className="page")

noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")



# Describe the layout, or the UI, of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update page
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return overview
    elif pathname == '/price-performance':
        return pricePerformance
    elif pathname == '/portfolio-management':
        return portfolioManagement
    elif pathname == '/fees':
        return feesMins
    elif pathname == '/distributions':
        return distributions
    elif pathname == '/news-and-reviews':
        return newsReviews
    elif pathname == '/full-view':
        return overview,pricePerformance,portfolioManagement,feesMins,distributions,newsReviews
    else:
        return noPage


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True)

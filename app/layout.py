import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table as dt

ui_messages = html.Div(
    id='messages',
    children=[
        dt.DataTable(id='messages-table'),
        html.Div(
            id='messages-container',
            className='force-overflow',
            style={
                'position': 'fixed',
                'maxWidth': '320px',
                'top': '10px',
                'left': 'calc(50% - 160px)',
                'maxHeight': 'calc(100vh - 10px)',
                'overflow': 'auto',
                'z-index': '999'
            },
            children=[]
        ),
    ]
)


header = dbc.Row([
    dbc.Col(
        width=12,
        lg=3,
        xl=3,
        style={'textAlign': 'center'}
    ),
    dbc.Col(
        width=12,
        lg=6,
        xl=6,
        children=[
            html.H1(
                children='Power Plant State Prediction',
                style={'color': '#323232'}
            ),
            html.H3(
                children='Expert System',
                style={'color': '#505050'}
            ),
        ],
        style={'textAlign': 'center'}
    )
])


files_upload = dbc.Card(dbc.CardBody([
    dbc.Row(
        align='start',
        children=[
            dbc.Col(
                width=7,
                children=dcc.Upload(
                    id='files-upload-btn',
                    multiple=True,
                    style_active=None,
                    style_reject=None,
                    children=[
                        dbc.Button(
                            children=[
                                "Upload Files ",
                                dbc.Badge(
                                    id='counter-badge',
                                    color="light",
                                    className="ml-1",
                                    children=0,
                                )
                            ],
                            color='primary',
                            style={'width': '100%'}
                        )
                    ]
                )
            ),
            dbc.Col(
                width=5,
                style={'textAlign': 'right'},
                children=[
                    dcc.Store(id='table-controls-store', data={}),
                    dbc.Button(
                        id='select-files-btn',
                        className='unselected',
                        color="primary",
                        disabled=True,
                        style={'height': '38px', 'width': '38px'}
                    ),
                    dbc.Button(
                        id='delete-files-btn',
                        className="ml-1",
                        color="primary",
                        disabled=True,
                        style={'height': '38px', 'width': '38px'}
                    ),
                ]
            ),
        ],
    ),
    dcc.Upload(
        id='files-upload',
        multiple=True,
        disable_click=True,
        style={
            'position': 'relative',
            'margin': '15px 0'
        },
        style_active={'background': '#94c8ff52'},
        children=[
            html.Div(id='files-table-back'),
            dt.DataTable(
                id='files-table',
                columns=[
                    {'id': 'filename', 'name': 'File'},
                    {'id': 'length', 'name': 'Ticks'},
                ],
                data=[],
                fixed_rows={'headers': True},
                page_action='none',
                row_selectable="multi",
                row_deletable=True,
                selected_rows=[],
                selected_row_ids=[],
                style_header={'display': 'none'},
                style_table={
                    'height': '340px',
                    'overflowY': 'auto'
                }
            )
        ]
    ),
    dbc.Row(
        align='center',
        justify='between',
        children=[
            dbc.Col(
                children=dbc.Checklist(
                    id="use_delta_switch",
                    options=[{"label": "ΔSinganal", "value": 1}],
                    value=[],
                    switch=True,
                )
            ),
            dbc.Col(
                width=4,
                children=dbc.DropdownMenu(
                    id='filter-select',
                    addon_type="prepend",
                    label='Original',
                    color='primary',
                    direction='up',
                    group=True,
                    right=True,
                    children=[
                        dbc.DropdownMenuItem("Original", id="orig-filter-select"),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem("FIR", id="fir-filter-select"),
                        dbc.DropdownMenuItem("IIR", id="iir-filter-select"),
                    ],
                )
            )
        ]
    ),
]))


signal = [
    html.Div(id='signal-graph-back', className='graph-back'),
    dbc.Row(
        dcc.Graph(
            id='signal-graph',
            config={
                'responsive': True,
                'displayModeBar': False,
            },
            style={
                'width': '100%',
                'height': '400px',
            },
            figure={
                'layout': {
                    'margin': {'t': 40, 'l': 40, 'b': 30, 'r': 20},
                    'showlegend': False
                }
            }
        ),
    )
]


statistic = [
    html.Div(id='statistic-graph-back', className='graph-back'),
    dbc.Row(
        dcc.Graph(
            id='statistic-graph',
            config={
                'responsive': True,
                'displayModeBar': False,
            },
            style={
                'width': '100%',
                'height': '400px',
            },
            figure={
                'layout': {
                    'barmode': 'overlay',
                    'xaxis': {
                        'anchor': 'y',
                        'domain': [0.0, 0.98],
                    },
                    'xaxis2': {
                        'anchor': 'y2',
                        'domain': [0.0, 0.98],
                        'matches': 'x',
                        'showgrid': False,
                        'showticklabels': False
                    },
                    'yaxis': {
                        'anchor': 'x',
                        'domain': [0.0, 0.7326],
                        'showgrid': False,
                    },
                    'yaxis2': {
                        'anchor': 'x2',
                        'domain': [0.7426, 1.0],
                        'matches': 'y2',
                        'showgrid': False,
                        'showticklabels': False
                    },
                    'legend': {'tracegroupgap': 0},
                    'margin': {'t': 40, 'l': 40, 'b': 30, 'r': 20},
                    'template': 'none',
                    'showlegend': False,
                }
            }
        ),
    )
]


spectrum = [
    html.Div(id='spectrum-graph-back', className='graph-back'),
    dbc.Row(
        dcc.Graph(
            id='spectrum-graph',
            config={
                'responsive': True,
                'displayModeBar': False,
            },
            style={
                'width': '100%',
                'height': '400px',
            },
            figure={
                'layout': {
                    'margin': {'t': 40, 'l': 40, 'b': 30, 'r': 20},
                    'showlegend': False
                }
            }
        ),
    )
]


features = dbc.Card(dbc.CardBody(dcc.Tabs([
    dcc.Tab(signal, label='Signal', style={'padding': '15px'}),
    dcc.Tab(statistic, label='Statistic', style={'padding': '15px'}),
    dcc.Tab(spectrum, label='Spectrum', style={'padding': '15px'})
], style={"margin": 'calc(-1.25rem - 1px)', 'marginBottom': 0}), style={'boxSizing': 'border-box'}))


radar = dbc.Card(dbc.CardBody([
    html.Div(id='radar-graph-back', className='graph-back'),
    dbc.Row(
        dcc.Graph(
            id='radar-graph',
            config={
                'responsive': True,
                'displayModeBar': False,
            },
            style={
                'width': '100%',
                'height': '400px',
            },
            figure={
                'layout': {
                    'title': 'Classification',
                    'margin': {'t': 40, 'l': 40, 'b': 30, 'r': 20},
                    'showlegend': False
                }
            }
        ),
    )
]))


trend = dbc.Card(dbc.CardBody([
    html.Div(id='trend-graph-back', className='graph-back'),
    dbc.Row(
        dcc.Graph(
            id='trend-graph',
            config={
                'responsive': True,
                'displayModeBar': False,
            },
            style={
                'width': '100%',
                'height': '400px',
            },
            figure={
                'layout': {
                    'title': 'Trend',
                    'margin': {'t': 40, 'l': 40, 'b': 30, 'r': 20},
                    'showlegend': False
                },
                'data': []
            }
        ),
    )
]))


body = html.Div(
    children=[
        dt.DataTable(id='content-table', page_action='none', data=[]),
        dt.DataTable(id='upload-table', page_action='none', data=[]),
        dt.DataTable(id='signal-table', page_action='none', data=[]),
        ui_messages,
        header,
        dbc.Row([
            dbc.Col(files_upload, width=12, lg=4, xl=4),
            dbc.Col(features, width=12, lg=8, xl=8)
        ]),
        dbc.Row([
            dbc.Col(radar, width=12, lg=5, xl=5),
            dbc.Col(trend, width=12, lg=7, xl=7)
        ]),
    ],
    style={
        'padding': '0 15px 0 15px',
        'backgroundColor': '#f7f7f7',
        'minHeight': '100vh',
    }
)

#Variables

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
#import geopandas as gpd
import flask
import os



#import os
#import pandas as pd

#Abre bd
entidades= pd.read_csv("https://raw.githubusercontent.com/fdealbam/censo2020/main/zmall2020.csv")#, encoding= "Latin-1")
######################################################################

############################################################################ TEMÄTICA
variables_tematica= pd.read_csv("https://raw.githubusercontent.com/fdealbam/0entrada/main/diccionario_variables.csv", encoding= "latin-1")

tema_pre = variables_tematica[variables_tematica.MNEMONICO == "PNACOE"]
descriptor = tema_pre.iloc[0]['DESCRIPCION']
tema = tema_pre.iloc[0]['TEMATICA']




#____________VARIABLES LIST
#for_var = [
##'POBTOT',
##'POBFEM','POBMAS',
#'P_0A2','P_3A5','P_6A11','P_12A14','P_15A17','POB15_64','P_60YMAS','P_15YMAS','P_18YMAS',
#'PNACOE','PNACOE_F',
#'PRESOE15',
#'PNACOE',
#'P15YM_AN',
#'P15SEC_CO','P18YM_PB',
#'PE_INAC','POCUPADA','POCUPADA_F','POCUPADA_M','PDESOCUP',
#'PSINDER','PDER_IMSS','PDER_SEGP','PAFIL_IPRIV',
#'PCATOLICA','PRO_CRIEVA','POTRAS_REL','PSIN_RELIG',
#'TOTHOG','HOGJEF_F','POBHOG','PHOGJEF_F','PHOGJEF_M',
#'VIVTOT','TVIVHAB','PROM_OCUP','PRO_OCUP_C','VPH_1DOR',
#
#'VPH_C_ELEC','VPH_AGUADV','VPH_TINACO','VPH_CISTER','VPH_EXCSA','VPH_DRENAJ','VPH_REFRI',
#'VPH_LAVAD','VPH_BICI','VPH_TV','VPH_PC','VPH_CEL','VPH_INTER',
#'VPH_SPMVPI','PCDISC_MOT',
#'PCDIvaSC_VIS',
#'PCDISC_LENG',
#'PCDISC_AUD',]


#____________VARIABLES LIST
#for v in for_var:
mas10   = entidades.sort_values("PNACOE_%" , ascending=False,ignore_index=True ).head(10)
menos10 = entidades.sort_values("PNACOE_%" , ascending=True,ignore_index=True ).head(10)

#___________ MÄS
masnamezm1 = mas10.iloc[0]["NOM_ZM"]
masnamezm2 = mas10.iloc[1]["NOM_ZM"]
masnamezm3 = mas10.iloc[2]["NOM_ZM"]
masnamezm4 = mas10.iloc[3]["NOM_ZM"]
masnamezm5 = mas10.iloc[4]["NOM_ZM"]
masnamezm6 = mas10.iloc[5]["NOM_ZM"]
masnamezm7 = mas10.iloc[6]["NOM_ZM"]
masnamezm8 = mas10.iloc[7]["NOM_ZM"]
masnamezm9 = mas10.iloc[8]["NOM_ZM"]
masnamezm10= mas10.iloc[9]["NOM_ZM"]

masvaluezm1 = mas10.iloc[0]["PNACOE"]
masvaluezm2 = mas10.iloc[1]["PNACOE"]
masvaluezm3 = mas10.iloc[2]["PNACOE"]
masvaluezm4 = mas10.iloc[3]["PNACOE"]
masvaluezm5 = mas10.iloc[4]["PNACOE"]
masvaluezm6 = mas10.iloc[5]["PNACOE"]
masvaluezm7 = mas10.iloc[6]["PNACOE"]
masvaluezm8 = mas10.iloc[7]["PNACOE"]
masvaluezm9 = mas10.iloc[8]["PNACOE"]
masvaluezm10= mas10.iloc[9]["PNACOE"]

masvaluezm1_p = mas10.iloc[0]["PNACOE_%"]
masvaluezm2_p = mas10.iloc[1]["PNACOE_%"]
masvaluezm3_p = mas10.iloc[2]["PNACOE_%"]
masvaluezm4_p = mas10.iloc[3]["PNACOE_%"]
masvaluezm5_p = mas10.iloc[4]["PNACOE_%"]
masvaluezm6_p = mas10.iloc[5]["PNACOE_%"]
masvaluezm7_p = mas10.iloc[6]["PNACOE_%"]
masvaluezm8_p = mas10.iloc[7]["PNACOE_%"]
masvaluezm9_p = mas10.iloc[8]["PNACOE_%"]
masvaluezm10_p= mas10.iloc[9]["PNACOE_%"]

#_____________ MENOS
menosnamezm1 = menos10.iloc[0]["NOM_ZM"]
menosnamezm2 = menos10.iloc[1]["NOM_ZM"]
menosnamezm3 = menos10.iloc[2]["NOM_ZM"]
menosnamezm4 = menos10.iloc[3]["NOM_ZM"]
menosnamezm5 = menos10.iloc[4]["NOM_ZM"]
menosnamezm6 = menos10.iloc[5]["NOM_ZM"]
menosnamezm7 = menos10.iloc[6]["NOM_ZM"]
menosnamezm8 = menos10.iloc[7]["NOM_ZM"]
menosnamezm9 = menos10.iloc[8]["NOM_ZM"]
menosnamezm10= menos10.iloc[9]["NOM_ZM"]

menosvaluezm1 = menos10.iloc[0]["PNACOE"]
menosvaluezm2 = menos10.iloc[1]["PNACOE"]
menosvaluezm3 = menos10.iloc[2]["PNACOE"]
menosvaluezm4 = menos10.iloc[3]["PNACOE"]
menosvaluezm5 = menos10.iloc[4]["PNACOE"]
menosvaluezm6 = menos10.iloc[5]["PNACOE"]
menosvaluezm7 = menos10.iloc[6]["PNACOE"]
menosvaluezm8 = menos10.iloc[7]["PNACOE"]
menosvaluezm9 = menos10.iloc[8]["PNACOE"]
menosvaluezm10= menos10.iloc[9]["PNACOE"]

menosvaluezm1_p = menos10.iloc[0]["PNACOE_%"]
menosvaluezm2_p = menos10.iloc[1]["PNACOE_%"]
menosvaluezm3_p = menos10.iloc[2]["PNACOE_%"]
menosvaluezm4_p = menos10.iloc[3]["PNACOE_%"]
menosvaluezm5_p = menos10.iloc[4]["PNACOE_%"]
menosvaluezm6_p = menos10.iloc[5]["PNACOE_%"]
menosvaluezm7_p = menos10.iloc[6]["PNACOE_%"]
menosvaluezm8_p = menos10.iloc[7]["PNACOE_%"]
menosvaluezm9_p = menos10.iloc[8]["PNACOE_%"]
menosvaluezm10_p= menos10.iloc[9]["PNACOE_%"]


#_________BULLETS (MÄS+)
bulletmas_p = ("En valores relativos, la zona metropolitana de "+masnamezm1+" es la que más tiene "+
               descriptor+" ("+str(masvaluezm1_p)+"%), "+
"seguida por "+masnamezm2+" ("+str(masvaluezm2_p)+"%); "+
 masnamezm3+" ("+str(masvaluezm3_p)+"%); "+
 masnamezm4+" ("+str(masvaluezm4_p)+"%); "+
 masnamezm5+" ("+str(masvaluezm5_p)+"%); "+
 masnamezm6+" ("+str(masvaluezm6_p)+"%); "+
 masnamezm7+" ("+str(masvaluezm7_p)+"%); "+
 masnamezm8+" ("+str(masvaluezm8_p)+"%); "+
 masnamezm9+" ("+str(masvaluezm9_p)+"%); finalmente, por "+
 masnamezm10+" ("+str(masvaluezm10_p)+"%).")

bulletmas = ("En valores absolutos, la zona metropolitana de "+masnamezm1+" es la que más tiene "+
             descriptor+" ("+str(f'{masvaluezm1:,d}')+"), "+
"seguida por "+masnamezm2+" ("+str(f'{masvaluezm2:,d}')+" ); "+
 masnamezm3+" ("+str(f'{masvaluezm3:,d}')+"); "+
 masnamezm4+" ("+str(f'{masvaluezm4:,d}')+"); "+
 masnamezm5+" ("+str(f'{masvaluezm5:,d}')+"); "+
 masnamezm6+" ("+str(f'{masvaluezm6:,d}')+"); "+
 masnamezm7+" ("+str(f'{masvaluezm7:,d}')+"); "+
 masnamezm8+" ("+str(f'{masvaluezm8:,d}')+"); "+
 masnamezm9+" ("+str(f'{masvaluezm9:,d}')+"); finalmente, por "+
 masnamezm10+" ("+str(f'{masvaluezm10:,d}')+").")

#_________BULLETS (MENOS-)
bulletmenos_p = ("En valores relativos, la zona metropolitana de "+menosnamezm1+" es la que menos tiene "+
             descriptor+" ("+str(menosvaluezm1_p)+"%); "+
"seguida por "+menosnamezm2+" ("+str(menosvaluezm2_p)+"%); "+
 menosnamezm3+" ("+str(menosvaluezm3_p)+"%); "+
 menosnamezm4+" ("+str(menosvaluezm4_p)+"%); "+
 menosnamezm5+" ("+str(menosvaluezm5_p)+"%); "+
 menosnamezm6+" ("+str(menosvaluezm6_p)+"%); "+
 menosnamezm7+" ("+str(menosvaluezm7_p)+"%); "+
 menosnamezm8+" ("+str(menosvaluezm8_p)+"%); "+
 menosnamezm9+" ("+str(menosvaluezm9_p)+"%); finalmente, por "+
 menosnamezm10+" ("+str(menosvaluezm10_p)+"%).")

bulletmenos = ("En valores absolutos, la zona metropolitana de "+menosnamezm1+" es la que menos tiene "+
             descriptor+" ("+str(f'{menosvaluezm1:,d}')+"); "+
"seguida por "+menosnamezm2+" ("+str(f'{menosvaluezm2:,d}')+"); "+
 menosnamezm3+" ("+str(f'{menosvaluezm3:,d}')+"); "+
 menosnamezm4+" ("+str(f'{menosvaluezm4:,d}')+"); "+
 menosnamezm5+" ("+str(f'{menosvaluezm5:,d}')+"); "+
 menosnamezm6+" ("+str(f'{menosvaluezm6:,d}')+"); "+
 menosnamezm7+" ("+str(f'{menosvaluezm7:,d}')+"); "+
 menosnamezm8+" ("+str(f'{menosvaluezm8:,d}')+"); "+
 menosnamezm9+" ("+str(f'{menosvaluezm9:,d}')+"); finalmente, por "+
 menosnamezm10+" ("+str(f'{menosvaluezm10:,d}')+").")


############################################################################ TABLA_1
## Tabla de variablesvar (MAS+)
row0title = html.Tr([
                html.Td("Zona metropolitana", 
                      style={"color": "black",
                          "font-size": ".5em",
                          "font-family": "Arial",
                            "width":"14rem",
                             "textAlign": "right",
                            "padding-top": "0rem",  
                            "padding-bottom": "0rem",
                                          "padding-left": "0rem",
                                          "padding-right": "0rem",
                              }),
                html.Td("Total",
                         style={"color": "black",
                          "font-size": ".5em",
                                "margin-left":".5em",
                            "width":"2rem",
                            "padding-top": "0rem",  
                            "padding-bottom": "0rem",
                            "padding-right": "0rem",
                              }),
                 html.Td( "%", 
                        style={"color": "black",
                          "font-size": ".5em",
                            "width":"1rem",
                             "textAlign": "center",
                            "padding-top": "0rem",   
                            "padding-bottom": "0rem",
                            "padding-right": "0rem",
                              })
                ], style={"padding-top": "0rem",
                           "padding-bottom": "0rem",
                           "padding-left": "0rem",
                           "padding-right": "0rem",
                         "stripped": True,    
                           "no_gutters": True,
                             })



row1zmfirst = html.Tr([
                html.Td(masnamezm1, 
                      style={ "color": "green",
                          "font-size": ".5em",
                          #"font-family": "Arial",
                            "width":"14rem",
                             "textAlign": "right",
                            "padding-top": "0rem",  
                            "padding-bottom": "0rem",
                                          "padding-left": "0rem",
                                          "padding-right": "0rem",
                              }),
                html.Td(f"{int(masvaluezm1):,}",
                         style={"color": "black",
                             "font-size": ".5em",
                                "margin-left":".5em",
                            "width":"2rem",
                            "padding-top": "0rem",  
                            "padding-bottom": "0rem",
                            "padding-right": "0rem",
                              }),
                 html.Td( [(masvaluezm1_p),"%"], 
                        style={ "color": "green",
                            "font-size": ".5em",
                            "width":"1rem",
                            "padding-top": "0rem",   
                            "padding-bottom": "0rem",
                                          "padding-right": "0rem",
                              })], style={"padding-top": "0rem",
                                          "padding-bottom": "0rem",
                                          "padding-left": "0rem",
                                          "padding-right": "0rem",
                                          "no_gutters": True,
                                            })
row2 = html.Tr([html.Td(masnamezm2, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(masvaluezm2):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(masvaluezm2_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row3 = html.Tr([html.Td(masnamezm3, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(masvaluezm3):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(masvaluezm3_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row4 = html.Tr([html.Td(masnamezm4, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(masvaluezm4):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(masvaluezm4_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row5 = html.Tr([html.Td(masnamezm5, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(masvaluezm5):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(masvaluezm5_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row6 = html.Tr([html.Td(masnamezm6, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(masvaluezm6):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(masvaluezm6_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row7 = html.Tr([html.Td(masnamezm7, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(masvaluezm7):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(masvaluezm7_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row8 = html.Tr([html.Td(masnamezm8, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(masvaluezm8):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(masvaluezm8_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row9 = html.Tr([html.Td(masnamezm9, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(masvaluezm9):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(masvaluezm9_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row10 = html.Tr([html.Td(masnamezm10, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(masvaluezm10):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(masvaluezm10_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

table_body = [html.Tbody([row0title, row1zmfirst,
                          row2, row3, row4,row5, row6, row7, row8, row9, row10 
], style={
          "padding-top": "0rem",
          "padding-bottom": "0rem",
          "padding-left": "0em",
          "padding-right": "0em",
          "no_gutters": True})]


############################################################################ TABLA_2
## Tabla de variablesvar (MENOS-)
row0title = html.Tr([
                html.Td("Zona metropolitana", 
                      style={"color": "black",
                          "font-size": ".5em",
                          "font-family": "Arial",
                            "width":"14rem",
                             "textAlign": "right",
                            "padding-top": "0rem",  
                            "padding-bottom": "0rem",
                                          "padding-left": "0rem",
                                          "padding-right": "0rem",
                              }),
                html.Td("Total",
                         style={"color": "black",
                          "font-size": ".5em",
                                "margin-left":".5em",
                            "width":"2rem",
                            "padding-top": "0rem",  
                            "padding-bottom": "0rem",
                            "padding-right": "0rem",
                              }),
                 html.Td( "%", 
                        style={"color": "black",
                          "font-size": ".5em",
                            "width":"1rem",
                             "textAlign": "center",
                            "padding-top": "0rem",   
                            "padding-bottom": "0rem",
                            "padding-right": "0rem",
                              })
                ], style={"padding-top": "0rem",
                           "padding-bottom": "0rem",
                           "padding-left": "0rem",
                           "padding-right": "0rem",
                         "stripped": True,    
                           "no_gutters": True,
                             })



row1zmfirst = html.Tr([
                html.Td(menosnamezm1, 
                      style={ "color": "red",
                          "font-size": ".5em",
                          #"font-family": "Arial",
                            "width":"14rem",
                             "textAlign": "right",
                            "padding-top": "0rem",  
                            "padding-bottom": "0rem",
                                          "padding-left": "0rem",
                                          "padding-right": "0rem",
                              }),
                html.Td(f"{int(menosvaluezm1):,}",
                         style={"color": "black",
                             "font-size": ".5em",
                                "margin-left":".5em",
                            "width":"2rem",
                            "padding-top": "0rem",  
                            "padding-bottom": "0rem",
                            "padding-right": "0rem",
                              }),
                 html.Td( [(menosvaluezm1_p),"%"], 
                        style={ "color": "red",
                            "font-size": ".5em",
                            "width":"1rem",
                            "padding-top": "0rem",   
                            "padding-bottom": "0rem",
                                          "padding-right": "0rem",
                              })], style={"padding-top": "0rem",
                                          "padding-bottom": "0rem",
                                          "padding-left": "0rem",
                                          "padding-right": "0rem",
                                          "no_gutters": True,
                                            })
row2 = html.Tr([html.Td(menosnamezm2, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(menosvaluezm2):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(menosvaluezm2_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row3 = html.Tr([html.Td(menosnamezm3, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(menosvaluezm3):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(menosvaluezm3_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row4 = html.Tr([html.Td(menosnamezm4, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(menosvaluezm4):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(menosvaluezm4_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row5 = html.Tr([html.Td(menosnamezm5, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(menosvaluezm5):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(menosvaluezm5_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row6 = html.Tr([html.Td(menosnamezm6, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(menosvaluezm6):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(menosvaluezm6_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row7 = html.Tr([html.Td(menosnamezm7, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(menosvaluezm7):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(menosvaluezm7_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row8 = html.Tr([html.Td(menosnamezm8, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(menosvaluezm8):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(menosvaluezm8_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row9 = html.Tr([html.Td(menosnamezm9, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(menosvaluezm9):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(menosvaluezm9_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

row10 = html.Tr([html.Td(menosnamezm10, 
                      style={"color": "black","font-size": ".5em","width":"14rem","textAlign":
                             "right","padding-top": "0rem",  "padding-bottom": "0rem",
                             "padding-left": "0rem","padding-right": "0rem",}),
                html.Td(f"{int(menosvaluezm10):,}",
                         style={"color": "black","font-size": ".5em","margin-left":".5em",
                                "width":"2rem","padding-top": "0rem",  "padding-bottom": "0rem",
                                "padding-right": "0rem",}),
                 html.Td( [(menosvaluezm10_p),"%"], 
                        style={"color": "black","font-size": ".5em","width":"1rem","padding-top": "0rem",
                               "padding-bottom": "0rem","padding-right": "0rem",})
               ], style={"padding-top": "0rem","padding-bottom": "0rem","padding-left": "0rem",
                          "padding-right": "0rem","no_gutters": True,
                            })

table_body2 = [html.Tbody([row0title, row1zmfirst,
                          row2, row3, row4,row5, row6, row7, row8, row9, row10 
], style={
          "padding-top": "0rem",
          "padding-bottom": "0rem",
          "padding-left": "0em",
          "padding-right": "0em",
          "no_gutters": True})]

############################################################################ MAPAS
mapas= pd.read_csv("https://raw.githubusercontent.com/fdealbam/0entrada/main/diccionario_mapas.csv", encoding= "UTF-8")

#_______mapas (MAS+)_filtro
masmapa1_pre=mapas[mapas.NAME_ZM == masnamezm1]
masmapa2_pre=mapas[mapas.NAME_ZM == masnamezm2]
masmapa3_pre=mapas[mapas.NAME_ZM == masnamezm3]

#_______mapas (MENOS-)_filtro
menosmapa1_pre=mapas[mapas.NAME_ZM == menosnamezm1]
menosmapa2_pre=mapas[mapas.NAME_ZM == menosnamezm2]
menosmapa3_pre=mapas[mapas.NAME_ZM == menosnamezm3]

#_______mapas (MAS+)_id-url
masmapa1 = masmapa1_pre.iloc[0]['URL_PATH']
masmapa2 = masmapa2_pre.iloc[0]['URL_PATH']
masmapa3 = masmapa3_pre.iloc[0]['URL_PATH']
#_______mapas (MENOS-)_id-url
menosmapa1 = menosmapa1_pre.iloc[0]['URL_PATH']
menosmapa2 = menosmapa2_pre.iloc[0]['URL_PATH']
menosmapa3 = menosmapa3_pre.iloc[0]['URL_PATH']


#####################################################################################################################

buttonsmas = html.Div([
 
  
  html.Br(),
  html.Br(),
    #titulo variable

#   html.P("PISO DE TIERRA", style={"margin-left":"110px","font-size": "25px", "font-family": "Arial Black",
#                                  "color": "gray"}),
#  html.Hr(style={'borderWidth': "0.3vh", "width": "50%", 
#                 "color": "#1B5244", "margin-left":"10px","margin-right":"200px","margin-top":"-20px"}),
#   
    #subtitulo
 #  html.P("CON ", 
 #          style={"margin-left":"110px","font-size": "25px", "font-family": "Arial Black",
 #                                  "color": "brown","margin-top":"1px"},
 #          ),
   html.P(
       "%s"%(descriptor),
             style={"margin-left":"110px","font-size": "25px", "font-family": "Arial Black", "margin-top":"0px", "color": "#A52A2A"}),
    
   html.Hr(style={'borderWidth': "0.3vh", "width": "50%", 
                 "color": "#1B5244", "margin-left":"10px","margin-right":"200px","margin-top":"0px"}),



  html.P(" Las 10 con", 
                    style={#"text-transform": "lowercase",
                           'backgroundColor': 'beige',
                        "color": "gray", 
                               "font-size": "16px",
                               "font-weight": 'bold',
                         "width": "31em",
                        'margin-left': '110px',
                          }),
     html.P("más", 
                    style={#"text-transform": "lowercase",
                           'backgroundColor': 'beige',
                        "color": "black", "font-family": "Arial Black",
                               "font-size": "16px",
                               "font-weight": 'bold',
                         "width": "21em",
                        'margin-left': '205px', "margin-top":"-41px"
                          }),
    #1dobotón 
    dbc.Button([dbc.Table(table_body), 
          ],style={ 'backgroundColor': 'white',
                   "font-size": "1.5em",
                  'margin-left': '10px',
                   "width": "18em",
                   "height": "14em",  
                   
                 } ,disabled=True),

    
    #2dobotón 
    #los tres mapas 
    dbc.Button(([
                            dbc.CardImg(src="%s?raw=true"%(masmapa1),
                                        style={"width": "110px", 
                                                'margin-left': '-50px',
                                                'margin-top': '-25px',
                                               }),
                            html.Br(),
                            dbc.CardImg(src="%s?raw=true"%(masmapa2),
                                        style={"width": "110px", 
                                                'margin-left': '-50px',
                                               }),
                            html.Br(),
                            dbc.CardImg(src="%s?raw=true"%(masmapa3),
                                        style={"width": "110px", 
                                                'margin-left': '-50px',
                                               }),
                ]), style={'margin-left': '.74em',
                  'height': '24em',
                  'width': '7em',
                          }, disabled=True),
    
    #3dobotón 
    #las tres zm más
    dbc.Col(dbc.Button(([ 
                             html.P((masnamezm1), 
                                    style={"font-size":"1em",
                                           "color": "green",
                                          "margin-top":"-2em",
                                          "margin-left":"-1.4em"}),
                             html.P(f"{int(masvaluezm1):,}", 
                                    style={"font-size":".8em",
                                           "color": "#878f99",
                                           "margin-top": "-2em",
                                           "margin-left":"-1.4em"
                                          }),
                             html.P([(masvaluezm1_p),"%"], 
                                        style={"font-size":"1.8em",
                                               "textAlign": "right",
                                           "margin-top": "-1.6em",
                                           "margin-left":"-1.4em",
                                             "color": "green",    
                                          }),

  html.Br(),
  html.Br(),
  html.Br(),
        
                             html.P((masnamezm2), 
                                    style={"font-size":"1em",
                                           "color": "#878f99",
                                          "margin-top":"-2em",
                                          "margin-left":"-1.4em"}),
                             html.P(f"{int(masvaluezm2):,}", 
                                    style={"font-size":".8em",
                                           "color": "#878f99",
                                           "margin-top": "-2em",
                                           "margin-left":"-1.4em"
                                          }),
                             html.P([(masvaluezm2_p),"%"], 
                                        style={"font-size":"1.8em",
                                               "textAlign": "right",
                                           "margin-top": "-1.6em",
                                           "margin-left":"-1.4em",
                                             "color": "gray",    
                                          }),

  html.Br(),
  html.Br(),
        
                             html.P((masnamezm3), 
                                    style={"font-size":"1em",
                                           "color": "#878f99",
                                          "margin-top":"-1em",
                                          "margin-left":"-1.4em"}),
                             html.P(f"{int(masvaluezm3):,}", 
                                    style={"font-size":".8em",
                                           "color": "#878f99",
                                           "margin-top": "-2em",
                                           "margin-left":"-1.4em"
                                          }),
                             html.P([(masvaluezm3_p),"%"], 
                                        style={"font-size":"1.8em",
                                               "textAlign": "right",
                                           "margin-top": "-1.6em",
                                           "margin-left":"-1.4em",
                                             "color": "gray",    
                                          }),

                ]),style={"margin-top":"-300px",
                          "margin-left": "37em",
                          'height': '24em',
                          'width': '13em',
                          "textAlign": "left",
                                      })),
      ])
       
############################################################################################
    
buttonsmenos = html.Div([
 
  html.Br(),
  html.Br(),
    
    #nueva edición 
  html.P(" Las 10 con ", 
                    style={#"text-transform": "lowercase",
                           'backgroundColor': 'navajowhite',
                        "color": "gray", 
                               "font-size": "16px",
                               "font-weight": 'bold',
                               "width": "31em",
                               'margin-left': '110px',
                          }),
    
      html.P("menos ", 
                    style={#"text-transform": "lowercase",
                           #'backgroundColor': 'navajowhite',
                        "color": "black", "font-family": "Arial Black",
                               "font-size": "16px",
                               "font-weight": 'bold',
                             #  "width": "21em",
                               'margin-left': '205px',
                           "margin-top":"-41px",
                          }),
    
    #2dobotón 
    dbc.Button([dbc.Table(table_body2), 
          ],style={ 'backgroundColor': 'white',
                   "font-size": "1.5em",
                  'margin-left': '10px',
                   "width": "18em",
                   "height": "14em",  
                 } ,disabled=True),

    
    
    #los tres mapas 
    dbc.Button(([
                            dbc.CardImg(src="%s?raw=true"%(menosmapa1),
                                        style={"width": "110px", 
                                                'margin-left': '-50px',
                                                'margin-top': '-25px',
                                               }),
            
                            html.Br(),
                            dbc.CardImg(src="%s?raw=true"%(menosmapa2),
                                        style={"width": "110px", 
                                                'margin-left': '-50px',
                                               }),
                            html.Br(),
                            dbc.CardImg(src="%s?raw=true"%(menosmapa3),
                                        style={"width": "110px", 
                                                'margin-left': '-50px',
                                               }),
                
            ]), style={'margin-left': '.74em',
                          'height': '24em',
                          'width': '7em',
        
                          }, disabled=True),
    
    #las tres zm más
    dbc.Col(dbc.Button(([ 
                             html.P((menosnamezm1), 
                                    style={"font-size":"1em",
                                           "color": "red",
                                          "margin-top":"-2em",
                                          "margin-left":"-1.4em"}),
                             html.P(f"{int(menosvaluezm1):,}", 
                                    style={"font-size":".8em",
                                           "color": "#878f99",
                                           "margin-top": "-2em",
                                           "margin-left":"-1.4em"
                                          }),
                             html.P([(menosvaluezm1_p),"%"], 
                                        style={"font-size":"1.8em",
                                               "textAlign": "right",
                                           "margin-top": "-1.6em",
                                           "margin-left":"-1.4em",
                                             "color": "red",    
                                          }),

  html.Br(),
  html.Br(),
  html.Br(),
        
                             html.P((menosnamezm2), 
                                    style={"font-size":"1em",
                                           "color": "#878f99",
                                          "margin-top":"-2em",
                                          "margin-left":"-1.4em"}),
                             html.P(f"{int(menosvaluezm2):,}", 
                                    style={"font-size":".8em",
                                           "color": "#878f99",
                                           "margin-top": "-2em",
                                           "margin-left":"-1.4em"
                                          }),
                             html.P([(menosvaluezm2_p),"%"], 
                                        style={"font-size":"1.8em",
                                               "textAlign": "right",
                                           "margin-top": "-1.6em",
                                           "margin-left":"-1.4em",
                                             "color": "gray",   
                                               
                                          }),

  html.Br(),
  html.Br(),
        
                             html.P((menosnamezm3), 
                                    style={"font-size":"1em",
                                           "color": "#878f99",
                                          "margin-top":"-1em",
                                          "margin-left":"-1.4em"}),
                             html.P(f"{int(menosvaluezm3):,}", 
                                    style={"font-size":".8em",
                                           "color": "#878f99",
                                           "margin-top": "-2em",
                                           "margin-left":"-1.4em"
                                          }),
                             html.P([(menosvaluezm3_p),"%"], 
                                        style={"font-size":"1.8em",
                                               "textAlign": "right",
                                           "margin-top": "-1.6em",
                                           "margin-left":"-1.4em",
                                             "color": "gray",    
                                          }),

                ]),style={"margin-top":"-300px",
                          "margin-left": "37em",
                          'height': '24em',
                          'width': '13em',
                          "textAlign": "left",
                          
                  #"box-shadow": "20px 40px 60px gray",
                         },disabled=True)),
     #fuente
     html.P("Censo Nacional de Población y Vivienda, 2020",
                    style={#"text-transform": "lowercase",
                           "font-style": "italic",
                          
                        "color": "gray", 
                               "font-size": "9px",
                               "font-weight": 'bold',
                               "width": "31em",
                               'margin-left': '130px',
                          }),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row([
    dbc.Col(html.P("Análisis de la variable"),        
                   style={"margin-left": "9em","font-size": "12px", "font-family": "Arial Black", "color": "#A52A2A"}),        
             ], justify="start",),
    dbc.Row([
        dbc.Col(html.P(bulletmas_p),
               width={'size': 5, 'offset': 1}, 
                style={"margin-left": "13em", "margin-bottom": "-1em",
                                                      "font-size": "8px",}),
               ], justify="start",),
    
    dbc.Row([
        dbc.Col(html.P(bulletmas),
               width={'size': 5, 'offset': 1}, style={"margin-left": "13em", "margin-bottom": "-1em",
                                                      "font-size": "8px",}),
               ], justify="start",),
    
    dbc.Row([
        dbc.Col(html.P(bulletmenos_p),
               width={'size': 5, 'offset': 1}, style={"margin-left": "13em", "margin-bottom": "-1em",
                                                      "font-size": "8px",}),
               ], justify="start",),
    
    dbc.Row([
        dbc.Col(html.P(bulletmenos),
               width={'size': 5, 'offset': 1}, style={"margin-left": "13em", "margin-bottom": "-1em",
                                                      "font-size": "8px",}),
               ], justify="start",),
    
    html.Br(),
    html.Br(),
    
    #fuente
    
    
   #    dbc.Button(
   #             html.Span(["", html.H1(className="fas fa-home", style={"color": "lightblue",
   #                                                                    'margin-left': '530px',
   #                                                                  }),
   #                          ]),),
     html.P("Zonas metropolitanas",
                    style={#"text-transform": "lowercase",
                          # "font-style": "italic",
                       
                        "color": "lightblue", 
                               "font-size": "14px",
                           
                               "width": "31em",
                               'margin-left': '510px',
                          }),
    
     html.Hr(style={'borderWidth': "0.3vh", "width": "12%", 
                  "color": "#1B5244", "margin-left":"510px","margin-right":"200px", "margin-top":"-15px"}),
    
    html.P("Variables de",
                    style={#"text-transform": "lowercase",
                          # "font-style": "italic",
                          "margin-top":"-15px",
                        "color": "lightblue", 
                               "font-size": "14px",
                           
                               "width": "31em",
                               'margin-left': '510px',
                          }),
    html.P("%s"%(tema),
                    style={#"text-transform": "lowercase",
                          #"font-style": "italic",
                          "margin-top":"-36px",
                        "color": "#ff8c00", 
                               "font-size": "14px",
                               "font-weight": 'bold',
                               "width": "31em",
                               'margin-left': '605px',
                          }),
 
        
    
])
    
########################################################################
# A P P 
########################################################################

FONT_AWESOMEpro1 = "{% static 'fontawesome_pro/js/all.min.js' %}"
FONT_AWESOMEpro = "{% static 'fontawesome_pro/css/all.min.css' %}"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
server = flask.Flask(__name__)    
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. 
                                                #CERULEAN, 
                                                #COSMO, 
                                                #CYBORG, 
                                                #DARKLY, 
                                                #FLATLY, 
                                                #JOURNAL, 
                                                #LITERA, 
                                                #LUMEN, #SIRVE 
                                                LUX, 
                                                #MATERIA, 
                                                #MINTY, 
                                                #PULSE, 
                                                #SANDSTONE, #SIRVE 
                                                #SIMPLEX, 
                                                #SKETCHY, 
                                                #SLATE, 
                                                #SOLAR, 
                                                #SPACELAB, 
                                                #SUPERHERO, 
                                                #uNITED, 
                                                #YETI, 
                                                FONT_AWESOMEpro1,
                                                FONT_AWESOME, 
                                                FONT_AWESOMEpro], server=server)

app.layout = html.Div(
    [buttonsmas,
     buttonsmenos
      ], 
            style={
            'margin-top': '0px',
            'margin-left': '5px',
            'width': '1400px',
            'height': '1413px',
            'backgroundColor': 'white'
            },)


if __name__ == '__main__':
    app.run_server(use_reloader = False)
 


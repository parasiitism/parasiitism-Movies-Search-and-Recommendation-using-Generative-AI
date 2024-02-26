import os
import random
import numpy as np
import streamlit as st
import torch


def seed_everything(seed: int):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = True


def streamlit_header_and_footer_setup():
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)

    st.markdown("""
        <style>
        .navbar-nav{
            display: flex;
            flex-direction: row;
        }
        @media only screen and (max-width: 525px) {
            nav{
                flex-direction: column !important;
                gap: 15px !important;
            }
        }
        </style>
        <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #000; justify-content:space-between;">
            <a href="https://github.com/parasiitism" target="_blank"><svg width="144" height="80" viewBox="0 -10 144 80" fill="none" xmlns="http://www.w3.org/20001/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.77562 14.2897C8.4216 14.2897 9.70659 14.2543 11.4828 13.523C13.5526 12.6708 17.6705 11.1239 20.6411 9.53491C22.7187 8.42355 23.6293 6.95369 23.6293 4.97427C23.6294 2.22707 21.4024 0 18.6551 0H7.14487C3.19886 0 0 3.19886 0 7.14487C0 11.0909 2.99508 14.2897 7.77562 14.2897Z" fill="#355146"/>
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M9.72217 19.2123C9.72217 17.2781 10.8866 15.5341 12.6731 14.7926L16.298 13.2882C19.9645 11.7665 24.0001 14.461 24.0001 18.4308C24.0001 21.5064 21.5064 23.9995 18.4308 23.9986L14.5062 23.9976C11.8638 23.9969 9.72217 21.8547 9.72217 19.2123Z" fill="#D18EE2"/>
                    <path d="M4.11881 15.229H4.11874C1.84402 15.229 0 17.073 0 19.3477V19.8812C0 22.1559 1.84402 24 4.11874 24H4.11881C6.39353 24 8.23755 22.1559 8.23755 19.8812V19.3477C8.23755 17.073 6.39353 15.229 4.11881 15.229Z" fill="#FF7759"/>
                    </g>
                    </svg></a>
            <div style="justify-content: flex-end;">
                <ul class="navbar-nav">
                    <li>
                        <a class="nav-link text-white" href="https://github.com/parasiitism" style="background: #917EF3; border-radius: 100px; padding-left: 15px; padding-right: 15px;">Welcome</a>
                    </li>
                    <li>
                        <a class="nav-link text-white" href="https://github.com/parasiitism" target="_blank">Please jump on Github →</a>
                    </li>
                </ul>
            </div>
        </nav>
    """,
                unsafe_allow_html=True)

    hide_st_style = """
        <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:'Welcome on my';
                visibility: visible;
                display: block;
                position: relative;
                #background-color: red;
                padding: 5px;
                top: 2px;
            }
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)
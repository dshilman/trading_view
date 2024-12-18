import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

def get_info_widget(
        ticker: str = "AAPL",
        theme: str = "dark",   
    ):
    
    width = 1000
    height = 200
    
    header = '''
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
    '''
    
    footer = '''
        </script>
        </div>
    '''
    
    widget = {
      "symbol": ticker,
      "height": height,
      "width": width,
      "locale": "en",
      "colorTheme": theme,
      "isTransparent": False
    }
    
    widget = (
        str(widget)
        .replace('True', 'true')
        .replace('False', 'false')
        .replace('\'', '"')
    )
    
    return (
        header + widget + footer,
        width,
        height,
    )

def get_chart_widget(
        ticker: str = "AAPL",
        theme: str = "dark",    
    ):
    
    height = 600
    width = 1000
    
    header = '''
      <div class="tradingview-widget-container">
      <div id="technical-analysis-chart-demo"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget(
    '''
    
    footer = '''
      );
      </script>
      </div>
    '''
    
    widget = {
      "width": width, 
      "height": height,
      "symbol": ticker,
      "interval": "D",
      "timezone": "exchange",
      "theme": theme,
      "style": "1",
      "withdateranges": True,
      "hide_side_toolbar": False,
      "allow_symbol_change": True,
      "studies": [
        {"id": "MASimple@tv-basicstudies", "inputs": {"length": 10}},
        {"id": "MASimple@tv-basicstudies", "inputs": {"length": 20}},
      ],
      "show_popup_button": False,
      "popup_width": "1000",
      "popup_height": "650",
      "locale": "en"
    }
    
    widget = (
        str(widget)
        .replace('True', 'true')
        .replace('False', 'false')
        .replace('\'', '"')
    )
    
    return (
        header + widget + footer,
        width,
        height,
    )

def get_fundamentals(
        ticker: str="AAPL",
        theme: str="dark",
        display: str="regular",
    ):
    
    width = 400
    height = 825

    header = '''
        <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
    '''
    
    footer = '''
        </script>
        </div>
    '''
    
    widget = {
        "colorTheme": theme,
        "displayMode": display,
        "width": width,
        "height": height,
        "symbol": ticker,
        "locale": "en"
    }
    
    widget = (
        str(widget)
        .replace('True', 'true')
        .replace('False', 'false')
        .replace('\'', '"')
    )
    
    return (
        header + '\n'+ widget + '\n' + footer,
        width,
        height,
    )

st.sidebar.subheader('Chart Options')
ticker = st.sidebar.text_input('Ticker', value = "AAPL")
theme = st.sidebar.selectbox('Theme', options = ['dark', 'light'])
fund_type = st.sidebar.selectbox('Fundamental Display', options = ['regular', 'compact'])

info, info_width, info_height = get_info_widget(
    ticker=ticker,
    theme=theme,
)

chart, chart_width, chart_height = get_chart_widget(
    ticker=ticker,
    theme=theme,
)

fund, fund_width, fund_height = get_fundamentals(
    ticker=ticker,
    theme=theme,
    display=fund_type
)

col1, col2 = st.columns([3, 1])

with col1:

    components.html(
        info, 
        height=info_height, 
        width=info_width,
    )
    
    components.html(
        chart, 
        height=chart_height, 
        width=chart_width,
    )

with col2:
    components.html(
        fund, 
        height=fund_height, 
        width=fund_width,
    )

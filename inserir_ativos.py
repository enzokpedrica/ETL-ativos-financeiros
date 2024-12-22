import pandas as pd
import yfinance as yf
import criacao_db

cns, mycursor = criacao_db.conectar_banco()
mycursor.execute("USE acoes")

def inserir_ativos():
    sql = "INSERT INTO IF NOT EXISTS ativos (Ticker, Ticker_id) VALUES (%s, %s)"
    valores = [("MSFT", 1), ("AAPL" , 2) , ("NVDA", 3)]
    mycursor.executemany(sql, valores)
    cns.commit()

def atualizar_tick_historico(tick):
    ticker = yf.Ticker(tick)
    teste = ticker.history(period='1y')
    df_atual = pd.DataFrame(teste)
    df_atual = df_atual.reset_index()

    if tick == 'MSFT':
        ativo = 1
    
    elif tick == 'AAPL':
        ativo = 2
    else:
        ativo = 3

    for _, row in df_atual.iterrows():
        mycursor.execute('''
        INSERT INTO historico (Date, Open, High, Low, Close, Ativo_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        ''', (row['Date'], row['Open'], row['High'],row['Low'], row['Close'], ativo))
    cns.commit()

def atualizar_tick_diario(tick):
    try:
        ticker = yf.Ticker(tick)
        teste = ticker.history(period='1d')
        df_atual = pd.DataFrame(teste)

        df_atual = df_atual.reset_index()
        if tick == 'MSFT':
            ativo = 1
        elif tick == 'AAPL':
            ativo = 2
        else:
            ativo = 3

        for _, row in df_atual.iterrows():
            mycursor.execute('''
            INSERT INTO historico (Date, Open, High, Low, Close, Ativo_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            ''', (row['Date'], row['Open'], row['High'],row['Low'], row['Close'], ativo))
        print(f'Inserção {tick} realizada com sucesso !!!')
        cns.commit()
    except:
        print(f'erro')
        
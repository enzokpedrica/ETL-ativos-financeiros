import inserir_ativos
import criacao_db

try:

    # TALVEZ MELHORAR ISSO AQUI, PRECISA EXECUTAR TODA HORA????
    cns, mycursor = criacao_db.conectar_banco()
    criacao_db.criar_database(cns, mycursor)

    criacao_db.criar_tabelas(cns, mycursor)


#BUILDING ---------------------
    # df_1 = criacao_db.obter_dados(cns)
    # print(df_1[df_1["Ativo_id"]==2])
#BUILDING ---------------------
    

    print(" -- PROGRAMA DE ATUALIZAÇÃO -- ")
    print("Qual ativo deseja escolher para hoje?")
    print("""
    [1] - Microsoft - MSFT
    [2] - Apple - AAPL
    [3] - Nvidia - NVDA
    [4] - Atualizar todas
    """)
    resposta_acao = int(input("Digite sua resposta: "))
    

    print(" -- Deseja qual tipo de inserção? -- ")
    print("""
    [1] - Histórico
    [2] - Diário
    """)
    resposta_periodo = int(input("Digite sua resposta: "))

    if resposta_periodo == 1:
        if resposta_acao == 1:
            inserir_ativos.atualizar_tick_historico("MSFT")
        elif resposta_acao == 2:
            inserir_ativos.atualizar_tick_historico("AAPL")
        elif resposta_acao == 3:
            inserir_ativos.atualizar_tick_historico("NVDA")
        elif resposta_acao == 4:
            inserir_ativos.atualizar_tick_historico("MSFT")
            inserir_ativos.atualizar_tick_historico("AAPL")
            inserir_ativos.atualizar_tick_historico("NVDA")
        else:
            print("TICKER INCORRETO")

    elif resposta_periodo == 2:
        if resposta_acao == 1:
            inserir_ativos.atualizar_tick_diario("MSFT")
        elif resposta_acao == 2:
            inserir_ativos.atualizar_tick_diario("AAPL")
        elif resposta_acao == 3:
            inserir_ativos.atualizar_tick_diario("NVDA")
        elif resposta_acao == 4:
            inserir_ativos.atualizar_tick_diario("MSFT")
            inserir_ativos.atualizar_tick_diario("AAPL")
            inserir_ativos.atualizar_tick_diario("NVDA")
        else:
            print("TICKER INCORRETO")
    else:
        print("PERÍODO NÃO IDENTIFICADO")

finally:
    # Encerrar conexão
    mycursor.close()
    cns.close()
    print("Conexão encerrada.")
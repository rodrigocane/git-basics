df_comp = df.copy()
df_comp = df_comp.merge(tabela_notas_fiscais, on=['NotaFiscal'])
df_comp = df_comp.merge(tabela_precos, on=['NomeProduto'])
item_venda = df_comp.groupby(['IdNotaFiscal','IdProduto']).agg(
    Qtde=('Qtde','sum'),ValorTotal=('ValorLiquido','sum')
).reset_index()

item_venda
with pd.ExcelWriter('vendas.xlsx', engine='xlsxwriter') as writer:
  tabela_clientes.to_excel(writer, sheet_name='Clientes')
  tabela_valor_total.to_excel(writer, sheet_name='Vendas')
  tabela_precos.to_excel(writer, sheet_name='Produtos')
  item_venda.to_excel(writer, sheet_name='VendasProdutos')
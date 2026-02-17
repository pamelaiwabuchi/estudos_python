from calculadora_de_tarifas import calcular_tarifas

# 2. Teste de limites (Edge Cases)
# Testamos o que acontece se o usuário digitar valores que não deveriam existir.

def test_tempo_invalido():
    #Verifica se números negativos ou zero retornam a mensagem de erro
    assert calcular_tarifas(0, "NÃO") == "Tempo inválido"
    assert calcular_tarifas(-1, "NÃO") == "Tempo inválido"

# 3. Teste da Regra Base (Até 1 hora)
def test_tarifa_minima():
    assert calcular_tarifas(1, "NÃO") == 5.0

#4. Teste da Regra de Adicional (2 a 4 horas)
def test_tarifa_adicional():
    # Exemplo: 3 horas. 
    # 1ª hora (5.00) + 2 horas adicionais (2 * 3.00 = 6.00) = 11.00
    assert calcular_tarifas(3, "NÃO") == 11.0

# 5. Teste da Tarifa Diária (Acima de 4 horas)
def test_tarifa_diaria():
# Qualquer valor acima de 4 deve retornar 15.00
    assert calcular_tarifas(5, "NÃ0") == 15.0
    assert calcular_tarifa(10, "NÃO") == 15.0

# 6. Teste da Lógica do Cupom
def test_aplicacao_cupom():
    # 1 hora com cupom: 5.00 - 2.00 = 3.00
    assert calcular_tarifas(1, "SIM") == 3.0
    # Testamos se o .upper() que você colocou funciona (Sim minúsculo)
    assert calcular_tarifas(1, "sim") == 3.0

# 7. Teste de Proteção (Valor nunca menor que zero)
def test_valor_nao_negativo():
    # Se por algum erro a conta desse negativa, o max(0, valor) deve proteger
    # Aqui simulamos uma entrada que poderia causar erro se não houvesse proteção
    resultado = calcular_tarifas(0.1, "SIM")
    assert resultado >= 0 
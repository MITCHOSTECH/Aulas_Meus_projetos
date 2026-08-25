try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except Exception as erro:
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    print("Não é possível dividir um número por Zero!")
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultafo é {r:.2f}')
finally:
    print('volte sempre! Obrigado')
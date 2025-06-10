def set_initial_participant_id_counter():
    """
    Ajusta o contador de ID do participante após carregar dados (ex: de mock data).
    Isso garante que novos IDs gerados automaticamente não entrem em conflito
    com IDs já existentes, começando do maior ID + 1.
    """
    global next_participant_id_num # Eu digo: "Ei, vou mexer no contador de crachás que está lá fora!"

    # participants_data é o seu "caderno" onde estão registrados todos os crachás e seus donos.
    # Ele verifica: "Tem algum crachá registrado nesse caderno?"
    if participants_data: # Se o caderno NÃO ESTIVER vazio (tem participantes)
        max_id_num = 0 # Guarda o maior número de crachá que eu encontrei até agora. Começa em zero.

        # "Agora, vou olhar crachá por crachá no caderno..."
        for p_id in participants_data.keys(): # Por exemplo, 'P001', 'P002', 'P006'
            try:
                # "Para cada crachá, eu tento tirar a letra 'P' e converter o resto para um número."
                # Exemplo: 'P006'
                # p_id.startswith('P'): "Começa com 'P'?" -> Sim!
                # p_id[1:]: "Pego o resto do crachá, que é '006'."
                # .isdigit(): "É tudo número?" -> Sim!
                if p_id.startswith('P') and p_id[1:].isdigit():
                    num_part = int(p_id[1:]) # Converte '006' para o número 6

                    # "Esse número que acabei de ver (6) é maior que o maior que já vi (0)? Sim!"
                    if num_part > max_id_num:
                        max_id_num = num_part # Então, o maior número que vi agora é 6.

            except ValueError:
                # Se eu encontrar um crachá "malfeito" (tipo "ABC" ou "P-XYZ"), eu ignoro.
                pass

        # Depois de olhar todos os crachás...
        # "O maior número de crachá que encontrei foi 6. Então, o próximo crachá que eu posso entregar
        # tem que ser o 6 + 1 = 7."
        next_participant_id_num = max_id_num + 1

    else: # Se o caderno ESTIVER vazio (não tem nenhum participante ainda)
        # "Ah, não tem ninguém. Então, o próximo crachá é o número 1."
        next_participant_id_num = 1
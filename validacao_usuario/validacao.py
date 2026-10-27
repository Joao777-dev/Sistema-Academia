def validar_cpf(cpf_usuario):
    return cpf_usuario.isdigit() and len(cpf_usuario) == 11

def validar_nasc(data_nasc):
    return data_nasc.isdigit() and len(data_nasc) == 8

def validar_tel(tel_usuario):
    return tel_usuario.isdigit() and len(tel_usuario) == 11

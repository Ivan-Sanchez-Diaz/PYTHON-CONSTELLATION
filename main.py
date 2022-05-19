import numpy as np
import matplotlib.pyplot as plt

inp = [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0]


def ocho_psk(inp):
    n = 3
    casos = casos_3()
    print(casos)

    x = np.arange(0, 4, 0.1)
    out = []
    for i in range(0, len(inp), n):
        la = inp[i:i+n]
        la = str(la[0])+str(la[1])+str(la[2])
        signo = 0
        grados = 0
        for n, caso in enumerate(casos):
            if n > 3:
                signo = 1
            elif n < 3:
                signo = -1

            if caso == la:
                print(la + " == " + caso)
                if caso == "000" or caso == "100":
                    grados = 112.5 * signo
                    print("grados = " + str(grados))
                    y = 2*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                if caso == "001" or caso == "101":
                    grados = 157.5 * signo
                    print("grados = " + str(grados))
                    y = 2*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                if caso == "010" or caso == "110":
                    grados = 67.6 * signo
                    print("grados = " + str(grados))
                    y = 2*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                if caso == "011" or caso == "111":
                    grados = 22.5 * signo
                    print("grados = " + str(grados))
                    y = 2*np.sin(2*x+np.deg2rad(np.deg2rad(grados)))
                    for i in y:
                        out.append(i)
    return out


def ocho_qam(inp):
    x = np.arange(0, 4, 0.1)
    out = []
    n = 3
    casos = casos_3()
    print(casos)
    for i in range(0, len(inp), n):
        la = inp[i:i+n]
        la = str(la[0])+str(la[1])+str(la[2])
        for n, caso in enumerate(casos):
            amplitud = 0
            if n % 2 == 0:
                amplitud = 0.765
            else:
                amplitud = 1.848
            if caso == la:
                print(la + " == " + caso)
                if n == 0 or n == 1:
                    grados = -135
                    y = amplitud*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                elif n == 2 or n == 3:
                    grados = -45
                    y = amplitud*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                elif n == 4 or n == 5:
                    grados = 135
                    y = amplitud*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                elif n == 6 or n == 7:
                    grados = 45
                    y = amplitud*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                print("grados = " + str(grados))
    return out


def dseis_psk(inp):
    x = np.arange(0, 4, 0.1)
    out = []
    n = 4
    casos = casos_4()
    print(casos)
    for i in range(0, len(inp), n):
        la = inp[i:i+n]
        la = str(la[0])+str(la[1])+str(la[2])+str(la[3])
        grados = 11.25
        for n, caso in enumerate(casos):
            if n != 0:
                grados = grados + 22.5
            if caso == la:
                y = 2*np.sin(2*x+np.deg2rad(grados))
                for i in y:
                    out.append(i)
                print(la + " == " + caso)
                print("grados = " + str(grados))
    return out


def dseis_qam(inp):
    n = 4
    casos = casos_4()
    print(casos)
    x = np.arange(0, 3, 0.1)
    out = []
    for i in range(0, len(inp), n):
        la = inp[i:i+n]
        la = str(la[0])+str(la[1])+str(la[2])+str(la[3])
        for n, caso in enumerate(casos):
            if n > 7:
                signo = 1
            elif n < 8:
                signo = -1

            if caso == "0000" or caso == "0010" or caso == "1000" or caso == "1010":
                amplitud = 0.311
            elif caso == "0001" or caso == "0011" or caso == "0100" or caso == "0110" or caso == "1001" or caso == "1011" or caso == "1110" or caso == "1100":
                amplitud = 0.850
            elif caso == "0101" or caso == "0111" or caso == "1101" or caso == "1111":
                amplitud = 1.161

            if caso == la:
                print(la + " == " + caso)
                if caso == "0000" or caso == "0101" or caso == "1000" or caso == "1101":
                    grados = 135 * signo
                    y = amplitud*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                    print("grados = " + str(grados))
                elif caso == "0001":
                    grados = 165 * signo
                    y = amplitud*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                    print("grados = " + str(grados))
                elif caso == "0010" or caso == "0111" or caso == "1010" or caso == "1111":
                    grados = 45 * signo
                    y = amplitud*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                    print("grados = " + str(grados))
                elif caso == "0011" or caso == "1011":
                    grados = 15 * signo
                    y = amplitud*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                    print("grados = " + str(grados))
                elif caso == "0100" or caso == "1100":
                    grados = 105 * signo
                    y = amplitud*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                    print("grados = " + str(grados))
                elif caso == "0110" or caso == "1110":
                    grados = 75 * signo
                    y = amplitud*np.sin(2*x+np.deg2rad(grados))
                    for i in y:
                        out.append(i)
                    print("grados = " + str(np.deg2rad(grados)))
    return out


def casos_4():
    cases = []
    binario = -1
    for i in range(0, 16):
        binario = suma_binaria(binario, 1)
        if len(binario) == 1:
            caso = "000" + str(binario)
        if len(binario) == 2:
            caso = "00" + str(binario)
        if len(binario) == 3:
            caso = "0" + str(binario)
        if len(binario) == 4:
            caso = str(binario)
        cases.append(caso)
    return cases


def casos_3():
    cases = []
    binario = -1
    for i in range(0, 8):
        binario = suma_binaria(binario, 1)
        if len(binario) == 1:
            caso = "00" + str(binario)
        if len(binario) == 2:
            caso = "0" + str(binario)
        if len(binario) == 3:
            caso = str(binario)
        cases.append(caso)
    return cases


def suma_binaria(a, b):
    intNum = int(str(a), 2) + int(str(b), 2)
    return bin(intNum)[2:]


final = dseis_qam(inp)
x = np.arange(0, 3.5, 0.1)
y = 0.311*np.sin(2*x+np.deg2rad(-135))
plt.plot(final)
plt.show()

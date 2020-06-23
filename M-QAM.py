'''
@Author: Mu Yifan Yvonne
@Date: 2020-03-04 16:58:09
@LastEditTime: 2020-06-23 17:32:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \\M-QAM\\M-QAM.py
'''
import numpy as np
import time


def bi2de(binary):
    # 与matlab bi2de函数功能相同
    # 将二进制数组转化为十进制数
    # 二进制数组内从右向左读
    bin_temp = 0
    bin_res = np.zeros(len(binary), dtype=int)
    for i in range(len(binary)):
        for j in range(len(binary[i])):
            bin_temp = bin_temp + binary[i][j] * (2 ** j)
        bin_res[i] = bin_temp
        bin_temp = 0
    return bin_res


def GetSquareConstellation(M):
    # 获得星座图分布
    ini_phase = 0  # 初始相位
    nbits = np.log2(M)  # 
    if nbits == 3:
        # 8-QAM
        constellation = np.array([-3 + 1j, -3 - 1j, -1 + 1j, -1 - 1j, 1 + 1j, 1 - 1j, 3 + 1j, 3 - 1j])
    else:
        # Square QAM
        sqrtM = int(2 ** (nbits / 2))

        x = np.arange(-(sqrtM - 1), sqrtM, 2)
        y = np.arange(sqrtM - 1, -sqrtM, -2).reshape(-1, 1)
        constellation = x + y * 1j
        constellation = (constellation * np.exp(1j * ini_phase)
                         ).reshape(constellation.size, order='F')
    return constellation


def QuadratureAmplitudeModulation(x, M):
    if(x == np.array([])):
        return print('QAM Input Empty')
    else:
        y = np.array([])
        constellation = GetSquareConstellation(M)
        print(constellation)
        for i in x:
            y = np.append(y, constellation[i])
    return y


time_start = time.time()  # 程序开始计时
# number of symbol
N = 8
# number of subcarriers
M = 8
# size of constellation
M_mod = 4
M_bits = int(np.log2(M_mod))
# number of symbols per frame
N_syms_perfram = N * M
# number of bits per frame
N_bits_perfram = N * M * M_bits

# random input bits generation
data_info_bit = np.random.randint(0, 2, N_bits_perfram)
data_temp = bi2de(np.reshape(data_info_bit, (N_syms_perfram, M_bits), order='F'))  # 'F'和matlab中的相同
y = QuadratureAmplitudeModulation(data_temp, M_mod)
print(y)

time_end = time.time()  # 结束计时
time_cost = time_end - time_start  # 运行所花时间
print('time cost:', time_cost, 's')

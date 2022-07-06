
# File:      hw3_3.py
# Author(s): Xiongyu Chen

input = open('cme.20210709.c.pa2', 'rt', encoding='utf-8')
output = open('CL_and_NG_expirations_and_settlements.txt', 'wt', encoding='utf-8')


def writeline(line):
    output.write(line + '\n')


writeline('{:<10s}{:<11s}{:<11s}{:<12s}{:<10s}{:<7s}'.format(
    'Futures', 'Contract', 'Contract', 'Futures', 'Options', 'Options'))
writeline('{:<10s}{:<11s}{:<11s}{:<12s}{:<10s}{:<7s}'.format(
    'Code', 'Month', 'Type', 'Exp Date', 'Code', 'Exp Date'))
writeline('{:<10s}{:<11s}{:<11s}{:<12s}{:<10s}{:<7s}'.format(
    '-' * 7, '-' * 8, '-' * 8, '-' * 8, '-' * 7, '-' * 8))

Gap = False

for line in input:
    if line[0] == 'B' and 202109 <= int(line[18:24]) <= 202312:
        if line[5:18] == 'CL        FUT':
            writeline('{:<10s}{:4s}-{:6s}{:<11s}{:4s}-{:2s}-{:2s}'.format(
                'CL', line[18:22], line[22:24], 'Fut', line[91:95], line[95:97], line[97:99]))
        elif line[5:18] == 'LO        OOF':
            writeline('{:<10s}{:4s}-{:6s}{:<23s}{:<10s}{:4s}-{:2s}-{:2s}'.format(
                'CL', line[18:22], line[22:24], 'Opt', 'LO', line[91:95], line[95:97], line[97:99]))
        elif line[5:18] == 'NG        FUT':
            writeline('{:<10s}{:4s}-{:6s}{:<11s}{:4s}-{:2s}-{:2s}'.format(
                'NG', line[18:22], line[22:24], 'Fut', line[91:95], line[95:97], line[97:99]))
        elif line[5:18] == 'ON        OOF':
            writeline('{:<10s}{:4s}-{:6s}{:<23s}{:<10s}{:4s}-{:2s}-{:2s}'.format(
                'NG', line[18:22], line[22:24], 'Opt', 'ON', line[91:95], line[95:97], line[97:99]))

    elif line[0:2] == '81' and 202109 <= int(line[29:35]) <= 202312:
        if line[15:28] == 'CL        FUT' and not Gap:
            writeline('{:<10s}{:<11s}{:<11s}{:<9s}{:<10s}'.format(
                'Futures', 'Contract', 'Contract', 'Strike', 'Settlement'))
            writeline('{:<10s}{:<11s}{:<11s}{:<9s}{:<10s}'.format(
                'Code', 'Month', 'Type', 'Price', 'Price'))
            writeline('{:<10s}{:<11s}{:<11s}{:<9s}{:<10s}'.format(
                '-' * 7, '-' * 8, '-' * 8, '-' * 6, '-' * 10))
            Gap = True
        if line[15:28] == 'CL        FUT':
            writeline('{:<10s}{:4s}-{:<6s}{:<20s}{:>7.2f}'.format(
                'CL', line[29:33], line[33:35], 'Fut', int(line[108:122]) / 100))
        elif line[5:15] == 'LO        ' and line[25:28] == 'OOF':
                if line[28] == 'C':
                    writeline('{:<10s}{:4s}-{:<6s}{:<11s}{:>6.2f}{:>10.2f}'.format(
                        'CL', line[29:33], line[33:35], 'Call', 
                        int(line[47:54]) / 100, int(line[108:122]) / 100))
                elif line[28] == 'P':
                    writeline('{:<10s}{:4s}-{:<6s}{:<11s}{:>6.2f}{:>10.2f}'.format(
                        'CL', line[29:33], line[33:35], 'Put', 
                        int(line[47:54]) / 100, int(line[108:122]) / 100))
        elif line[15:28] == 'NG        FUT':
                writeline('{:<10s}{:4s}-{:<6s}{:<20s}{:>8.3f}'.format(
                    'NG', line[29:33], line[33:35], 'Fut', int(line[108:122]) / 1e5))
        elif line[5:15] == 'ON        ' and line[25:28] == 'OOF':
                if line[28] == 'C':
                    writeline('{:<10s}{:4s}-{:<6s}{:<11s}{:>7.3f}{:>10.3f}'.format(
                        'NG', line[29:33], line[33:35], 'Call', 
                        int(line[47:54]) / 1e3, int(line[108:122]) / 1e4))
                elif line[28] == 'P':
                    writeline('{:<10s}{:4s}-{:<6s}{:<11s}{:>7.3f}{:>10.3f}'.format(
                        'NG', line[29:33], line[33:35], 'Put', 
                        int(line[47:54]) / 1e3, int(line[108:122]) / 1e4))

input.close()
output.close()

maze = {
    '00': ['01', '10'],
    '01': ['00', '11'],
    '02': ['03', '12'],
    '03': ['02', '04'],
    '04': ['03', '14'],
    '05': ['06', '15'],
    '06': ['05'],
    '07': ['08', '17'],
    '08': ['07', '09'],
    '09': ['08', '19'],

    '10': ['00', '20'],
    '11': ['01', '12'],
    '12': ['11', '02'],
    '13': ['23', '14'],
    '14': ['13', '04'],
    '15': ['05', '16'],
    '16': ['15', '26'],
    '17': ['07', '27'],
    '18': ['28'],
    '19': ['09', '29'],

    '20': ['10', '21', '30'],
    '21': ['20', '22', '31'],
    '22': ['21', '32'],
    '23': ['13', '33'],
    '24': ['25', '34'],
    '25': ['24', '35'],
    '26': ['16', '27'],
    '27': ['17', '26', '37'],
    '28': ['18', '29'],
    '29': ['19'],

    '30': ['20', '40'],
    '31': ['21'],
    '32': ['22', '42'],
    '33': ['23', '34'],
    '34': ['24', '33'],
    '35': ['25', '36', '45'],
    '36': ['35', '37'],
    '37': ['27', '36', '47'],
    '38': ['48', '39'],
    '39': ['38'],

    '40': ['30', '41'],
    '41': ['40', '51'],
    '42': ['32', '43'],
    '43': ['42'],
    '44': ['54', '45'],
    '45': ['44', '35'],
    '46': ['47'],
    '47': ['37', '46', '48'],
    '48': ['47', '38'],
    '49': ['59'],

    '50': ['51', '60'],
    '51': ['50', '41'],
    '52': ['62'],
    '53': ['54', '63'],
    '54': ['53', '44'],
    '55': ['65'],
    '56': ['66', '57'],
    '57': ['56', '67'],
    '58': ['68', '59'],
    '59': ['58', '49'],

    '60': ['61', '50'],
    '61': ['60', '62', '71'],
    '62': ['61', '52'],
    '63': ['64', '53'],
    '64': ['63', '74'],
    '65': ['55', '75'],
    '66': ['76', '56'],
    '67': ['57', '77'],
    '68': ['58', '78'],
    '69': ['79'],

    '70': ['71', '80'],
    '71': ['70', '81', '61'],
    '72': ['73', '82'],
    '73': ['72', '83'],
    '74': ['64', '75'],
    '75': ['74', '65'],
    '76': ['66', '86'],
    '77': ['67', '78'],
    '78': ['68', '77', '79'],
    '79': ['78', '69'],

    '80': ['90', '80'],
    '81': ['71'],
    '82': ['92', '72'],
    '83': ['84', '93', '73'],
    '84': ['83'],
    '85': ['86', '95'],
    '86': ['85', '76', '87'],
    '87': ['86', '97'],
    '88': ['89'],
    '89': ['88', '99'],

    '90': ['91', '80'],
    '91': ['90', '92'],
    '92': ['91', '82'],
    '93': ['94', '83'],
    '94': ['93', '95'],
    '95': ['94', '85', '96'],
    '96': ['95'],
    '97': ['87', '98'],
    '98': ['97', '99'],
    '99': ['98', '89'],
}


def solve_maze(g, start, end):

    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)

        v = p[-2:]

        if v == end:
            return p
        for x in g[v]:  # 대상 꼭짓점에 연결된 꼭짓점들 중에
            if x not in done:  # 아직 큐에 추가된 적이 없는 꼭짓점을
                qu.append(p + x)  # 이동 경로에 새 꼭짓점으로 추가하여 큐에 저장하고
                done.add(x)  # 집합에도 추가

    return "?"


print(solve_maze(maze, '50', '49'))

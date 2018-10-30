import sys
import os
import glob

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        if self.value < other.value:
            return True
        elif self.value > other.value:
            return False
        else:
            if self.key > other.key:
                return True
            else:
                return False


class Top:
    def __init__(self):
        self.STATES = {}
        self.OCCUPATIONS = {}
        self.status_index = 0
        self.state_index = 0
        self.occupation_index = 0
        self.certified_number = 0

    def header(self, line):
        header = line.split(';')
        for i in range(len(header)):
            if 'STATUS' in header[i]:
                self.status_index = i
            if ('WORKLOC1_STATE' in header[i]) or ('WORKSITE_STATE' in header[i]):
                self.state_index = i
            if 'SOC_NAME' in header[i]:
                self.occupation_index = i

    def insert(self, line):
        record = line.split(';')
        status = record[self.status_index]
        if status == 'CERTIFIED':
            self.certified_number += 1
            state, occupation = record[self.state_index], record[self.occupation_index]
            if (not occupation) or (len(state) != 2):
                return
            if occupation[0] == '"':
                occupation = occupation[1:-1]
            if state not in self.STATES:
                self.STATES[state] = 0
            self.STATES[state] += 1
            if occupation not in self.OCCUPATIONS:
                self.OCCUPATIONS[occupation] = 0
            self.OCCUPATIONS[occupation] += 1

    def get_top_10(self):
        _STATES_LIST = []
        _OCCUPATIONS_LIST = []
        for key in self.STATES:
            _STATES_LIST.append(Pair(key, self.STATES[key]))
        for key in self.OCCUPATIONS:
            _OCCUPATIONS_LIST.append(Pair(key, self.OCCUPATIONS[key]))
        _STATES_LIST = sorted(_STATES_LIST, reverse=True)
        _OCCUPATIONS_LIST = sorted(_OCCUPATIONS_LIST, reverse=True)
        top_10_state = []
        top_10_occupation = []
        for element in _STATES_LIST[:7]:
            top_10_state.append('%s;%d;%.1f%s\n' % (element.key, element.value,
                                                    100 * element.value / float(self.certified_number),
                                                    '%'))
        top_10_state.append('%s;%d;%.1f%s' % (_STATES_LIST[7].key, _STATES_LIST[7].value,
                                                    100 * element.value / float(self.certified_number),
                                                    '%'))
        for element in _OCCUPATIONS_LIST[:10]:
            top_10_occupation.append('%s;%d;%.1f%s\n' % (element.key, element.value,
                                                         100 * element.value / float(self.certified_number),
                                                         '%'))
        return top_10_state, top_10_occupation


def main():
    input_file_name = sys.argv[1]
    output_file_name_occupation = sys.argv[2]
    output_file_name_state = sys.argv[3]
    f = open(input_file_name, 'r', encoding='utf-8')
    top = Top()
    top.header(f.readline())
    while True:
        line = f.readline()
        if not line:
            break
        top.insert(line)
    f.close()
    state, occupation = top.get_top_10()
    f = open(output_file_name_state, 'w')
    for line in state:
        f.write(line)
    f.close()
    f = open(output_file_name_occupation, 'w')
    for line in occupation:
        f.write(line)
    f.close()


if __name__ == '__main__':
    main()

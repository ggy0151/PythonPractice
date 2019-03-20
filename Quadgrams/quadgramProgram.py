from math import log10

import string


def chosen_plaintext_attack(plaintext, ciphertext, bifurcation, texttodecrypt):
    answer = ''   # 해독된 텍스트
    noanswer = ''  # 딕셔너리에 없는 해독할 단어
    dictionary = {}

    for n in range(0, int(len(ciphertext) / bifurcation)):
        dictionary[ciphertext[n * bifurcation: (n + 1) * bifurcation]] = plaintext[n]
        #bifurcation만큼 자른 ciphertext를 key로, 이에 대응하는 plaintext 1글자가 value가 되는 딕셔너리 생성



    for n in range(0, int(len(texttodecrypt) / bifurcation)):
        decryptStr = texttodecrypt[n * bifurcation: (n + 1) * bifurcation]
        #texttodecrypt를 bifurcation만큼 자른 값을 decryptStr에 저장


        try:
            newStr = dictionary[decryptStr]

        except:  # 해독할 단어가 딕셔너리에 없다면
            noanswer += decryptStr + ' '

        else:  # 해독할 단어가 딕셔너리에 있다면
            answer += newStr

    if len(noanswer) == 0:
        print('해독된 텍스트:', answer)
    else:
        print('암호 해독이 중단되었습니다. 찾을 수 없는 키: ', noanswer[:-1])  # 맨 뒤 공백 제거


# 제공 함수
# file pointer 리턴 함수

def open_file():
    while True:

        fileName = input("파일 이름을 입력해 주세요: ")

        try:

            fp = open(fileName, 'r')

        except:

            print("파일을 열 수 없습니다. 다시 시도해주세요.\n")

        else:

            return fp


def log_probability_dictionary(fp):
    quadDict = {}
    totalQuadgram = 0

    for line in fp.read().split('\n'):  # 파일에 있는 line 들을 '\n'을 기준으로 자른다
        line = line.split(' ')  # 다시 공백으로 quadgram과 count를 스플릿해서 리스트를 만든다.

        # {'key': [count, 0]}
        quadDict[line[0]] = [int(line[1]), 0]  # log_probability는 현재 0, line[0]=key 이고 line[1] = count 이다.
        totalQuadgram += int(line[1])  # count 값의 총 합을 구한다

    fp.close()

    # h  log probability 값 계산해서 딕셔너리에 추가

    for key in quadDict:
        count_list = quadDict[key]
        count_list[1] = log10(count_list[0] / totalQuadgram)  # 0으로 뒀던 log_probability 계산 및 저장

    # 출력 형식

    print("\n{:<8s}{:>13s}{:>22s}".format('Quadgram', 'Count', 'Log Probability'))

    print("-------------------------------------------")
    quadBigList = []

    for key in quadDict:
        # (key, count, log)
        quadBigList.append((key, quadDict[key][0], quadDict[key][1]))  # quadBigList에 튜플형으로 자료를 추가한다.
                                  # quadDict[key][0] = count, quadDict[key][1] = log_probability

    quadBigList = sorted(quadBigList, key=lambda x: x[1])
    #튜플형 자료형은 lambda를 이용. x: x[2] 로 count의 값으로 sort() 한다고 지정함.

    quadBigList.reverse()

    for i in range(0, 10):
        item = quadBigList[i]
        print("{:<8s}{:>13d}{:>22.6f}".format(item[0], item[1], item[2]))
        # for문 돌 때마다 key, count, log_probability의 값을 출력함

    return quadDict



def bruteforce_shift_cipher(ciphertext, quadDict):

    fitness_List = []
    for key in range(0, 26):    #알파벳은 26글자 -> 범위는 0부터 25까지

        potential_plaintext = ciphertext  # potential_plaintext의 값이 shift_characters로 밀리기 전 값 즉 a로 시작할 때의 값 입력
        fitness = fitness_calculator(potential_plaintext, quadDict)


        fitness_List.append((key, potential_plaintext, fitness))
        #튜플 형태로 fitness_List에 quadDict의 key, plaintext, fitness  값을 for문 돌 때마다 추가해준다.

        ciphertext = shift_characters(ciphertext)
        #한 글자씩 ciphertext 미룸. 다음 for문 돌 때 밀린 ciphertext값이 potential_plain text 값에 들어감.

    fitness_List = sorted(fitness_List, key=lambda x: x[2])
    #튜플형 자료형은 lambda를 이용. x: x[2] 로 fitness의 값으로 sort() 한다고 지정함.

    fitness_List.reverse()

    # 출력 형식

    print("{:<5s}{:^35s}   {:>10s}".format("\nKey", "Plaintext", "Fitness"))

    print("------------------------------------------------------")
    for i in range(0, 5):
        item = fitness_List[i]
        print("{:<5d}{:<35s}   {:>10.4f}".format(item[0], item[1][0:35], item[2]))
        #for문 돌 때마다 key, potential_plaintext, fitness의 값을 출력함

    print('\n 계속하려면 엔터키를 누르세요...')
    print("\n해독된 암호문: ", fitness_List[0][1])



# 제공 함수

# 알파벳대문자 한칸씩 이동시키는 함수 ex) a -> b, b -> c, z -> a

def shift_characters(ciphertext):
    shiftedtext = ''

    for char in ciphertext:

        if ord(char) == 90:

            shiftedtext += chr(65)

        else:

            shiftedtext += chr(ord(char) + 1)

    return shiftedtext


def fitness_calculator(potential_plaintext, quadDict):
    Total_log_probability = 0

    for i in range(0, len(potential_plaintext) - 3): # -3를 안하면 범위가 넘친다.
        quadgrams = potential_plaintext[i:(i + 4)]  # 4개씩 potential_plaintext을 슬라이싱 해서 quadgram의 값을 얻는다.

        if quadgrams in quadDict.keys(): #guadgrams가 key값으로 quadDict 안에 있는지 확인한다

            log_probability = quadDict[quadgrams][1]
            # quadDict 딕셔너리에 있는 log_probability 값 구하기 딕셔너리의 value값이 리스트일 때 그 리스트 값 중 1개만 출력
            Total_log_probability += log_probability
        else:
            pass



    return Total_log_probability



def main():
    BANNER = """\

    ———————————————————————————————————————————————————————————————————

                암호 해독의 세계에 오신 여러분을 환영합니다.         


        이 프로그램은 암호 알고리즘이나 암호키에 대한 지식이 없더라도

          암호화된 암호문을 해독할 수 있게 도와주는 프로그램입니다.

    ———————————————————————————————————————————————————————————————————

    """

    MENU = """\

    1. 선택 평문 공격 [chosen plaintext attack]

    2. 문자 빈도 분석 [quadgram frequency analysis]

    """
    print(BANNER)
    print(MENU)

    while True:
        choice = input('선택: ')
        if choice == '1':
            plaintext = input("평문: ")
            ciphertext = input("암호문: ")
            bifurcation = int(input("분기: "))
            texttodecrypt = input("해독할 문장: ")
            chosen_plaintext_attack(plaintext, ciphertext, bifurcation, texttodecrypt)

        elif choice == '2':
            Fp = open_file()
            quadDict = log_probability_dictionary(Fp)
            ciphertext = input('암호문:').upper()
            ciphertext = ciphertext.replace(' ', '').translate(str.maketrans({key: None for key in string.punctuation}))
            bruteforce_shift_cipher(ciphertext, quadDict)

        else:
            print('입력이 올바르지 않습니다.\n')



# Execute the main() function

if __name__ == "__main__":
    main()


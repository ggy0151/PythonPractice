from math import log10
import string


def chosen_plaintext_attack(plaintext, ciphertext, bifurcation, texttodecrypt):
    pass
#딕셔너리 사용
#h                ┌Key--------------------------------------┐ : ┌Value--┐  
#h  dictionary = {ciphertext[n*bifurcation : (n+1)*bifurcation] : plaintext[n]}

#출력 형식
#h  "\n해독된 텍스트: "
#h  "\n암호 해독이 중단되었습니다. 찾을 수 없는 키: "



#제공 함수
#file pointer 리턴 함수
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

#딕셔너리 사용
#h               ┌Key--┐ : ┌Value-(list 형식)---┐  
#h  dictionary = {quadgram : [count, log_probability]}

#   pointer를 받은 파일을 한줄씩 읽어서 딕셔너리로 만드는 과정
#h  total count of Quadgrams 도 함께 계산
    while True:
        line = fp.readline()
        if not line: #파일의 내용을 한줄씩 읽고 다음줄이 없으면 while문 break
            break


#   열었던 파일을 닫음
    fp.close()
    
#h  log probability 값 계산해서 딕셔너리에 추가
    for key in quadDic:
        pass


#출력 형식
    print("\n{:<8s}{:>13s}{:>22s}".format('Quadgram','Count','Log Probability'))
    print("-------------------------------------------")
#h  "{:<8s}{:>13d}{:>22.6f}".format( -해당값- , -해당값- , -해당값- ) 



def bruteforce_shift_cipher(ciphertext, quadgram_dictionary):

#출력 형식
    print("{:<5s}{:^35s}   {:>10s}".format("\nKey", "Plaintext", "Fitness")) 
    print("------------------------------------------------------") 
#h  "{:<5d}{:^35s}   {:>10.4f}".format( -해당값- , -해당값- , -해당값- )) 

#h  "\n계속하려면 엔터키를 누르세요..."
#h  "\n해독된 암호문: "



#제공 함수
#알파벳대문자 한칸씩 이동시키는 함수 ex) a -> b, b -> c, z -> a
def shift_characters(ciphertext):
    shiftedtext = ''
    for char in ciphertext:
        if ord(char) == 90:
            shiftedtext += chr(65)
        else:
            shiftedtext += chr(ord(char)+1)
    return shiftedtext



def fitness_calculator(potential_plaintext, quadgram_dictionary):
    pass
#매개변수로 받은 potential_plaintext를 qardgrams으로 나눠서   
#모든 qardgram의 log_probability들의 합을 리턴
#       ex) potential_plaintext = 'PYTHON' 일때 qardgrams은 ‘PYTH',‘YTHO,‘THON’



def main():

    BANNER = """\
    ---------------------------------------------------------------------
    
                암호 해독의 세계에 오신 여러분을 환영합니다.         
                
        이 프로그램은 암호 알고리즘이나 암호키에 대한 지식이 없더라도
          암호화된 암호문을 해독할 수 있게 도와주는 프로그램입니다.
    
    ---------------------------------------------------------------------
    """
    MENU = """\
    1. 선택 평문 공격 [chosen plaintext attack]
    2. 문자 빈도 분석 [quadgram frequency analysis]
    """


#h  "선택: "
#h  "입력이 올바르지 않습니다."
#h  "평문: "         -> plaintext
#h  "암호문: "       -> ciphertext
#h  "분기: "         -> bifurcation
#h  "해독할 문장: "  -> texttodecrypt


#h  2번 문자 빈도 분석에서 bruteforce_shift_cipher()함수 호출을 위한 ciphertext 공백, 구두점 제거
#h  ciphertext = ciphertext.replace(' ', '').translate(str.maketrans({key: None for key in string.punctuation}))



#Execute the main() function
if __name__ == "__main__":
    main()

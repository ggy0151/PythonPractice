import random
import time


l = ['가위','바위','보']

playerHP = 100
playerDamage = 0

enemyName = ''
enemyHP = 0
enemyDamage = 0

n = 1
leather = 0

def displayIntro():
	print('어둡고 음침한 밤...')
	time.sleep(0.5)
	print('당신은 '+ enemyName +'을 만납니다!!! ')
	time.sleep(0.5)

def displayRound():
	print('==========Round'+str(n)+'============')
	print('player\t','HP : [','='*int(playerHP/10),']')
	print(enemyName,'\t','HP : [','='*int(enemyHP/10),']')
	print('============================')

def setBear():
	global enemyName,enemyHP
	gomName = ['아빠곰','엄마곰','아기곰']
	gomHP = [80,60,40]
	gom = random.randint(0,2)

	enemyName = gomName[gom]
	enemyHP = gomHP[gom]
	

def choose():

	while True:
		print('가위바위보 중 하나를 선택 하십시오[1.가위 2.바위 3.보]')

		playerChoice = int(input()) - 1
		enemyChoice = random.randint(0,2)

		time.sleep(0.3)
		
		print('\tplayer\t' + enemyName)
		print('선택\t'+ l[playerChoice] + '\t' + l[enemyChoice])

		time.sleep(1)

		fight = playerChoice - enemyChoice

		if fight == 0:
			print('비겼습니다. 한번 더 진행하세요!')
		elif fight == 1 or fight == -2:
		    return 1
		else:
		    return -1
		

setBear()
displayIntro()

while playerHP > 0:
	
	displayRound()	

	
	playerDamage = random.randint(20,50)
	enemyDamage = random.randint(10,30)

	gameResult = choose()

	if gameResult ==-1:
		print('졌습니다ㅜㅜ')

		
		if random.randint(1,5) == 1:
			print('Critical Hit!!!')
			enemyDamage *= 2

		playerHP = playerHP - enemyDamage
		print(enemyName+'가 당신을 공격하여'+str(enemyDamage)+'만큼의 데미지를 입혔습니다.')

	elif gameResult ==1:
		print('이겼습니다')

		if random.randint(1,4) == 1:
			print('Critical Hit!!!')
			playerDamage *= 2

		enemyHP = enemyHP - playerDamage
		print(enemyName+'를 공격하여'+str(playerDamage)+'의 데미지를 입혔습니다. \n')

	time.sleep(0.5)

	if enemyHP <= 0 :
		leather += 1
		print('사냥 성공')
		print('승리!! 곰가죽을 ', leather ,' 개 얻었습니다.\n')

		setBear()
		displayIntro()	         

	if playerHP <= 0 :
		print('사냥 실패. 획득 가죽 :',str(leather),'개!')
	time.sleep(1)

	
	n+=1



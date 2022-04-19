from hashlib import sha256 #Libraria para converter em HASH utilizando SHA256
#Lista do Top200 de passwords mais usadas
top200 = ['123456','123456789','picture1','password','12345678','111111','123123','12345',
'1234567890','senha','1234567','qwerty','abc123','Million2','000000','1234','iloveyou',
'aaron431','password1','qqww1122','123','omgpop','123321','654321','qwertyuiop','qwer123456',
'123456a','a123456','666666','asdfghjkl','ashley','987654321','unknown','zxcvbnm','112233',
'chatbooks','20100728','123123123','princess','jacket025','evite','123abc','123qwe','sunshine',
'121212','dragon','1q2w3e4r','5201314','159753','123456789','pokemon','qwerty123','Bangbang123',
'jobandtalent','monkey','1qaz2wsx','abcd1234','default','aaaaaa','soccer','123654','ohmnamah23',
'12345678910','zing','shadow','102030','11111111','asdfgh','147258369','qazwsx','qwe123',
'michael','football','baseball','1q2w3e4r5t','party','daniel','asdasd','222222','myspace1',
'asd123','555555','a123456789','888888','7777777','fuckyou','1234qwer','superman','147258',
'999999','159357','love123','tigger','purple','samantha','charlie','babygirl','88888888',
'jordan23','789456123','jordan','anhyeuem','killer','basketball','michelle','1q2w3e','lol123',
'qwerty1','789456','6655321','nicole','naruto','master','chocolate','maggie','computer','hannah',
'jessica','123456789a','password123','hunter','686584','iloveyou1','0987654321','justin','cookie',
'hello','blink182','andrew','25251325','love','987654','bailey','princess1','0123456','101010',
'12341234','a801016','1111','1111111','anthony','yugioh','fuckyou1','amanda','asdf1234','trustno1',
'butterfly','x4ivygA51F','iloveu','batman','starwars','summer','michael1','00000000','lovely',
'jakcgt333','buster','jennifer','babygirl1','family','456789','azerty','andrea','q1w2e3r4',
'qwer1234','hello123','10203','matthew','pepper','12345a','letmein','joshua','131313','123456b',
'madison','Sample123','777777','football1','jesus1','taylor','b123456','whatever','welcome',
'ginger','flower','333333','1111111111','robert','samsung','a12345','loveme','gabriel','alexander',
'cheese','passw0rd','142536','peanut','11223344','thomas','angel1']
#Hashed password que se pretende descobrir
hashedPasswordToCrack = '96cae35ce8a9b0244178bf28e4966c2ce1b8385723a96a6b838858cdd6ca0a1e'
#Ciclo para comparar as hash
for password in top200:
	if(sha256(password.encode('utf-8')).hexdigest()==hashedPasswordToCrack):
		print(password)
		break


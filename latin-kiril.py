latin_={
	"g'":"ғ",
	"g`":"ғ",
	"G'":"Ғ",
	"G`":"Ғ",
	"o'":"ў",
	"o`":"ў",
	"O'":"Ў",
	"O`":"Ў",
	"sh":"ш",
	"SH":"Ш",
	"sH":"ш",
	"Sh":"Ш",
	"ch":"ч",
	"CH":"Ч",
	"Ch":"Ч",
	"cH":"ч",
	"yo":"ё",
	"yO":"ё",
	"Yo":"Ё",
	"YO":"Ё",
	"ye":"е",
	"yE":"е",
	"Ye":"Е",
	"YE":"Е",
	"yu":"ю",
	"yU":"ю",
	"Yu":"Ю",
	"YU":"Ю",
	"ya":"я",
	"yA":"я",
	"Ya":"Я",
	"YA":"Я",
}
latin={
	"h":"ҳ",
	"H":"Ҳ",
	"q":"қ",
	"Q":"Қ",
	"`":"ъ",
	"'":"ъ",
	"a":"а",
	"A":"А",
	"b":"б",
	"B":"Б",
	"c":"с",
	"C":"С",
	"d":"д",
	"D":"Д",
	"e":"е",
	"E":"Е",
	"f":"ф",
	"F":"Ф",
	"g":"г",
	"G":"Г",
	"i":"и",
	"I":"И",
	"j":"ж",
	"J":"Ж",
	"k":"к",
	"K":"К",
	"l":"л",
	"L":"Л",
	"m":"м",
	"M":"М",
	"n":"н",
	"N":"Н",
	"o":"о",
	"O":"О",
	"p":"п",
	"P":"П",
	"r":"р",
	"R":"Р",
	"s":"с",
	"S":"С",
	"t":"т",
	"T":"Т",
	"u":"у",
	"U":"У",
	"v":"в",
	"V":"В",
	"x":"х",
	"X":"Х",
	"y":"й",
	"Y":"Й",
	"z":"з",
	"Z":"З",
	"w":"в",
	"W":"В",
}

ee={
	"e":"э",
	"E":"Э",
}

ye={
	"е":"ye",
	"Е":"Ye"
}

kiril={
	"а":"a",
	"А":"A",
	"б":"b",
	"Б":"B",
	"в":"v",
	"В":"V",
	"г":"g",
	"Г":"G",
	"д":"d",
	"Д":"D",
	"э":"e",
	"Э":"E",
	"ф":"f",
	"Ф":"F",
	"е":"e",
	"Е":"E",
	"ё":"yo",
	"Ё":"Yo",
	"ж":"j",
	"Ж":"J",
	"з":"z",
	"З":"Z",
	"и":"i",
	"И":"I",
	"й":"y",
	"Й":"Y",
	"к":"k",
	"К":"K",
	"л":"l",
	"Л":"L",
	"м":"m",
	"М":"M",
	"н":"n",
	"Н":"N",
	"о":"o",
	"О":"O",
	"п":"p",
	"П":"P",
	"қ":"q",
	"Қ":"Q",
	"р":"r",
	"Р":"R",
	"с":"s",
	"С":"S",
	"т":"t",
	"Т":"T",
	"у":"u",
	"У":"U",
	"х":"x",
	"Х":"X",
	"ў":"o'",
	"Ў":"O'",
	"ғ":"g'",
	"Ғ":"G'",
	"ш":"sh",
	"Ш":"Sh",
	"ч":"ch",
	"Ч":"Ch",
	"ҳ":"h",
	"Ҳ":"H",
	"ъ":"'",
	"Ъ":"'",
	"Ю":"Yu",
	"ю":"yu",
}

kiril_letters=[1118, 1171, 1179, 1203, 1105, 1025]

def is_letter(txt, count):
	a = False
	if count > 0:
		let = ord(txt[count-1])
		a = 1040 <= let <= 1103 or let in kiril_letters or 65<=let<=90 or 97<=let<=122 
	return a 

def to_kiril(txt: str):
	for i in latin_:
		txt=txt.replace(i, latin_[i])
	new_txt=""
	for count, i in enumerate(txt):
		if i.lower() =="e":
			if is_letter(txt, count):
				new_txt+=latin[i]
			else:
				new_txt+=ee[i]  
		else:
			new_txt+=latin[i] if i in latin else i
	return new_txt

def to_latin(txt:str):
	new_txt=""
	for count, i in enumerate(txt):
		if i.lower() == "е":
			if is_letter(txt, count):
				new_txt+=kiril[i]
			else:
				new_txt+=ye[i]
		else:
			new_txt+=kiril[i] if i in kiril else i
	return new_txt


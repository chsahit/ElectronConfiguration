def shell(prefix,max_num,configStr,atomic_number):
        while max_num>0 :
                if atomic_number>=max_num:
                        configStr=configStr+' '+prefix+"%i" %max_num
                        return configStr
                max_num-=1
        return configStr

def s1(atomic_number,configStr):
	configStr=shell('1s',2,configStr,atomic_number)
	return configStr

def s2(atomic_number,configStr):
	configStr=shell('2s',2,configStr,atomic_number)
	return configStr

def p2(atomic_number,configStr):
	configStr=shell('2p',6,configStr,atomic_number)
	return configStr

def s3(atomic_number,configStr):
	configStr=shell('3s',2,configStr,atomic_number)
        return configStr

def p3(atomic_number,configStr):
	configStr=shell('3p',6,configStr,atomic_number)
	return configStr

def s4(atomic_number,configStr):
	configStr=shell('4s',2,configStr,atomic_number)
	return configStr

def d3(atomic_number,configStr):
	configStr=shell('3d',10,configStr,atomic_number)
	return configStr

def p4(atomic_number,configStr):
	configStr=shell('4p',6,configStr,atomic_number)
	return configStr

def s5(atomic_number,configStr):
	configStr=shell('5s',2,configStr,atomic_number)
	return configStr

def d4(atomic_number,configStr):
        configStr=shell('4d',10,configStr,atomic_number)
        return configStr

def p5(atomic_number,configStr):
        configStr=shell('5p',6,configStr,atomic_number)
        return configStr

def s6(atomic_number,configStr):
        configStr=shell('6s',2,configStr,atomic_number)
        return configStr


def f4(atomic_number,configStr):
        configStr=shell('4f',14,configStr,atomic_number)
        return configStr

def d5(atomic_number,configStr):
        configStr=shell('5d',10,configStr,atomic_number)
        return configStr

def p6(atomic_number,configStr):
        configStr=shell('6p',6,configStr,atomic_number)
        return configStr

def s7(atomic_number,configStr):
        configStr=shell('7s',2,configStr,atomic_number)
        return configStr

def f5(atomic_number,configStr):
        configStr=shell('5f',14,configStr,atomic_number)
        return configStr

def d6(atomic_number,configStr):
        configStr=shell('6d',10,configStr,atomic_number)
        return configStr

def p7(atomic_number,configStr):
        configStr=shell('7p',6,configStr,atomic_number)
        return configStr

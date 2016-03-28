import binascii

file = open("nibbles.txt", "r")

count = 1
bytes = ""
message = ""

for i, line in enumerate(file):
    startIndex = line.index('(')
    endIndex = line.index(')')

    co = line[startIndex:endIndex+1]        # (-1.35, 2.30)
    coordinates = line[startIndex+1:endIndex]   # -1.35, 2.30
    comma = coordinates.index(',')
    iVoltage = coordinates[0:comma]
    iv = float(iVoltage)
    qVoltage = coordinates[comma+2:]
    qv = float(qVoltage)
    
    if iv >= 0 and iv <= 2 and qv >= 0 and qv <= 2:
        point = "1101"
    if iv >= 2 and iv <= 4 and qv >= 0 and qv <= 2:
        point = "1001"
    if iv >= 0 and iv <= 2 and qv >= 2 and qv <= 4:
        point = "1100"
    if iv >= 2 and iv <= 4 and qv >= 2 and qv <= 4:
        point = "1000"
        
    if iv >= 0 and iv <= 2 and qv <= 0 and qv >= -2:
        point = "1111"
    if iv >= 2 and iv <= 4 and qv <= 0 and qv >= -2:
        point = "1011"
    if iv >= 0 and iv <= 2 and qv <= -2 and qv >= -4:
        point = "1110"
    if iv >= 2 and iv <= 4 and qv <= -2 and qv >= -4:
        point = "1010"
        
    if iv >= -4 and iv <= -2 and qv >= 0 and qv <= 2:
        point = "0001"
    if iv >= -2 and iv <= 0 and qv >= 0 and qv <= 2:
        point = "0101"
    if iv >= -4 and iv <= -2 and qv >= 2 and qv <= 4:
        point = "0000"
    if iv >= -2 and iv <= 0 and qv >= 2 and qv <= 4:
        point = "0100"
        
    if iv >= -4 and iv <= -2 and qv >= -2 and qv <= 0:
        point = "0011"
    if iv >= -2 and iv <= 0 and qv >= -2 and qv <= 0:
        point = "0111"
    if iv >= -4 and iv <= -2 and qv >= -4 and qv <= -2:
        point = "0010"
    if iv >= -2 and iv <= 0 and qv >= -4 and qv <= -2:
        point = "0110"

    bytes = bytes + point
    if count%2 == 0 :
        n = int(bytes, 2)
        letter = binascii.unhexlify('%x' %n) 
        #letter = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode() # for Python 3.2+
        print(co + " decodes as " + point + " - together, " + bytes + " gives \"" + letter + "\"\n")
        bytes = ""
        message = message + letter
    else :
        print(co + " decodes as " + bytes)
    
    count += 1

print("Decoded message with symbol errors included: " + message)
        

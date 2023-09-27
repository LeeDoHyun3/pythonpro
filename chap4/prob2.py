import random as r

hHp = r.randrange(50, 100)
mHp = r.randrange(50, 100)
count = 0
print("hero HP: " + str(hHp) + ", monster HP: " + str(mHp))

while(hHp > 0 and mHp > 0):
    hAttack = r.randrange(-10, 20)
    mAttack = r.randrange(-10, 20)

    if (hAttack > 0 and mAttack > 0) :
        hHp -= mAttack
        mHp -= hAttack
        print("hero(HP:" + str(hHp) +", attck:"+ str(hAttack) +") succese <-> monster(HP:"+ str(mHp) + ", attck:"+ str(mAttack) + ") success")
        count += 1
    elif(hAttack > 0 and mAttack <= 0) :
        mHp -= hAttack
        print("hero(HP:" + str(hHp) +", attck:"+ str(hAttack) +") succese <-> monster(HP:"+ str(mHp) +", attck:"+ str(mAttack) + ") fail")
        count += 1
    elif (hAttack <= 0 and mAttack > 0) :
        hHp -= mAttack
        print("hero(HP:" + str(hHp) +", attck:"+ str(hAttack) +") fail <-> monster(HP:"+str(mHp)+", attck:"+ str(mAttack) + ") success")
        count += 1
    elif(hAttack <= 0 and mAttack <= 0) :
        print("Hero(HP:" + str(hHp) +", attck:"+ str(hAttack) +") fail <-> monster(HP:"+str(mHp)+", attck:"+ str(mAttack) + ") fail")
        count += 1

print("------------------------------------------\n")
print("Total phase : "+ str(count) + ",")
if(hHp > 0) :
    print("Hero Win!!!!")
else:
    print("Monster Win!!!!")


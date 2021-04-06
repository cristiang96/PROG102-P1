# "P1 Exercise - Mastering Mastermind"
def mastering(n, s1, s2):
    r, s = 0, 0
    ite = 0
    while ite < len(s1):
        if s1[ite] == s2[ite]:
            r+=1
            s1 = s1[0:ite]+s1[ite+1:]
            s2 = s2[0:ite]+s2[ite+1:]
        else:
            ite+=1

    for i in set(s1):
        s+= min(s1.count(i),s2.count(i))
    print(r,s)

if __name__ == '__main__':
    mastering(4, "BACC", "CABB")
    # mastering(13, "ABCDEFGHIJKLM", "NOPQRSTUVWXYZ")
    mastering(6, "REJUIO", "RFOIJO")


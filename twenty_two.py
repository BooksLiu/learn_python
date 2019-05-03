# coding:utf-8

'''
题目：两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''

teamA = ["a", "b", "c"]
teamB = ["x", "y", "z"]

relationsArr = []
mapRelations = {
    "a": 0,
    "b": 0,
    "c": 0,
    "x": 0,
    "y": 0,
    "z": 0
}

for indexA in range(0, 3):
    for indexB in range(0, 3):
        if teamA[indexA] == "a" and teamB[indexB] == "x":
            continue
        elif teamA[indexA] == "c" and teamB[indexB] == "x" or teamB[indexB] == "z":
            continue
        else:
            if mapRelations[teamA[indexA]] > 1:
                # 需要回溯
                print  ""
            else:
                mapRelations[teamA[indexA]] = mapRelations[teamA[indexA]] + 1
                mapRelations[teamB[indexB]] = mapRelations[teamB[indexB]] + 1


for mateA in teamA:
    for mateB in teamB:
        if (mateA == "a" and mateB == "x"):
            continue
        elif mateA == "c" and mateB == "x" or mateB == "z":
            continue
        else:
            mapRelations.get()
            print mateA + " VS " + mateB

# --------------------------------------
# エンコード宣言
# --------------------------------------
# -*- coding: utf-8 -*-
# --------------------------------------
# 定数宣言
# --------------------------------------
G_TURE = 0            # 正常判定
G_FALSE = -1          # エラー判定
G_MAXSTONE = 35       # 石の最大数
G_ROW = 5             # 石を並べる行数
G_COL = 7             # 石を並べる列数
G_SENTE = 0           # 先手
G_GOTE = 1            # 後手
# -------------------------------------------------------------------
# 取得する全パターンを一つのリストにするよ
# -------------------------------------------------------------------
def fncAllForOne(l_lstLiveStone):
    chkListAll = []
    chkListAll = fncAddList(chkListAll,fncGeneratePair(4,l_lstLiveStone,l_lstLiveStone[0]))
    chkListAll = fncAddList(chkListAll,fncGeneratePair(3,l_lstLiveStone,l_lstLiveStone[0]))
    chkListAll = fncAddList(chkListAll,fncGeneratePair(2,l_lstLiveStone,l_lstLiveStone[0]))
    chkListAll = fncAddList(chkListAll,l_lstLiveStone)
    print(chkListAll)
    return chkListAll
# -------------------------------------------------------------------
# 複数のリストを1つのリストに追加していくよ
# -------------------------------------------------------------------
def fncAddList(outList,inList):
    #呼び出しエラーの回避------------------------------------------------
    #追加要素が0で呼び出されたらそのまま返す
    if len(inList) < 1:
        return outList
#--------------------------------------------------------------------
#1要素づつ追加して返す
    for i in inList:
        outList.append(i)
        return outList
# -------------------------------------------------------------------
# リストにリストを追加するよ！
# -------------------------------------------------------------------
def fncListAdd(outList,inList):
    inNum = len(inList)
    rtnList = list(outList)
    #呼び出しエラーの回避------------------------------------------------
    #追加要素が0で呼び出されたらそのまま返す
    if inNum < 1:
        return outList
    #--------------------------------------------------------------------
    #リストを追加して返す
    rtnList.append(inList)
    return rtnList
# -------------------------------------------------------------------
# 連続する「pairNum」個の組の組み合わせ配列を作成しますよ！
# -------------------------------------------------------------------
def fncGeneratePair(pairNum,inListLiveStone,inChkListStone):
    #呼び出しエラーの回避--------------------------------
    #引数が無効な状態で呼び出されたら終了
    if len(inChkListStone) < 1:
        return -1
    elif len(inListLiveStone) < 1:
        return -1
    elif pairNum < 2:
        return -1
    #--------------------------------------------------------------------
    rtn_lstLiveStone = []    # 残存石のペア配列を初期化
    rtn_chkLiveStone = []    # 残存石のペア配列を初期化
    l_lstLiveStone = list(inListLiveStone)    # 残存石を処理用に格納
    l_ChkListStone = []
    l_lstchkLiveStone = list(l_lstLiveStone)
    
    #pairNumが0になるまでは準備を続ける！
    for i in l_lstLiveStone:
        del l_ChkListStone[:]
        l_lstchkLiveStone.remove(i)
        if pairNum > 1:
            outPairNum = pairNum - 1
            outChkStone = list(i)
            rtn_chkLiveStone = list(l_lstLiveStone)
            rtn_fnlstLiveStone = list(fncGeneratePair(outPairNum,rtn_chkLiveStone,outChkStone))
            rtn_lstLiveStone.extend(rtn_fnlstLiveStone)
        else:
            l_ChkListStone.extend(inChkListStone)
            l_ChkListStone.append(i)
            print(l_ChkListStone)
            rtn_chkLiveStone = list(l_ChkListStone)
            if fncCheckStones(rtn_chkLiveStone) == G_TURE:
                rtn_lstLiveStone.append(rtn_chkLiveStone)
                return rtn_lstLiveStone
# ----------------------------------------------------------
# 複数の石の連続性をチェックする関数
#
# 引数：取る石の番号を格納した文字列リスト
# 戻値：正常(G_TRUE)もしくはエラー(G_FALSE)
# ----------------------------------------------------------
def fncCheckStones(a_lstTakeStone):
    i = len(a_lstTakeStone)          # 石の数を取得
    iMin = int(a_lstTakeStone[0])    # 最小値を取得
    iMax = int(a_lstTakeStone[i - 1]) # 最大値を取得
    iMinDiv = int(iMin / G_COL) # 最小を列数で割った整数部
    iMaxDiv = int(iMax / G_COL) # 最大を列数で割った整数部
    iMinMod = iMin % G_COL      # 最小を列数で割った余り
    iMaxMod = iMax % G_COL      # 最大を列数で割った余り
    # 最大が石数＋最小で、最大と最小を列数で割った結果が同じなら
    if iMax == (iMin + i -1) and iMinDiv == iMaxDiv:
    # 横の連続なので
        return G_TURE # 正常を返す
    # 最大が最小＋石数×列数で、
    # 最大を列数で割った余りと最小を列数で割った余りが同じなら
    if iMax == iMin + ((i -1)* G_COL) and iMinMod == iMaxMod:
        # 他に石がなければ縦の連続なので
        if i == 2:
            return G_TURE # 正常を返す
        # 列数で割った余りがすべて同じでないなら
    for j in range(len(a_lstTakeStone)): # 石の数だけループ
        # 石を列数で割った余りがすべて一致しないなら
        if (int(a_lstTakeStone[j]) % G_COL) != iMinMod:
            return G_FALSE # エラーを返す
        # 縦の連続なので
        return G_TURE # 正常を返す
    # 最大が初期値＋長さ×(列数-1)で、
    # 最小を列数で割った余りが最大を列数で割った余りより小さいなら
    if iMax == iMin + ((i - 1) * (G_COL - 1)) and iMinMod > iMaxMod:
        # 列数-1で割った余りがすべて同じでないなら
        for j in range(len(a_lstTakeStone)):
            # 石の数だけループ
            # 石を列数-1で割った余りがすべて一致しないなら
            if (int(a_lstTakeStone[j]) % (G_COL - 1)) != iMin % (G_COL - 1):
                return -1 # エラーを返す
            # 斜め左の連続なので
            return G_TURE # 正常を返す
        # 最大が初期値＋長さ×(列数+1)で、
        # 最小を列数で割った余りが最大を列数で割った余りより大きいなら
        if iMax == iMin + ((i - 1) * (G_COL + 1)) and iMinMod < iMaxMod:
            # 列数+1で割った余りがすべて同じでないなら
            for j in range(len(a_lstTakeStone)): # 石の数だけループ
                # 石を列数+1で割った余りがすべて一致しないなら
                if (int(a_lstTakeStone[j])) % (G_COL + 1) != iMin % (G_COL + 1):
                    return -1 # エラーを返す
                # 斜め右の連続なので
                return G_TURE # 正常を返す
            # どのパターンにも当てはまらなければ
            return G_FALSE # エラーを返す
    # --------------------------------------
    # 実行部ですよ～
    # --------------------------------------
    #chk = fncAllForOne(['01','02','03','04','05','06']):
    chk = fncGeneratePair(2,['01','02','03','04','05','06','07','08','13','14','15','16','17','18'],['01'])
    print(chk)

import csv
import pandas as pd
import pygal
def getCSV():
    """get csv function"""
    csvdf = pd.read_csv('C:/Users/WIN/Desktop/Project PSIT2/bnkdata.csv', encoding='utf-8')
    columns = ["date","text"]
    csvdf.columns = columns
    text = csvdf['text']
    return text

def RemoveRT():
    """Remove "RT" function"""
    text = getCSV()
    lit = []
    count = 0
    for i in text:
        if i[0:2] == "RT":
            pass
        else:
            lit.append(i.lower())
    return lit

def countmember():
    """Count BNK member function"""
    data = RemoveRT()
    count_aom = 0
    count_bamboo = 0
    count_cake = 0
    count_cherprang = 0
    count_deenee = 0
    count_faii = 0
    count_fifa = 0
    count_fond = 0
    count_gygee = 0
    count_izurina = 0
    count_jaa = 0
    count_jane = 0
    count_jennis = 0
    count_jib = 0
    count_june = 0
    count_kaew = 0
    count_kaimook = 0
    count_kate = 0
    count_khamin = 0
    count_kheng = 0
    count_korn = 0
    count_maira = 0
    count_mewnich = 0
    count_mind = 0
    count_minmin = 0
    count_miori = 0
    count_mobile = 0
    count_music = 0
    count_myyu = 0
    count_namneung = 0
    count_namsai = 0
    count_natherine = 0
    count_new = 0
    count_niky = 0
    count_nine = 0
    count_nink = 0
    count_oom = 0
    count_orn = 0
    count_pakwan = 0
    count_panda = 0
    count_phukkhom = 0
    count_paim = 0
    count_pun = 0
    count_pupe = 0
    count_ratah = 0
    count_satchan = 0
    count_stang = 0
    count_tarwaan = 0
    count_view = 0
    count_wee = 0
    count_noey = 0
    count_piam = 0

    for i in data:
        if "#aombnk48" in i:
            count_aom += 1
        if "#bamboobnk48" in i:
            count_bamboo += 1
        if "#cakebnk48" in i:
            count_cake += 1
        if "#cherprangbnk48" in i:
            count_cherprang += 1
        if "#deeneebnk48" in i:
            count_deenee += 1
        if "#faiibnk48" in i:
            count_faii += 1
        if "#fifabnk48" in i:
            count_fifa += 1
        if "#fondbnk48" in i:
            count_fond += 1
        if "#gygeebnk48" in i:
            count_gygee += 1
        if "#izurinabnk48" in i:
            count_izurina += 1
        if "#jaabnk48" in i:
            count_jaa += 1
        if "#janebnk48" in i:
            count_jane += 1
        if "#jennisbnk48" in i:
            count_jennis += 1
        if "#jibbnk48" in i:
            count_jib += 1
        if "#junébnk48" in i:
            count_june += 1
        if "#kaewbnk48" in i:
            count_kaew += 1
        if "#kaimookbnk48" in i:
            count_kaimook += 1
        if "#katebnk48" in i:
            count_kate += 1
        if "#khaminbnk48" in i:
            count_khamin += 1
        if "#khengbnk48" in i:
            count_kheng += 1
        if "#kornbnk48" in i:
            count_korn += 1
        if "#mairabnk48" in i:
            count_maira += 1
        if "#mewnichbnk48" in i:
            count_mewnich += 1
        if "#mindbnk48" in i:
            count_mind += 1
        if "#minminbnk48" in i:
            count_minmin += 1
        if "#mioribnk48" in i:
            count_miori += 1
        if "#mobilebnk48" in i:
            count_mobile += 1
        if "#musicbnk48" in i:
            count_music += 1
        if "#myyubnk48" in i:
            count_myyu += 1
        if "#namneungbnk48" in i:
            count_namneung += 1
        if "#namsaibnk48" in i:
            count_namsai += 1
        if "#natherinebnk48" in i:
            count_natherine += 1
        if "#newbnk48" in i:
            count_new += 1
        if "#nikybnk48" in i:
            count_niky += 1
        if "#ninebnk48" in i:
            count_nine += 1
        if "#ninkbnk48" in i:
            count_nink += 1
        if "#noeybnk48" in i:
            count_noey += 1
        if "#oombnk48" in i:
            count_oom += 1
        if "#ornbnk48" in i:
            count_orn += 1
        if "#pakwanbnk48" in i:
            count_pakwan += 1
        if "#pandabnk48" in i:
            count_panda += 1
        if "#phukkhombnk48" in i:
            count_phukkhom += 1
        if "#piambnk48" in i:
            count_piam += 1
        if "#punbnk48" in i:
            count_pun += 1
        if "#pupebnk48" in i:
            count_pupe += 1
        if "#ratahbnk48" in i:
            count_ratah += 1
        if "#satchanbnk48" in i:
            count_satchan += 1
        if "#stangbnk48" in i:
            count_stang += 1
        if "#tarwaanbnk48" in i:
            count_tarwaan += 1
        if "#viewbnk48" in i:
            count_view += 1
        if "#weebnk48" in i:
            count_wee += 1

    lit2 = [(count_aom,"aom"), (count_cake,"cake"), (count_bamboo,"bamboo"), (count_cherprang,"cherprang"), (count_deenee,"deenee"), \
    (count_faii,"faii"), (count_fifa,"fifa"), (count_fond,"fond"), (count_gygee, "gygee"), (count_izurina,"izurina"), \
    (count_jaa,"jaa"), (count_jane,"jane"), (count_jennis,"jennis"), (count_jib,"jib"), (count_june,"juné"), \
    (count_kaew,"keaw"), (count_kaimook,"kaimook"), (count_kate,"kate"), (count_khamin,"khamin"), (count_kheng,"kheng"), \
    (count_korn,"korn"), (count_maira,"maira"), (count_mewnich,"mewnich"), (count_mind, "mind"), (count_minmin, "minmin"), \
    (count_miori,"miori"), (count_mobile,"mobile"), (count_music,"music"), (count_myyu,"myyu"), (count_namneung,"namneung"), \
    (count_namsai,"namsai"), (count_natherine,"natherine"), (count_new,"new"), (count_niky,"niky"), (count_nine,"nine"), \
    (count_nink,"nink"), (count_noey,"noey"), (count_oom,"oom"), (count_orn,"orn"), (count_pakwan,"pakwan"), \
    (count_panda,"panda"), (count_phukkhom,"phukkhom"), (count_piam,"piam"), (count_pun,"pun"), (count_pupe,"pupe"), \
    (count_ratah,"ratah"), (count_satchan,"satchan"), (count_stang,"stang"), (count_tarwaan,"tarwaan"), (count_view,"view"), (count_wee,"wee")]

    lit2.sort(reverse=True)
    return lit2

def pygal():
    """made chart"""
    data = countmember()
    rank = data[0:7]
    print(rank)
#    line_chart = pygal.HorizontalBar()
#    line_chart.title = 'Browser usage in February 2012 (in %)'
#    for i in range(0,7):
#        line_chart.add(rank[i][1], rank[i][0])
#    line_chart.render('projjjjjj.svg')
pygal()

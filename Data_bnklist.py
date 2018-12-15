import csv
import pandas as pd
import pygal as pg
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
    for char in text:
        if "RT" in char[0:3]:
            pass
        else:
            lit.append(char.lower())
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
        count_aom += i.count("#aombnk48")
        count_bamboo += i.count("#bamboobnk48")
        count_cake += i.count("#cakebnk48")
        count_cherprang += i.count("#cherprangbnk48")
        count_deenee += i.count("#deeneebnk48")
        count_faii += i.count("#faiibnk48")
        count_fifa += i.count("#fifabnk48")
        count_fond += i.count("#fondbnk48")
        count_gygee += i.count("#gygeebnk48")
        count_izurina += i.count("#izurinabnk48")
        count_jaa += i.count("#jaabnk48")
        count_jane += i.count("#janebnk48")
        count_jennis += i.count("#jennisbnk48")
        count_jib += i.count("#jibbnk48")
        count_june += i.count("#junébnk48")
        count_kaew += i.count("#kaewbnk48")
        count_kaimook += i.count("#kaimookbnk48")
        count_kate += i.count("#katebnk48")
        count_khamin += i.count("#khaminbnk48")
        count_kheng += i.count("#khengbnk48")
        count_korn += i.count("#kornbnk48")
        count_maira += i.count("#mairabnk48")
        count_mewnich += i.count("#mewnichbnk48")
        count_mind += i.count("#mindbnk48")
        count_minmin += i.count("#minminbnk48")
        count_miori += i.count("#mioribnk48")
        count_mobile += i.count("#mobilebnk48")
        count_music += i.count("#musicbnk48")
        count_myyu += i.count("#myyubnk48")
        count_namneung += i.count("#namneungbnk48")
        count_namsai += i.count("#namsaibnk48")
        count_natherine += i.count("#natherinebnk48")
        count_new += i.count("#newbnk48")
        count_niky += i.count("#nikybnk48")
        count_nine += i.count("#ninebnk48")
        count_nink += i.count("#ninkbnk48")
        count_oom += i.count("#oombnk48")
        count_orn += i.count("#ornbnk48")
        count_pakwan += i.count("#pakwanbnk48")
        count_panda += i.count("#pandabnk48")
        count_phukkhom += i.count("#phukkhombnk48")
        count_piam += i.count("#piambnk48")
        count_pun += i.count("#punbnk48")
        count_pupe += i.count("#pupebnk48")
        count_ratah += i.count("#ratahbnk48")
        count_satchan += i.count("#satchanbnk48")
        count_stang += i.count("#stangbnk48")
        count_tarwaan += i.count("#tarwaanbnk48")
        count_view += i.count("#viewbnk48")
        count_wee += i.count("#weebnk48")
        count_noey += i.count("#noeybnk48")

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
    """ Make a graph HorizontalBar """
    data = countmember()
    rank = data[0:7]
    line_chart = pg.HorizontalBar()
    line_chart.title = 'Top 7 BNK48 member in 13-14 Dec 2018'
    for i in range(0,7):
        line_chart.add(rank[i][1], rank[i][0])
    line_chart.render_to_file('bnk48 graph.svg')
pygal()


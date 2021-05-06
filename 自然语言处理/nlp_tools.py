# -*-coding:utf-8-*- 
# 作者：   29511
# 文件名:  nlp_tools.py
# 日期时间：2021/3/16，17:31

# 工具函数大致列表：
# 名字即功能：
#
# 1.文件1读入写入文件2
# 2.文件1内容分词去逗号存入文件2
# 3.函数1调用函数2进行分词和去符号去停用词
# 4.为了计算p(w)，words总数，去重words总数
# 5.[1,2,3]+[4,5,6]=[5,7,9]
# 6.[1,2,3]*2=[2,4,6]
# 7.余弦距离 Li
# 8.余弦距离
# 9.得到一个A_rate之后乘以的新wordVector
# 10.得到一个词的词向量
# 11.字典根据value进行排序
# 12.'''将字典数据存入到二进制文件中'''
# 13.二进制文件中读入数据并转化为字典'''
# 14.csv文件时为其头部加上列名
# 15.测试集与训练集计算
# 16.随机选择数据
# 17.li arctan(1/|a-b|)
# 18.19.准确率

import jieba
import numpy as np
import gensim
import csv
import pickle
import pandas as pd
import math

# 工具函数
'''
    读入文件1数据写入文件2 这个函数是学习初期对读入文件和写入文件的
    一个简单实现，就是讲txt1中的数据通过读取然后在写入文件txt2中
    注意在函数结束时的close方法的调用防止内存占用
'''


def read1ToWrite2(readfile_path, writefile_path):
    fin = open(readfile_path, 'r')  # 路径写死了
    fou = open(writefile_path, 'w')
    line = fin.readlines()  # 加s的是获取所有数据
    for i in line:
        fou.write(i)
    fin.close()
    fou.close()


"""
这个函数那是在第一个函数的基础上进行改进
增加了使用jieba进行分词，是按照一行进行读取的同时设置了分词模式，
并使用了简单粗暴的方法进行了逗号等字符的去除
同时并将数据写入另一个文件中    
"""


# 文件1内容分词去逗号存入文件2
def cutWordTofile(writefile_path, cutWordfile_path):
    fin = open(writefile_path, 'r')  # 路径写死了
    fou = open(cutWordfile_path, 'w')
    line = fin.readline()
    while line:
        newline = ' '.join(jieba.cut(line, cut_all=False)).replace('，', '').replace('。', '')  # 结巴分词并去除逗号
        fou.write(newline)
        line = fin.readline()  # 每次更新一个line相当于i++
    fin.close()
    fou.close()


"""
这段函数里面总共有两个函数组成是进一步的改进，增加了停用词的去除
并实现了停用词的动态增加
函数一执行文件的读写操作，函数1调用函数2进行分词和去符号去停用词等操作
"""


# 读入文件分词之后存入文件中间有三函数(1,2,)的调用使用线进行分割
# --------------------------------------------------------------------------------------------------------
# 1读入文件分词之后存入文件
def readCutRemovewrite(readfile_path, writefile_path):
    inputs = open(readfile_path, 'r', encoding='utf-8')
    outputs = open(writefile_path, 'w', encoding='utf8')
    for line in inputs:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()


# 2句子分词并去停用词
def seg_sentence(sentence):
    # 2创建停用词list
    stopWords = [line.strip() for line in open('data/stopWord.txt', 'r', encoding='utf-8').readlines()]
    sentence_seged = jieba.cut(sentence.strip())
    outstr = ''
    for word in sentence_seged:
        if word not in stopWords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


# --------------------------------------------------------------------------------------------------------
"""
这个函数是为了计算p(w),在分词的同时记录以下数据
1所有words总数
2去重words总数
3每一个唯一word的概率
带着写入文件功能
"""


def get_words_Word_wordRate(readFilePath, writeFilePath):
    with codecs.open(readFilePath, 'r', 'utf8') as f:
        txt = f.read()
    fout = open(writeFilePath, 'w', encoding='utf-8')
    seg_list = jieba.cut(txt)
    c = Counter()  # 内函数计数器继承了字典类
    count = 0
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            count += 1
            c[x] += 1
    print('words result')
    print('all number result')
    print(count)
    print('no repeat words result')
    print(len(c))
    for key, value in c.most_common():  # 5就是返回5个词无参数 就是所有
        # print('%s  %d' % (key,   round(value/count, 5)))#other write
        # print(key, ' '*3, value, ' '*3,  round(value/count, 10))
        writestr = key + ' ' * 10 + str(round(value / count, 10)) + '\n'  # 通过str将int转成string
        fout.write(writestr)
    f.close()
    fout.close()


'''函数@liyang 将两个list[] 中每一个值对应相加如[1,2,3]+[4,5,6]=[5,7,9]
 返回值为新列表的长度和 数据'''


# 这个函数有了更新使用了矩阵multi_dynamic_list_sum(multi_list)
def two_list_sum(alist, blist):
    c = [a[i] + b[i] for i in range(min(len(a), len(b)))]
    return c


'''函数@liyang 将list[] 中每一个值对应相乘一个数a如[1,2,3]*2=[2,4,6]
 返回值为新列表的数据'''


def list_mult_a(listt, a):
    # 警告，当list的很大且数据都是小数存在，a也是小数时，
    # 这个函数会报错，说a不能是float类型 但实际检验过程中是可为float的
    b = [i * a for i in listt]
    return b


'''这是对上一个函数的改进 变成矩阵在乘防止出现问题'''


def listto_matrix_mult_a(list, a):
    b = np.array(list)
    c = b * a
    return c


'''输入：是两个向量的坐标
    输出: 两者的余弦距离'''


def cosineSimilarity_Li(a_vect, b_vect):
    '''@liyang'''
    dot_val = 0.0
    a_norm = 0.0
    b_norm = 0.0
    cos = None

    for i in range(min(len(a_vect), len(b_vect))):
        dot_val += a_vect[i] * b_vect[i]  # 分子
        a_norm += a_vect[i] ** 2  # a_vect绝对值
        b_norm += b_vect[i] ** 2  # b_vect绝对值
    if a_norm == 0 or b_norm == 0:
        cos = -1
    else:
        cos = dot_val / ((a_norm * b_norm) ** 0.5)

    return cos


'''余弦距离'''


def cosineSimilarity(a_vect, b_vect):
    '''@others'''
    dot_val = 0.0
    a_norm = 0.0
    b_norm = 0.0
    cos = None
    for a, b in zip(a_vect, b_vect):
        dot_val += a * b
        a_norm += a ** 2
        b_norm += b ** 2
    if a_norm == 0.0 or b_norm == 0.0:
        cos = -1
    else:
        cos = dot_val / ((a_norm * b_norm) ** 0.5)
    return cos


'''动态多重list相加 如：[[1, 2, 3], [4, 5, 6], [7, 8, 9]] 每一位对应相加得[12 15 18]'''
'''from liutao 使用numpy转化成矩阵计算'''


# 对上边函数进行了更新
def multi_dynamic_list_sum(multi_list):
    b = np.array(multi_list)
    list_sum = b.sum(axis=0)  # 这里的0也可以是1 为每一个小list求和
    return list_sum


# liyang2018.10.5---------------------------------------------------------------------------------------------------
'''@liyang得到一个A_rate之后乘以的新wordVector'''


def word2vectoMultiA_rate(word, A_rate):
    '''
    :param word: 词语
    :param A_rate: A概率
    :return: a概率*词向量的结果
    '''
    fdir = r'model/'
    model = gensim.models.Word2Vec.load(fdir + 'cauc.incivi.text.model')
    wordVector = model[word]
    newWordVector = listto_matrix_mult_a(wordVector, A_rate)
    return newWordVector


'''@liyang得到一个词的词向量，为了平均词向量准备的'''


def getword2vector_for_averageVs(word):
    '''
    :param word: 词语
    :return: 词向量
    '''
    fdir = 'model/'
    model = gensim.models.Word2Vec.load(fdir + 'cauc.incivi.text.model')
    wordVector = model[word]
    return wordVector


# liyang2018.10.5---------------------------------------------------------------------------------------------------
'''字典根据value进行排序'''


def sortDictForValueWriteCsv(Senteindex, dict):
    '''
    把一个字典根据value进行排序，并保存前10个
    :param Senteindex:外部参数
    :param dict:字典
    :return:
    '''
    csvfile = open('result/simiSifResult.csv', 'a+', encoding='utf-8', newline='')
    csvWrite = csv.writer(csvfile)
    # csvWrite.writerow(('societyIndex','caucnumber' 'cosine'))
    a = sorted(dict.items(), key=lambda item: item[1], reverse=True)  # 核心代码
    countt = 1  # 计时器
    for i, j in a:
        if countt <= 10:
            csvWrite.writerow((Senteindex, i, j))
            countt += 1
        else:
            break
    csvfile.close()


'''判断A B C D个数那个最多就返回时哪一类'''


def getMaxABCD(A, B, C, D):
    strA = None
    if max(A, B, C, D) == A:
        strA = 'A'
    if max(A, B, C, D) == B:
        strA = 'B'
    if max(A, B, C, D) == C:
        strA = 'C'
    if max(A, B, C, D) == D:
        strA = 'D'
    return strA


'''将字典数据存入到二进制文件中'''


def saveDictInBinFile(Dict, filepath):
    '''
    :param Dict: 字典
    :param filepath: 保存路径
    :return:
    '''
    f = open(filepath, 'wb')
    # pickle.dump(1, f)
    pickle.dump(Dict, f)
    f.close
    print('二进制文件保存成功')


'''二进制文件中读入数据并转化为字典'''


def readFromInBinToDict(filepath):
    '''
    将二进制文件读取变成字典
    :param filepath: 二进制文件路径
    :return:字典
    '''
    f = open(filepath, 'rb')  # file为.dat文件
    # pickle.load(f)
    d = pickle.load(f)
    f.close()
    Dict = {}
    Dict = d
    print('二进制文件读取完成')
    return Dict


'''在写入csv文件时为其头部加上列名但是因为to_csv()不知怎么用，所有已就用这个了'''


def setCscHead(filepath, list):
    '''
    :param filepath: 文件路径
    :param list: 列名的集合列表
    :return:
    '''
    csvfile = open(filepath, 'w', encoding='utf-8', newline='')
    csvWrite = csv.writer(csvfile)
    csvWrite.writerow(list)
    csvfile.close()
    print('csv列名写完成')


'''这个函数是为生成好的测试集和训练集 两个字典进行计算的 并把计算结果保存起来'''


def testAndTrainCalculat(testDict, trainDict, testfile, trainfile, resultfile):
    '''
       :param testDict: 测试集字典
       :param trainDict: 训练集字典
       :param testfile: 测试集原文件
       :param trainfile: 训练集原文件
       :param resultfile: 计算结果保存文件
       :return:
       '''
    testdata = pd.read_csv(testfile)
    traindata = pd.read_csv(trainfile)
    COS_DICT = {}
    list = []
    for teindex, tevs in testDict.items():
        for trindex, trvs in trainDict.items():
            cos = cosineSimilarity(tevs, trvs)  # 计算相似度
            COS_DICT.setdefault(trindex, cos)
        a = sorted(COS_DICT.items(), key=lambda item: item[1], reverse=True)  # 字典排序 降序

        list.append(
            [teindex, a[0][0], a[0][1], testdata.loc[teindex - 1, 'classs'], testdata.loc[teindex - 1, 'descrip'],
             traindata.loc[a[0][0] - 1, 'class'], traindata.loc[a[0][0] - 1, 'describe']])
        # 上面这个list中加入的东西比较多包括 testfile里面的下标、类别、句子，trainfile也一样
        COS_DICT.clear()
    # dataframe = pd.DataFrame(list)
    # setCscHead(resultfile,['teindex','trindex','cos','teclass','tedescribe','trclass','trdescribe'])
    # dataframe.to_csv(resultfile,mode='a',index=False,encoding='utf-8',header=False)
    print('测试集认定最max相似完成')


'''这个函数是为生成好的测试集和训练集 两个字典进行计算的 并把计算结果的（前十个）保存起来'''


def testAndTrainCalculatTen(testDict, trainDict, testfile, trainfile, resultfile):
    '''
    :param testDict: 测试集字典
    :param trainDict: 训练集字典
    :param testfile: 测试集原文件
    :param trainfile: 训练集原文件
    :param resultfile: 计算结果保存文件
    :return:
    '''
    testdata = pd.read_csv(testfile)
    traindata = pd.read_csv(trainfile)
    COS_DICT = {}
    list = []
    for teindex, tevs in testDict.items():
        for trindex, trvs in trainDict.items():
            cos = cosineSimilarity(tevs, trvs)  # 计算相似度
            COS_DICT.setdefault(trindex, cos)
        a = sorted(COS_DICT.items(), key=lambda item: item[1], reverse=True)  # 字典排序 降序
        for i in range(10):
            list.append(
                [teindex, a[i][0], a[i][1], testdata.loc[teindex - 1, 'classs'], testdata.loc[teindex - 1, 'descrip'],
                 traindata.loc[a[i][0] - 1, 'class'], traindata.loc[a[i][0] - 1, 'describe']])
        # 上面这个list中加入的东西比较多包括 testfile里面的下标、类别、句子，trainfile也一样
        COS_DICT.clear()
    dataframe = pd.DataFrame(list)
    print('list长度', len(list))
    setCscHead(resultfile, ['teindex', 'trindex', 'cos', 'teclass', 'tedescribe', 'trclass', 'trdescribe'])
    dataframe.to_csv(resultfile, mode='a', index=False, encoding='utf-8', header=False)
    print('测试集认定相似前10个完成')


'''随机选择数据的函数'''


def dataRandomSelectFromDBSoAndCa():
    data = pd.read_csv("F:\研究生课题\数据\DBsociAndCauc.csv")
    datalist = []
    randomlist = []
    for i in range(111):  # 循环几次就是选择出多少条出来
        randmindex = random.randint(1, len(data))
        randomlist.append(randmindex)

    dataSelect = data.ix[randomlist, :]
    print(dataSelect.classs.value_counts() / len(dataSelect))  # 统计每一类的所占的比例

    dataframe = pd.DataFrame(dataSelect)
    dataframe.to_csv('data/DBtestSoAndCa.csv', index=False)
    print('数据选择完成')


'''融合函数 Li_arctan（x）语义融合了处罚规则'''


def Liarctan(testPL, trainPL):
    if testPL == trainPL:
        a = (2 / math.pi) * math.atan(1 / math.fabs(0.001))
    else:
        a = (2 / math.pi) * math.atan(1 / math.fabs(testPL - trainPL))
    return a


def rightRateForTen(testfile, testresult):
    '''前10个，先确定好类，在计算准确率'''
    datatest = pd.read_csv(testfile)
    data = pd.read_csv(testresult)
    datatrindex = data[['trclass']]
    # print(datatrindex)
    # allcount = 1
    count = 0
    A_count = 0
    B_count = 0
    C_count = 0
    D_count = 0
    list = []
    for i in datatrindex.values:
        # print(i)
        if i == 'A':
            A_count += 1
        if i == 'B':
            B_count += 1
        if i == 'C':
            C_count += 1
        if i == 'D':
            D_count += 1
        count += 1
        if count == 10:
            predictClass = getMaxABCD(A_count, B_count, C_count, D_count)
            list.append(predictClass)
            count = 0
            A_count = 0
            B_count = 0
            C_count = 0
            D_count = 0
    print('predictclass列的长度：', len(list))
    datatest['predictClass'] = list
    dataRate = datatest[datatest['classs'] == datatest['predictClass']]
    print('准确个数：', len(dataRate))
    print('准确率：', len(dataRate) / len(datatest))


def rightRateForMax(resultfile):
    '''max准确率求解'''
    data = pd.read_csv(resultfile)
    dataright = data[data['teclass'] == data['trclass']]
    print('总个数：', len(data))
    print('准确个数：', len(dataright))
    print('准确率：', len(dataright) / len(data))

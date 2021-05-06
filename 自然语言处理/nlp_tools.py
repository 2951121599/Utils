# -*-coding:utf-8-*- 
# ���ߣ�   29511
# �ļ���:  nlp_tools.py
# ����ʱ�䣺2021/3/16��17:31

# ���ߺ��������б�
# ���ּ����ܣ�
#
# 1.�ļ�1����д���ļ�2
# 2.�ļ�1���ݷִ�ȥ���Ŵ����ļ�2
# 3.����1���ú���2���зִʺ�ȥ����ȥͣ�ô�
# 4.Ϊ�˼���p(w)��words������ȥ��words����
# 5.[1,2,3]+[4,5,6]=[5,7,9]
# 6.[1,2,3]*2=[2,4,6]
# 7.���Ҿ��� Li
# 8.���Ҿ���
# 9.�õ�һ��A_rate֮����Ե���wordVector
# 10.�õ�һ���ʵĴ�����
# 11.�ֵ����value��������
# 12.'''���ֵ����ݴ��뵽�������ļ���'''
# 13.�������ļ��ж������ݲ�ת��Ϊ�ֵ�'''
# 14.csv�ļ�ʱΪ��ͷ����������
# 15.���Լ���ѵ��������
# 16.���ѡ������
# 17.li arctan(1/|a-b|)
# 18.19.׼ȷ��

import jieba
import numpy as np
import gensim
import csv
import pickle
import pandas as pd
import math

# ���ߺ���
'''
    �����ļ�1����д���ļ�2 ���������ѧϰ���ڶԶ����ļ���д���ļ���
    һ����ʵ�֣����ǽ�txt1�е�����ͨ����ȡȻ����д���ļ�txt2��
    ע���ں�������ʱ��close�����ĵ��÷�ֹ�ڴ�ռ��
'''


def read1ToWrite2(readfile_path, writefile_path):
    fin = open(readfile_path, 'r')  # ·��д����
    fou = open(writefile_path, 'w')
    line = fin.readlines()  # ��s���ǻ�ȡ��������
    for i in line:
        fou.write(i)
    fin.close()
    fou.close()


"""
������������ڵ�һ�������Ļ����Ͻ��иĽ�
������ʹ��jieba���зִʣ��ǰ���һ�н��ж�ȡ��ͬʱ�����˷ִ�ģʽ��
��ʹ���˼򵥴ֱ��ķ��������˶��ŵ��ַ���ȥ��
ͬʱ��������д����һ���ļ���    
"""


# �ļ�1���ݷִ�ȥ���Ŵ����ļ�2
def cutWordTofile(writefile_path, cutWordfile_path):
    fin = open(writefile_path, 'r')  # ·��д����
    fou = open(cutWordfile_path, 'w')
    line = fin.readline()
    while line:
        newline = ' '.join(jieba.cut(line, cut_all=False)).replace('��', '').replace('��', '')  # ��ͷִʲ�ȥ������
        fou.write(newline)
        line = fin.readline()  # ÿ�θ���һ��line�൱��i++
    fin.close()
    fou.close()


"""
��κ��������ܹ���������������ǽ�һ���ĸĽ���������ͣ�ôʵ�ȥ��
��ʵ����ͣ�ôʵĶ�̬����
����һִ���ļ��Ķ�д����������1���ú���2���зִʺ�ȥ����ȥͣ�ôʵȲ���
"""


# �����ļ��ִ�֮������ļ��м���������(1,2,)�ĵ���ʹ���߽��зָ�
# --------------------------------------------------------------------------------------------------------
# 1�����ļ��ִ�֮������ļ�
def readCutRemovewrite(readfile_path, writefile_path):
    inputs = open(readfile_path, 'r', encoding='utf-8')
    outputs = open(writefile_path, 'w', encoding='utf8')
    for line in inputs:
        line_seg = seg_sentence(line)  # ����ķ���ֵ���ַ���
        outputs.write(line_seg + '\n')
    outputs.close()
    inputs.close()


# 2���ӷִʲ�ȥͣ�ô�
def seg_sentence(sentence):
    # 2����ͣ�ô�list
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
���������Ϊ�˼���p(w),�ڷִʵ�ͬʱ��¼��������
1����words����
2ȥ��words����
3ÿһ��Ψһword�ĸ���
����д���ļ�����
"""


def get_words_Word_wordRate(readFilePath, writeFilePath):
    with codecs.open(readFilePath, 'r', 'utf8') as f:
        txt = f.read()
    fout = open(writeFilePath, 'w', encoding='utf-8')
    seg_list = jieba.cut(txt)
    c = Counter()  # �ں����������̳����ֵ���
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
    for key, value in c.most_common():  # 5���Ƿ���5�����޲��� ��������
        # print('%s  %d' % (key,   round(value/count, 5)))#other write
        # print(key, ' '*3, value, ' '*3,  round(value/count, 10))
        writestr = key + ' ' * 10 + str(round(value / count, 10)) + '\n'  # ͨ��str��intת��string
        fout.write(writestr)
    f.close()
    fout.close()


'''����@liyang ������list[] ��ÿһ��ֵ��Ӧ�����[1,2,3]+[4,5,6]=[5,7,9]
 ����ֵΪ���б�ĳ��Ⱥ� ����'''


# ����������˸���ʹ���˾���multi_dynamic_list_sum(multi_list)
def two_list_sum(alist, blist):
    c = [a[i] + b[i] for i in range(min(len(a), len(b)))]
    return c


'''����@liyang ��list[] ��ÿһ��ֵ��Ӧ���һ����a��[1,2,3]*2=[2,4,6]
 ����ֵΪ���б������'''


def list_mult_a(listt, a):
    # ���棬��list�ĺܴ������ݶ���С�����ڣ�aҲ��С��ʱ��
    # ��������ᱨ��˵a������float���� ��ʵ�ʼ���������ǿ�Ϊfloat��
    b = [i * a for i in listt]
    return b


'''���Ƕ���һ�������ĸĽ� ��ɾ����ڳ˷�ֹ��������'''


def listto_matrix_mult_a(list, a):
    b = np.array(list)
    c = b * a
    return c


'''���룺����������������
    ���: ���ߵ����Ҿ���'''


def cosineSimilarity_Li(a_vect, b_vect):
    '''@liyang'''
    dot_val = 0.0
    a_norm = 0.0
    b_norm = 0.0
    cos = None

    for i in range(min(len(a_vect), len(b_vect))):
        dot_val += a_vect[i] * b_vect[i]  # ����
        a_norm += a_vect[i] ** 2  # a_vect����ֵ
        b_norm += b_vect[i] ** 2  # b_vect����ֵ
    if a_norm == 0 or b_norm == 0:
        cos = -1
    else:
        cos = dot_val / ((a_norm * b_norm) ** 0.5)

    return cos


'''���Ҿ���'''


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


'''��̬����list��� �磺[[1, 2, 3], [4, 5, 6], [7, 8, 9]] ÿһλ��Ӧ��ӵ�[12 15 18]'''
'''from liutao ʹ��numpyת���ɾ������'''


# ���ϱߺ��������˸���
def multi_dynamic_list_sum(multi_list):
    b = np.array(multi_list)
    list_sum = b.sum(axis=0)  # �����0Ҳ������1 Ϊÿһ��Сlist���
    return list_sum


# liyang2018.10.5---------------------------------------------------------------------------------------------------
'''@liyang�õ�һ��A_rate֮����Ե���wordVector'''


def word2vectoMultiA_rate(word, A_rate):
    '''
    :param word: ����
    :param A_rate: A����
    :return: a����*�������Ľ��
    '''
    fdir = r'model/'
    model = gensim.models.Word2Vec.load(fdir + 'cauc.incivi.text.model')
    wordVector = model[word]
    newWordVector = listto_matrix_mult_a(wordVector, A_rate)
    return newWordVector


'''@liyang�õ�һ���ʵĴ�������Ϊ��ƽ��������׼����'''


def getword2vector_for_averageVs(word):
    '''
    :param word: ����
    :return: ������
    '''
    fdir = 'model/'
    model = gensim.models.Word2Vec.load(fdir + 'cauc.incivi.text.model')
    wordVector = model[word]
    return wordVector


# liyang2018.10.5---------------------------------------------------------------------------------------------------
'''�ֵ����value��������'''


def sortDictForValueWriteCsv(Senteindex, dict):
    '''
    ��һ���ֵ����value�������򣬲�����ǰ10��
    :param Senteindex:�ⲿ����
    :param dict:�ֵ�
    :return:
    '''
    csvfile = open('result/simiSifResult.csv', 'a+', encoding='utf-8', newline='')
    csvWrite = csv.writer(csvfile)
    # csvWrite.writerow(('societyIndex','caucnumber' 'cosine'))
    a = sorted(dict.items(), key=lambda item: item[1], reverse=True)  # ���Ĵ���
    countt = 1  # ��ʱ��
    for i, j in a:
        if countt <= 10:
            csvWrite.writerow((Senteindex, i, j))
            countt += 1
        else:
            break
    csvfile.close()


'''�ж�A B C D�����Ǹ����ͷ���ʱ��һ��'''


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


'''���ֵ����ݴ��뵽�������ļ���'''


def saveDictInBinFile(Dict, filepath):
    '''
    :param Dict: �ֵ�
    :param filepath: ����·��
    :return:
    '''
    f = open(filepath, 'wb')
    # pickle.dump(1, f)
    pickle.dump(Dict, f)
    f.close
    print('�������ļ�����ɹ�')


'''�������ļ��ж������ݲ�ת��Ϊ�ֵ�'''


def readFromInBinToDict(filepath):
    '''
    ���������ļ���ȡ����ֵ�
    :param filepath: �������ļ�·��
    :return:�ֵ�
    '''
    f = open(filepath, 'rb')  # fileΪ.dat�ļ�
    # pickle.load(f)
    d = pickle.load(f)
    f.close()
    Dict = {}
    Dict = d
    print('�������ļ���ȡ���')
    return Dict


'''��д��csv�ļ�ʱΪ��ͷ����������������Ϊto_csv()��֪��ô�ã������Ѿ��������'''


def setCscHead(filepath, list):
    '''
    :param filepath: �ļ�·��
    :param list: �����ļ����б�
    :return:
    '''
    csvfile = open(filepath, 'w', encoding='utf-8', newline='')
    csvWrite = csv.writer(csvfile)
    csvWrite.writerow(list)
    csvfile.close()
    print('csv����д���')


'''���������Ϊ���ɺõĲ��Լ���ѵ���� �����ֵ���м���� ���Ѽ�������������'''


def testAndTrainCalculat(testDict, trainDict, testfile, trainfile, resultfile):
    '''
       :param testDict: ���Լ��ֵ�
       :param trainDict: ѵ�����ֵ�
       :param testfile: ���Լ�ԭ�ļ�
       :param trainfile: ѵ����ԭ�ļ�
       :param resultfile: �����������ļ�
       :return:
       '''
    testdata = pd.read_csv(testfile)
    traindata = pd.read_csv(trainfile)
    COS_DICT = {}
    list = []
    for teindex, tevs in testDict.items():
        for trindex, trvs in trainDict.items():
            cos = cosineSimilarity(tevs, trvs)  # �������ƶ�
            COS_DICT.setdefault(trindex, cos)
        a = sorted(COS_DICT.items(), key=lambda item: item[1], reverse=True)  # �ֵ����� ����

        list.append(
            [teindex, a[0][0], a[0][1], testdata.loc[teindex - 1, 'classs'], testdata.loc[teindex - 1, 'descrip'],
             traindata.loc[a[0][0] - 1, 'class'], traindata.loc[a[0][0] - 1, 'describe']])
        # �������list�м���Ķ����Ƚ϶���� testfile������±ꡢ��𡢾��ӣ�trainfileҲһ��
        COS_DICT.clear()
    # dataframe = pd.DataFrame(list)
    # setCscHead(resultfile,['teindex','trindex','cos','teclass','tedescribe','trclass','trdescribe'])
    # dataframe.to_csv(resultfile,mode='a',index=False,encoding='utf-8',header=False)
    print('���Լ��϶���max�������')


'''���������Ϊ���ɺõĲ��Լ���ѵ���� �����ֵ���м���� ���Ѽ������ģ�ǰʮ������������'''


def testAndTrainCalculatTen(testDict, trainDict, testfile, trainfile, resultfile):
    '''
    :param testDict: ���Լ��ֵ�
    :param trainDict: ѵ�����ֵ�
    :param testfile: ���Լ�ԭ�ļ�
    :param trainfile: ѵ����ԭ�ļ�
    :param resultfile: �����������ļ�
    :return:
    '''
    testdata = pd.read_csv(testfile)
    traindata = pd.read_csv(trainfile)
    COS_DICT = {}
    list = []
    for teindex, tevs in testDict.items():
        for trindex, trvs in trainDict.items():
            cos = cosineSimilarity(tevs, trvs)  # �������ƶ�
            COS_DICT.setdefault(trindex, cos)
        a = sorted(COS_DICT.items(), key=lambda item: item[1], reverse=True)  # �ֵ����� ����
        for i in range(10):
            list.append(
                [teindex, a[i][0], a[i][1], testdata.loc[teindex - 1, 'classs'], testdata.loc[teindex - 1, 'descrip'],
                 traindata.loc[a[i][0] - 1, 'class'], traindata.loc[a[i][0] - 1, 'describe']])
        # �������list�м���Ķ����Ƚ϶���� testfile������±ꡢ��𡢾��ӣ�trainfileҲһ��
        COS_DICT.clear()
    dataframe = pd.DataFrame(list)
    print('list����', len(list))
    setCscHead(resultfile, ['teindex', 'trindex', 'cos', 'teclass', 'tedescribe', 'trclass', 'trdescribe'])
    dataframe.to_csv(resultfile, mode='a', index=False, encoding='utf-8', header=False)
    print('���Լ��϶�����ǰ10�����')


'''���ѡ�����ݵĺ���'''


def dataRandomSelectFromDBSoAndCa():
    data = pd.read_csv("F:\�о�������\����\DBsociAndCauc.csv")
    datalist = []
    randomlist = []
    for i in range(111):  # ѭ�����ξ���ѡ�������������
        randmindex = random.randint(1, len(data))
        randomlist.append(randmindex)

    dataSelect = data.ix[randomlist, :]
    print(dataSelect.classs.value_counts() / len(dataSelect))  # ͳ��ÿһ�����ռ�ı���

    dataframe = pd.DataFrame(dataSelect)
    dataframe.to_csv('data/DBtestSoAndCa.csv', index=False)
    print('����ѡ�����')


'''�ںϺ��� Li_arctan��x�������ں��˴�������'''


def Liarctan(testPL, trainPL):
    if testPL == trainPL:
        a = (2 / math.pi) * math.atan(1 / math.fabs(0.001))
    else:
        a = (2 / math.pi) * math.atan(1 / math.fabs(testPL - trainPL))
    return a


def rightRateForTen(testfile, testresult):
    '''ǰ10������ȷ�����࣬�ڼ���׼ȷ��'''
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
    print('predictclass�еĳ��ȣ�', len(list))
    datatest['predictClass'] = list
    dataRate = datatest[datatest['classs'] == datatest['predictClass']]
    print('׼ȷ������', len(dataRate))
    print('׼ȷ�ʣ�', len(dataRate) / len(datatest))


def rightRateForMax(resultfile):
    '''max׼ȷ�����'''
    data = pd.read_csv(resultfile)
    dataright = data[data['teclass'] == data['trclass']]
    print('�ܸ�����', len(data))
    print('׼ȷ������', len(dataright))
    print('׼ȷ�ʣ�', len(dataright) / len(data))

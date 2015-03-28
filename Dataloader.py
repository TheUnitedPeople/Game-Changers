import yaml
import codecs

__author__ = 'iacusm'


def loadFile(filepath):
    dataobj = yaml.load(codecs.open(filepath, 'r', encoding='utf-8'))
    return dataobj


# Must be a list only
def returnList(dataobj):
    return dataobj

    
def debugPrint(dataobj):
    print(dataobj)

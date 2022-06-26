#生成邮箱列表，生成的列表需要去宝塔导入下才能用
def getMail():
    list = []
    i = 0
    file_handle = open('sum.txt',mode='w')
    for num in range(1,11): #1-10
        source='%d'%num+'.txt'
        with open(source,"r") as f:
            data=f.read().splitlines()
        class Mail:
            def _init_(self):
                self.name=''
                self.mailaddr=''
                self.secretcode=''
                self.volumn=''
        for data_ in data:
            data_=data_.lower()
            list.append(Mail())
            list[i].name=data_
            list[i].mailaddr=data_+'@bufermail.com'
            list[i].secretcode='A'+data_+'168168'
            list[i].volumn='0.5'
            file_handle.write(list[i].name + '|' + list[i].mailaddr + '|' + list[i].secretcode + '|' + list[i].volumn + '|GB\n')  #归并到sum.txt中，便于宝塔邮局批量添加地址
            i=i+1
    return list





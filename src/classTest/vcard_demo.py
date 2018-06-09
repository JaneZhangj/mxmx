
"""
批量生成二维码名片
"""
import qrcode

def vcard_demo():
    #读取文件中的姓名和手机号信息
    file = open('contactInformation.txt', mode='r', encoding='utf-8')
    rows = file.read().split('\n')

    for row in rows:
        split_row = row.split(',')
        name = split_row[0]  #取出姓名字段的值
        phone = split_row[1]  #取出手机号字段的值

        vstr = 'BEGIN:VCARD\n'+'FN:'+name+'\nTEL:'+phone+'\nEND:VCARD'  #定义vcard的值

        #调用qrcode生成二维码
        qr = qrcode.QRCode(version=2,
                           error_correction=qrcode.ERROR_CORRECT_L,
                           box_size=10,
                           border=20)
        qr.add_data(vstr)
        qr.make(fit=True)
        img = qr.make_image()
        img.save('%s的名片.jpg' %name)


if __name__ == '__main__':
    vcard_demo()

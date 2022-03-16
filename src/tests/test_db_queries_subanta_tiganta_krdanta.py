from src.source.Model.AmaraKosha_Database_Queries import *
if __name__ == '__main__':
    cols, lines = sqlQueryUnicode('Select * from Subanta where Base = ?', "अंशक") #×èÔÏè
    print('Subanta: %s\n%s'%(cols, lines))
    cols, lines = sqlQueryUnicode('Select * from Subanta where Base = ?', 'अंशुमती') #×èÔÏè
    print('Subanta: %s\n%s'%(cols, lines))
    cols, lines = sqlQueryUnicode('Select * from SubFin where Finform = ?', 'राम')
    print('SubFin: %s\n%s' % (cols, lines))
    cols, lines = sqlQueryUnicode('select * from stinfin where field2 = ? and field3 = ?', (383, "1A"))
    print('stinfin: %s\n%s' % (cols, lines))

    cols, lines = sqlQueryUnicode('select * from Sdhatu where field2 = ? ', 'अंश्')
    print('Sdhatu: %s\n%s' % (cols, lines))

    cols, data = tblSelectUnicode('sdhatu')
    print('sdhatu: %s\n%s' % (cols, data))

    cols, lines = sqlQueryUnicode('select * from krud where field4=? and field5=?', ('a1', 383))
    print('krud: %s\n%s' % (cols,lines))

    cols, lines = sqlQueryUnicode('Select * from Amara_Words where Word = ?', 'स्वर्') #×èÔÏè
    print('Amara_words: %s\n%s'%(cols, lines))

    for i in range(5):
        gana = str(i) if i > 0 else ''
        cols, lines = sqlQueryUnicode('select * from Sdhatu where cast(field9 as text) like ?', gana + '__')
        print('%d Sdhatu: gana %s' % (i, cols))
        for line in lines: print(line)
    for i in range(4):
        cols, lines = sqlQueryUnicode('select * from Sdhatu where cast(field9 as text) like ?', '_' + str(i) + '_')
        print('%d Sdhatu: padi %s' % (i, cols))
        for line in lines: print(line)
    for i in range(3):
        cols, lines = sqlQueryUnicode('select * from Sdhatu where cast(field9 as text) like ?', '__' + str(i))
        print('%d Sdhatu: it %s' % (i, cols))
        for line in lines: print(line)

    tbls = schemaParse()
    print('tables %s' % tbls)

    cols, lines = sqlQueryUnicode('Select su.base, su.erb, su.code, sf.sufstr from Subanta su, sufcode sf where Base = ? and sf.code = substr(su.code,1, 4)', 'अंशुमती')
    print('Subanta/Sufcode: %s\n%s'%(cols, lines))

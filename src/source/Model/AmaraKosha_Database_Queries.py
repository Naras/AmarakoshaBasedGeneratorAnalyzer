__author__ = 'NarasMG'

import peewee, os
from ..Controller.iscii2utf8 import *
conn_unicode = peewee.SqliteDatabase(os.getcwd() + '\Amarakosha.db', pragmas={'journal_mode': 'wal','cache_size': -1024 * 64})
maxrows = 5

mypar = Parser()
mypar.set_script(1)
def flatMap(f, li):
    mapped = map(f, li)
    flattened = flatten_single_dim(mapped)
    yield from flattened
def flatten_single_dim(mapped):
    for item in mapped:
        for subitem in item:
            yield subitem

# isascii = lambda s: len(s) == len(s.encode())
def isascii(s):
    # import re
    # return re.search('[^\x00-\x7F]', s) is None
    try:
        s.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False
def iscii_unicode(iscii_string, script=1):
    mypar.set_script(script)
    flush = 0
    x_as_List = [ord(char) for char in iscii_string+' ']
    n = mypar.iscii2utf8(x_as_List, flush)
    # y = x[n:]
    return ''.join([ch for ch in mypar.write_output()])
def unicode_iscii(unicode_string, script=1):
    mypar.set_script(script)
    try:
        scripts_map_unicode = mypar.make_script_maps_unicode_to_iscii()
        result_as_list = []
        for i, ch in enumerate(unicode_string):
            # print('ch %s hex %s dec %s'%(ch, hex(ord(ch)), ord(ch)))
            result_as_list.append(chr(scripts_map_unicode[ord(ch)]))
            if ord(ch) in nukta_specials.values(): result_as_list.append(chr(ISCII_NUKTA))
        return ''.join(result_as_list)
    except Exception as e:
        raise Exception('unicode_iscii: character %s unicode-string %s character %s' % (e, unicode_string, ch))
def schemaParse():
    cursor = conn_unicode.get_tables()
    mypar = Parser()
    mypar.set_script(1)
    tbls = []
    for row in cursor:
        tbls.append(row)
    return tbls
def sqlQueryUnicode(sql, param=None, maxrows=5, duplicate=False, script=1):
    # lstParam = [x for x in param] if isinstance(param,tuple) else param
    # print('sql=%s param=%s'%(sql, lstParam))
    current = 0
    if param==None: rowcursor = conn_unicode.execute_sql(sql)
    else:
        if not isinstance(param,tuple): param = (param,)
        rowcursor = conn_unicode.execute_sql(sql, param)
    try:
        result = []
        for r in rowcursor.fetchall():
            # print(r)
            resultRow = []
            for field in r:
                # resultRow.append(field)
                if isascii(str(field)):
                    resultRow.append(field)
                    if duplicate: resultRow.append(field)
                else:
                    resultRow.append(field)
                    if duplicate: resultRow.append(unicode_iscii(field))
            result += [resultRow]
            current += 1
            if maxrows > 0 and current > maxrows:
                break
    except IllegalInput as e:
        logging.warning('%s' % e)

    columns = [column[0] for column in rowcursor.description]
    if duplicate: columns = list(flatMap(lambda x: (x, x), columns))
    return columns, result
def tblSelectUnicode(table_name,maxrows=5,duplicate=False, script=1):
    current = 0
    rowcursor = conn_unicode.execute_sql('select * from ' + table_name)
    try:
        tbl = []
        for r in rowcursor.fetchall():
            # print(r)
            tblRow = []
            for field in r:
                if isascii(str(field)):
                    tblRow.append(field)
                    if duplicate: tblRow.append(field)
                else:
                    tblRow.append(field)
                    if duplicate: tblRow.append(unicode_iscii(str(field), script))
            tbl += [tblRow]
            current += 1
            if maxrows > 0 and current > maxrows:
                break
    except IllegalInput as e:
        logging.warning('%s' % e)
    columns = [column[0] for column in rowcursor.description]
    if duplicate: columns = list(flatMap(lambda x: (x, x), columns))

    return columns, tbl






import io
import json
from zipfile import ZipFile
import time

buf = io.BytesIO()

with ZipFile(buf, 'w') as file:
    with io.BytesIO() as json_buf:
        data = json.dumps({'a':'1', 'b':'1'})
        json_buf.write(data.encode())
        json_buf.seek(0)
        print(json_buf.read())
        file.writestr('1.json', json_buf.read())
        print('Time sleep...')
        time.sleep(30000)

'''with open('1.zip', 'wb') as file:
    buf.seek(0)
    file.write(buf.read())'''

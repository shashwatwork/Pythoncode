from urllib import request

csv_url='https://www.ibm.com/support/knowledgecenter/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/AssetsImportCompleteSample.csv?view=kc'

def download_stock(url_csv):
    response=request.urlopen(url_csv)
    sc= response.read()
    csv_str=str(sc)
    lines=csv_str.split("\\n")
    dest_url=r'sample.csv'
    fx=open(dest_url,'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_stock(csv_url)
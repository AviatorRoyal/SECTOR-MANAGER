con_dir='./configs/'
while True:
    print('''
    ENTER 1 TO USE PREVIOUS CONFIG FILES
    ENTER 2 TO USE NEW CONFIG FILE
    ENTER 3 TO exit
      ''')
    ch1=str(input('enter your selection'))
    if ch1=='1':
        k=input('enter name of config_file-(without .txt)-')
        try:
            config_file=open(str(con_dir+k+'.con'),'r')
            print('file succesfully recognised')
        except:
            print('File not found')
    elif ch1=='2':
        k=input('enter name of config_file-(without .txt)-')
        config_file=open(str(con_dir+k+'.con'),'w')
        print('config named,',k,' has been succesfully made')
        
    elif ch1=='3':
        print('closed')
        break
    else:
        print('incorrect choice')

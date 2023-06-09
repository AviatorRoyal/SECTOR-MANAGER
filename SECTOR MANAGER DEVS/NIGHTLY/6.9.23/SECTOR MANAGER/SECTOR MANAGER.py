while True:
    print('''
    ENTER 1 TO USE PREVIOUS CONFIG FILES
    ENTER 2 TO USE NEW CONFIG FILE
    ENTER 3 TO exit
      ''')
    ch1=int(input('enter your selection'))
    if ch1==1:
        k=input('enter name of config_file-(without txt)-')
    elif ch1==2:
        k=input('enter name of config_file-(without txt)-')
        con_dir='./configs/'+k
        config_file=open(con_dir,'w')
        print('config named,',k,' has been succesfully made')
        

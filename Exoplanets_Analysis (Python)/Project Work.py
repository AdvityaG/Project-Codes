import pandas as pd
import matplotlib.pyplot as plt
pro=pd.read_csv("C:\\Kids\\Advitya\\Class 12\\IP Work\\Project Work\\Nasa Exoplanet Final Data.csv"
                ,usecols=[0,1,2,3,4,7,10,11,12,13,14,15,16,17,18,19])

d=0             #Not includes columns=5,6,8,9
while True:
    if d==4:
        print('''
Thanks for playing :-)
-----------------------------------------------------''')
        break
        
    print('''
          WELCOME TO NASA'S EXOPLANET DATA 
          --------------------------------
          
Main Menu:
1. Reading Data
2. Datafram Details
3. Data Visualisation
4. Quit''')
    d=int(input("Enter your choice number- "))
    while True:
        if d==1:
            print('''Reading Data Menu:
1. Display all details of all Exoplanets (entire DataFrame)
2. Display details about a particular exoplanet
3. Display a particular column/property
4. Display 'n' closest exoplanets
5. Display top 'n' biggest exoplanets
6. Display top 'n' smallest exoplanets
7. Display type of particular exoplanet
8. Display exoplanets of particular type
9. Display detection method of particular exoplanet
10. Display 'n' heaviest exoplanets 
11. Display 'n' brightest exoplanets
12. Display 'n' dimmest exoplanets 
13. Display 'n' exoplanets with biggest orbital radius
14. Display 'n' exoplanets with smallest orbital radius
15. Display 'n' exoplanets with longest revolution
16. Display 'n' exoplanets with smallest revolution
                  ''')
            read=int(input("Enter your choice number-"))
            while True:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                if read==1:
                    print(pro.iloc[:,0:11])
                    read=0
                    break
    
                elif read==2:
                    pla=str(input("Enter the name of exoplanet-"))
                    te=0
                    for ab in range(938):
                        if pro.loc[ab,"Name"]==pla:
                            print(pro.iloc[:,0:11][pro.loc[:,"Name"]==pla])
                            te=1
                    break        
                                     
                    if te==0:
                        print("Sorry! that is not a exoplanet or we don't have it in our data")
                        read=0
                        break
        
                elif read==3:
                    par=input("Enter the column/property-")
                    li=pro.columns
                    if par in li:
                        print(pro[par])
                        break
                    else:
                        print("Sorry! we don't have the data about that column/property")
                        read=0
                        break
                        
                elif read==4:
                    cl=int(input("Enter no. of closest exoplanets you want to see-"))
                    if cl<=938 and cl>=0:
                        so=pro.sort_values(by="distanceForCal")
                        print(so.iloc[0:cl,0:11])
                        break
                        
                    else:
                        print("Sorry! We have the data for only 938 exoplanets")
                        break
                    
                elif read==5:
                    bi=int(input("Enter no. of biggest exoplanets you want to see-"))
                    if bi<=938 and bi>=0:
                        bg=pro.sort_values(by="radiusForCal",ascending=False)
                        print(bg.iloc[0:bi,0:11])
                        break
                    
                    else:
                        print("Sorry! We have the data for only 938 exoplanets")
                        break
                        
                elif read==6:
                    sl=int(input("Enter no. of smallest exoplanets you want to see-"))
                    if sl<=938 and sl>=0:
                        sm=pro.sort_values(by="radiusForCal")
                        print(sm.iloc[0:sl,0:11])
                        break
                    
                    else:
                        print("Sorry! We have the data for only 938 exoplanets")
                        break
                        
                elif read==7:
                    ty=input("Enter the name of the planet-")
                    pa=0
                    for ac in range(938):
                        if pro.loc[ac,"Name"]==ty:
                            print(pro.loc[:,"Planet_Type"][pro.loc[:,"Name"]==ty])
                            pa=1
                    break
                                
                    if pa==0:
                        print("Sorry! that is not a exoplanet or we don't have it in our data")
                        read=0
                        break
                        
                elif read==8:
                    pr=input("Enter the type of exoplanet-")
                    pe=0
                    for ad in range(938):
                        if pro.loc[ad,"Planet_Type"]==pr:
                            print(pro.iloc[:,0:11][pro.loc[:,"Planet_Type"]==pr])
                            pe=1
                            break
                    break
                
                    if pe==0:
                        print("Sorry! that is not a planet type or we don't have a exoplanet of that type in our data")
                        read=0
                        break
                    
                elif read==9:
                    dm=input("Enter the name of the planet-")
                    dp=0
                    for ae in range(938):
                        if pro.loc[ae,"Name"]==dm:
                            print(pro.loc[:,"Detection_Method"][pro.loc[:,"Name"]==dm])
                            dp=1
                    break
                                
                    if dp==0:
                        print("Sorry! that is not a exoplanet or we don't have it in our data")
                        read=0
                        break
                        
                elif read==10:
                    he=int(input("Enter no. of heaviest exoplanets you want to see-"))
                    if he<=938 and he>=0:
                        hv=pro.sort_values(by="massForCal",ascending=False)
                        print(hv.iloc[0:he,0:11])
                        break
                    
                    else:
                        print("Sorry! We have the data for only 938 exoplanets")
                        break
                        
                elif read==11:
                    br=int(input("Enter no. of brightest exoplanets you want to see-"))
                    if br<=938 and br>=0:
                        bh=pro.sort_values(by="Stellar_Magnitude")
                        print(bh.iloc[0:br,0:11])
                        break
                    
                    else:
                        print("Sorry! We have the data for only 938 exoplanets")
                        break
                    
                elif read==12:
                    dm=int(input("Enter no. of dimmest exoplanets you want to see-"))
                    if dm<=938 and dm>=0:
                        di=pro.sort_values(by="Stellar_Magnitude",ascending=False)
                        print(di.iloc[0:dm,0:11])
                        break
                        
                    else:
                        print("Sorry! We have the data for only 938 exoplanets")
                        break
                    
                elif read==13:
                    ob=int(input("Enter no. of biggest orbital radius exoplanets you want to see-"))
                    if ob<=938 and ob>=0:
                        ot=pro.sort_values(by="orForCal",ascending=False)
                        print(ot.iloc[0:ob,0:11])
                        break
                        
                    else:
                        print("Sorry! We have the data for only 938 exoplanets")
                        break
                    
                elif read==14:
                    sm=int(input("Enter no. of smallest orbital radius exoplanets you want to see-"))
                    if sm<=938 and sm>=0:
                        sr=pro.sort_values(by="orForCal")
                        print(sr.iloc[0:sm,0:11])
                        break
                        
                    else:
                        print("Sorry! We have the data for only 938 exoplanets")
                        break
                        
                elif read==15:
                    lr=int(input("Enter no. of longest revolution exoplanets you want to see-"))
                    if lr<=938 and lr>=0:
                        le=pro.sort_values(by="opForCal",ascending=False)
                        print(le.iloc[0:lr,0:11])
                        break
                        
                    else:
                        print("Sorry! We have the data for only 938 exoplanets")
                        break
                        
                elif read==16:
                    sr=int(input("Enter no. of smallest revolution exoplanets you want to see-"))
                    if sr<=938 and sr>=0:
                        se=pro.sort_values(by="opForCal")
                        print(se.iloc[0:sr,0:11])
                        break
                        
                    else:
                        print("Sorry! We have the data for only 938 exoplanets")
                        break
                else:
                    read=int(input("Please enter a valid choice number-"))
                    continue
             
            break
            
        elif d==2:
            print('''Dataframe Deatils menu:
1. Display all column names
2. Display all indices 
3. Display size of dataframe
4. Display shape of dataframe
5. Display dimensions of dataframe
6. Display total no. of rows
7. Display total no. of columns
    ''')
            
            dat=int(input("Enter your choice number-"))
            while True:
                if dat==1:
                    print("All the columns are-")
                    print(pro.columns)
                    break
                
                if dat==2:
                    print("All the rows are-")
                    print(pro.index)
                    break
                
                if dat==3:
                    print("The size of the dataframe is",pro.size)
                    break
                
                if dat==4:
                    print("The shape of datfarme is-", pro.shape)
                    break
                    
                if dat==5:
                    print("The dimensions of datframe is-", pro.ndim)
                    break
                    
                if dat==6:
                    print("Total no. of rows are-",len(pro))
                    break
                    
                if dat==7:
                    colcou=pro.columns
                    print("Total no. of columns are-", len(colcou)-5)
                    break
                    
                else:
                    dat=(input("Please enter a valid choice number-"))
                    continue
            break
        elif d==3:
            print(''''Date Visualisation menu:
1. Ananlyis by Discovery Year
2. Amount of Exoplanet Types
3. Usage of Detection Method of Exoplanets
4. Radius V/S Mass of Exoplanets 
5. Distance V/S Radius of Exoplanets
6. Mass V/S Distance of Exoplanets
7. Optical Radius V/S Optical Period of Exoplanets
    ''')
            vis=int(input("Enter choice no.-"))
            while True:
                if vis==1:
                    disc=pro["Discovery_Year"]
                    xax=[]
                    for i in disc:
                        xax.append(i)    
                    
                    plt.hist(xax,bins=[1990,1995,2000,2005,2010,2015,2020,2023],rwidth=0.9,color="gold")
                    plt.xlabel("Discovery Years",color="seagreen",fontsize=14)
                    plt.ylabel("No. of Exoplanets discovered",color="seagreen",fontsize=14)
                    plt.title("Exopanets' Discovery Years",color="royalblue",fontsize=18)
                    plt.show()
                    break         
                elif vis==2:
                    grty=input('''What type of graph do you want:
1. Vertical histogram
2. Horizonatal histogram
3. Pie chart
4. Vertcal bar graph
5. Horizontal bar graph
                               
Enter graph type-''').capitalize()
                    while True:
                        if grty=="Vertical histogram":
                            typ=pro["Planet_Type"] 
                            ty=[]
                            for i in typ:
                                ty.append(i)
    
                            plt.hist(ty, color="darkorange")
                            plt.xlabel("Exoplanet Types",color="darkgreen", fontsize=14)
                            plt.ylabel("No. of Exoplanets",color="darkgreen", fontsize=14)
                            plt.title("Amount of Exoplanet types",color="navy", fontsize=18)
                            plt.show()
                            break
                        elif grty=="Horizontal histogram":
                            typ=pro["Planet_Type"] 
                            ty=[]
                            for i in typ:
                                ty.append(i)
    
                            plt.hist(ty, color="darkorange",orientation="horizontal")
                            plt.ylabel("Exoplanet Types",color="darkgreen", fontsize=14)
                            plt.xlabel("No. of Exoplanets",color="darkgreen", fontsize=14)
                            plt.title("Amount of Exoplanet types",color="navy", fontsize=18)
                            plt.show()
                            break
                        elif grty=="Pie chart":
                            countGG=0
                            countNl=0
                            countSE=0
                            countTer=0
                            for i in ty:
                                if i=="Gas Giant":
                                    countGG+=1
                                if i=="Neptune-like":
                                    countNl+=1
                                if i=="Super Earth":
                                    countSE+=1
                                if i=="Terrestrial":
                                    countTer+=1
    
                            siz=[countGG,countNl,countSE,countTer]
                            typena=["Gas Giant","Neptune-like","Super Earth","Terrestrial"]
                            plt.pie(siz,labels=typena,colors=["c",'y','g','b'],shadow=True, explode=[0.05,0.05,0.05,0.05])
                            plt.title("Amount of Exoplanet types",color="navy", fontsize=18)
                            plt.show()
                            break
                        
                        elif grty=="Vertical bar graph":
                            typ=pro["Planet_Type"]     
                            countg=0
                            countn=0
                            counts=0
                            countt=0
                            for i in typ:
                                if i=="Gas Giant":
                                    countg+=1
                                if i=="Neptune-like":
                                    countn+=1
                                if i=="Super Earth":
                                    counts+=1
                                if i=="Terrestrial":
                                    countt+=1
                                    
                            finl=[countg,countn,counts,countt]
                            print(finl)
                            pla=["Gas Giant","Neptune-like","Super Earth","Terrestrial"]
                            plt.bar(pla,finl)
                            plt.xlabel("Exoplanet Type",color="darkgreen", fontsize=14)
                            plt.ylabel("No. of Planets",color="darkgreen", fontsize=14)
                            plt.title("Amount of Exoplanet types",color="navy", fontsize=18)
                            plt.show()
                            break
                        
                        elif grty=="Horizontal bar graph":
                            typ=pro["Planet_Type"]     
                            countg=0
                            countn=0
                            counts=0
                            countt=0
                            for i in typ:
                                if i=="Gas Giant":
                                    countg+=1
                                if i=="Neptune-like":
                                    countn+=1
                                if i=="Super Earth":
                                    counts+=1
                                if i=="Terrestrial":
                                    countt+=1
                                    
                            finl=[countg,countn,counts,countt]
                            print(finl)
                            pla=["Gas Giant","Neptune-like","Super Earth","Terrestrial"]
                            plt.barh(pla,finl)
                            plt.ylabel("Exoplanet Types",color="darkgreen", fontsize=14)
                            plt.xlabel("No. of Exoplanets",color="darkgreen", fontsize=14)
                            plt.title("Amount of Exoplanet types",color="navy", fontsize=18)
                            plt.show()
                            break
                            
                        else:
                            grty=input("Please enter either Vertical histogram, Horizontal histogram, Pie chart, Vertial bar graph or Horizontal bar graph -").capitalize()
                            continue
                    break
                elif vis==3:
                    grty=input('''What type of graph do you want:
1. Histogram
2. Pie chart
3. Horizontal bar graph
                               
Enter graph type-''').capitalize()
                    while True:
                        if grty=="Histogram":
                            typ=pro["Detection_Method"] 
                            ty=[]
                            for i in typ:
                                ty.append(i)
    
                            plt.hist(ty, color="mediumvioletred",orientation="horizontal")
                            plt.xlabel("No. of times used",color="forestgreen", fontsize=14)
                            plt.ylabel("Detection Method",color="forestgreen", fontsize=14)
                            plt.title("Usage of Detection Methods of Exoplanets",color="deepskyblue", fontsize=18)
                            plt.show()
                            break
                        
                        elif grty=="Pie chart":
                            typ=pro["Detection_Method"]     
                            countpt=0
                            countgm=0
                            countob=0
                            counttv=0
                            countet=0
                            counta=0
                            counttst=0
                            countdi=0
                            countrv=0
                            for i in typ:
                                if i=="Pulsar Timing":
                                    countpt+=1
                                if i=="Gravitational Microlensing":
                                    countgm+=1
                                if i=="Orbital Brightness Modulation":
                                    countob+=1
                                if i=="Transit Timing Variations":
                                    counttv+=1
                                if i=="Eclipse Timing Variations":
                                    countet+=1
                                if i=="Astrometry":
                                    counta+=1
                                if i=="Transit":
                                    counttst+=1
                                if i=="Direct Imaging":
                                    countdi+=1
                                if i=="Radial Velocity":
                                    countrv+=1
                                    
                            finl=[countgm,counttst,countdi,countrv, countob+counttv+countet+counta+countpt]
                            pla=["Gravitational Microlensing","Transit","Direct Imaging","Radial Velocity","Others"]
                            
                            plt.pie(finl,labels=pla, colors=["c",'y','g','b','orange'],shadow=True,startangle=90, explode=[0.05,0.05,0.05,0.05,0.05])
                            plt.title("Usage of Detection Methods of Exoplanets",color="deepskyblue", fontsize=18)
                            plt.show()
                            break
                            
                        elif grty=="Horizontal bar garph":
                            typ=pro["Detection_Method"]     
                            countpt=0
                            countgm=0
                            countob=0
                            counttv=0
                            countet=0
                            counta=0
                            counttst=0
                            countdi=0
                            countrv=0
                            for i in typ:
                                if i=="Pulsar Timing":
                                    countpt+=1
                                if i=="Gravitational Microlensing":
                                    countgm+=1
                                if i=="Orbital Brightness Modulation":
                                    countob+=1
                                if i=="Transit Timing Variations":
                                    counttv+=1
                                if i=="Eclipse Timing Variations":
                                    countet+=1
                                if i=="Astrometry":
                                    counta+=1
                                if i=="Transit":
                                    counttst+=1
                                if i=="Direct Imaging":
                                    countdi+=1
                                if i=="Radial Velocity":
                                    countrv+=1
                                    
                            finl=[countpt,countgm,countob,counttv,countet,counta,counttst,countdi,countrv]
                            print(finl)
                            pla=["Pulsar timing","Gravitational Microlensing","Orbital Brightness Modulation",
                                 "Transit Timing Variations","Eclipse Timing Variations","Astrometry","Transit",
                                 "Direct Imaging","Radial Velocity"]
                            plt.barh(pla,finl, color="mediumvioletred")
                            plt.xlabel("No. of times used",color="forestgreen", fontsize=14)
                            plt.ylabel("Detection Method",color="forestgreen", fontsize=14)
                            plt.title("Usage of Detection Methods of Exoplanets",color="deepskyblue", fontsize=18)
                            plt.show()
                            break
                    
                        else:
                            grty=input("Please enter either Histogram, Pie chart or Horizontal bar graph-").capitalize()
                            continue
                        
                    break
                
                elif vis==4:
                    typ=pro["radiusForCal"] 
                    typs=typ.sort_values()
                    ty=[]
                    for i in typs:
                        ty.append(i)
                        
    
                    typ2=pro["massForCal"] 
                    typ2s=typ2.sort_values()
                    ty2=[]
                    for i in typ2s:
                        ty2.append(i)
    
                    plt.plot(ty,ty2, color="mediumblue")
                    plt.xlabel("Radius of Exoplanets",color="darkgoldenrod",fontsize=14)
                    plt.ylabel("Mass of Exoplanets",color="darkgoldenrod",fontsize=14)
                    plt.title("Radius V/S Mass of Exoplanets",color="firebrick",fontsize=18)
                    plt.show()
                    break
            
                elif vis==5:
                    typ=pro["distanceForCal"] 
                    typs=typ.sort_values()
                    ty=[]
                    for i in typs:
                        ty.append(i)
                        
    
                    typ2=pro["radiusForCal"] 
                    typ2s=typ2.sort_values()
                    ty2=[]
                    for i in typ2s:
                        ty2.append(i)
    
                    plt.plot(ty,ty2, color="mediumblue")
                    plt.xlabel("Distance of Exoplanets",color="darkgoldenrod",fontsize=14)
                    plt.ylabel("Radius of Exoplanets",color="darkgoldenrod",fontsize=14)
                    plt.title("Distance V/S Radius of Exoplanets",color="firebrick",fontsize=18)
                    plt.show()
                    break
                
                elif vis==6:
                    typ=pro["massForCal"] 
                    typs=typ.sort_values()
                    ty=[]
                    for i in typs:
                        ty.append(i)
                        
    
                    typ2=pro["distanceForCal"] 
                    typ2s=typ2.sort_values()
                    ty2=[]
                    for i in typ2s:
                        ty2.append(i)
    
                    plt.plot(ty,ty2, color="mediumblue")
                    plt.xlabel("Mass of Exoplanets",color="darkgoldenrod",fontsize=14)
                    plt.ylabel("Distance of Exoplanets",color="darkgoldenrod",fontsize=14)
                    plt.title("Mass V/S Distance of Exoplanets",color="firebrick",fontsize=18)
                    plt.show()
                    break
                
                elif vis==7:
                    typ=pro["orForCal"] 
                    typs=typ.sort_values()
                    ty=[]
                    for i in typs:
                        ty.append(i)
                        
    
                    typ2=pro["opForCal"] 
                    typ2s=typ2.sort_values()
                    ty2=[]
                    for i in typ2s:
                        ty2.append(i)
    
                    plt.plot(ty,ty2, color="mediumblue")
                    plt.xlabel("Orbital Radius of Exoplanets",color="darkgoldenrod",fontsize=14)
                    plt.ylabel("Oribital Period of Exoplanets",color="darkgoldenrod",fontsize=14)
                    plt.title("Orbital Radius V/S Orbital Period of Exoplanets",color="firebrick",fontsize=18)
                    plt.show()
                    break
                else:
                    vis=int(input("Please enter a valid choice number-"))
                    continue
                                        
            break
        
        elif d!=1 and d!=2 and d!=3 and d!=4:
            d=int(input("Please enter either 1,2,3 or 4-"))
            continue
        break
        
    continue
     
     
    
#THE END
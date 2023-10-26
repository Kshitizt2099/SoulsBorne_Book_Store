from django.shortcuts import render,HttpResponse,redirect

from django.http import HttpResponseRedirect

from soulsbornestore.models import customusers,Adminusers,productslist,newlist,CartCheckoutmk85,sales1,reviewmk1

import re

from django.core.files.storage import FileSystemStorage

# Create your views here.

loggedname=""

cartdata=[]

user_id=""

inSearch=False

byauth=False

auth=""

Searchbyname=False

sname=""

l=[]

p=[]

Searchbyprice=False

inMoreInfo=False

info={}

booklist=[]

infilter=False

authlist=[]

def home(request):

    global loggedname

    global  byauth

    global Searchbyname

    global auth

    global sname

    global l,p

    global inSearch

    global Searchbyprice

    global info

    global inMoreInfo

    global booklist

    global infilter

    global user_id

    global authlist

    authlist=[]

    user_id=""

    inMoreInfo=False

    info={}

    loggedname=""

    l=[]

    p=[]

    byauth=False

    inSearch=False

    auth=""

    Searchbyname=False

    Searchbyprice=False

    booklist=[]

    infilter=False

    return render(request,"Home.html")

##Login View.

def Login(request):

    return render(request,"Login.html")

#Admin View.

def Adminuser(request):

    return render(request,"Adminuser.html")

#Admin Credential checker.

def Adminendpoint(request):

    global loggedname

    found=False

    if(request.method=="POST") :

       

        id1=request.POST.get('id')

        name=request.POST.get('name')

        password=request.POST.get('Password')

        email=request.POST.get('email')

        users=Adminusers.objects.all()

        for i in users:

            print(id1,name,password)

            if(i.id==id1 and name==i.username and password==i.password and i.Emailid==email):

                found=True

                loggedname=name

                break

 

        if(found==True):

            return render(request,"Adminendpoint.html",{"name":name})

    if(len(loggedname)!=0):

        return render(request,"Adminendpoint.html",{"name":loggedname})

 

    return render(request,"Error.html",{"name":"No user Found","path":"Adminuser"})

def search(request):

    if(request.method=="POST"):

        l=[]

        name=request.POST.get("query")

        allproducts=productslist.objects.all()

        for i in allproducts:

            data=re.findall(name,i.name)

            if(len(data)!=0):

                name=i.name

                price=i.price

                author=i.author

                image=i.image

                curr={"name":name,"price":price,"author":author,"image":image}

                l.append(curr)

 

        if(len(l)!=0):

            return render(request,"search.html",{"data":l})

        else:

            return HttpResponse("Nothing found")

#Adding book inside databse.

def adddata(request):

    if(request.method=="POST" and request.FILES['image']):

        name=request.POST.get("name")

        id=request.POST.get("id")

        author=request.POST.get("author")

        price=request.POST.get("price")

        image = request.FILES['image']

        fs = FileSystemStorage()

        filename = fs.save(image.name, image)

        uploaded_file_url = fs.url(filename)

        print(uploaded_file_url)

        desc=request.POST.get("desc")

        Genre=request.POST.get("Genre")

        Year=request.POST.get("Year")

        allproducts=productslist.objects.all()

        for i in allproducts:

            if(i.id==id):

                return render(request,"Error.html",{"name":"Id already registered please enter another id","path":"adddata"})

 

        addingproduct=productslist(name=name,id=id,author=author,price=price,image=uploaded_file_url,desc=desc,Genre=Genre,Year=Year)

        addingproduct.save()

        print("logeed name",loggedname)

        print("image",image)

        path="Adminendpoint"

        return render(request,"Success.html",{"name":"Adding data into the store","path":path})

       

       

    return render(request,"adddata.html")

  

def deldata(request):

    if(request.method=="POST"):

        name=request.POST.get("name")

        id=request.POST.get("id")

        author=request.POST.get("author")

        price=request.POST.get("price")

 

        targetproduct=productslist.objects.get(pk=id)

        

        print("target",targetproduct)

        targetproduct.delete()

        path="Adminendpoint"

        return render(request,"Success.html",{"name":"Deleting data from the store","path":path})

       

       

    return render(request,"deldata.html")

  

def modifydata(request):

   return redirect("Adminendpoint")

 

#user login credential checker and routing center point.   

def userendpoint(request):

     global loggedname

     global user_id

     global auth

     global Searchbyname

     global byauth

     global l

     global p

     found=False

     global inMoreInfo

     global info

     global booklist

     global infilter

     global user_id

     global authlist

     if(inMoreInfo==True):

         return render(request,"MoreInfo.html",{"data":info})

    

         

     if(request.method=="POST") :

       

        id1=request.POST.get('id')

        name=request.POST.get('name')

        password=request.POST.get('Password')

        email=request.POST.get('email')

        users=customusers.objects.all()

        print(users)

        print("name is ", name)

        for i in users:

           

            if(i.id==id1 and name==i.username and password==i.password and i.Emailid==email):

                print(i)

                found=True

                loggedname=name

                user_id=id1

                break

 

        if(found==True or len(loggedname)>0):

            books=productslist.objects.all()

            return render(request,"UserHome.html",{"books":books,"name":loggedname})

        else:

           return render(request,"Error.html",{"name":"No user Found","path":"Login"})

     if(found==True or len(loggedname)>0):

            cart=CartCheckoutmk85.objects.all()

            incart=len(cart)

            if(infilter==True):

                    if(len(booklist)!=0):

                        return render(request,"UserHome.html",{"books":booklist,"name":loggedname,"incart":incart})

                    else:

                        return HttpResponse("Nothing found")

            elif(inSearch==True):

                if(byauth==True):

                  

                    if(len(authlist)!=0):

                        return render(request,"UserHome.html",{"books":authlist,"name":loggedname,"incart":incart})

                    else:

                        return HttpResponse("Nothing found")

                elif(Searchbyname==True):

                    print("In here",Searchbyname)

                    if(len(l)!=0):

                        return render(request,"UserHome.html",{"books":l,"name":loggedname,"incart":incart})

                    else:

                        return HttpResponse("Nothing found")

                elif(Searchbyprice==True):

                    if(len(p)!=0):

                        return render(request,"UserHome.html",{"books":p,"name":loggedname,"incart":incart})

                    else:

                        return HttpResponse("Nothing found")

                elif(infilter==True):

                    if(len(booklist)!=0):

                        return render(request,"UserHome.html",{"books":booklist,"name":loggedname,"incart":incart})

                    else:

                        return HttpResponse("Nothing found")

 

 

 

 

         

            cart=CartCheckoutmk85.objects.all()

            incart=len(cart)

            books=productslist.objects.all()

            return render(request,"UserHome.html",{"books":books,"name":loggedname,"incart":incart})

     else:

         return HttpResponse("No customer with this name")

  

#Payment checkout view.        

def finalcheck(request):

    global loggedname

    if(request.method=="POST"):

        name=request.POST.get("name")

        dc=request.POST.get("dc")

        cvv=request.POST.get("cvv")

        bill=request.POST.get("bill")

        for i in cvv:

                if(i.isalpha()==True):

                    return render(request,"Error.html",{"name":"No Alphabets allowed in cvv no","path":"cart"})

        

        for i in dc:

                if(i.isalpha()==True):

                    return render(request,"Error.html",{"name":"No Alphabets allowed in card no","path":"cart"})

        if(name!=loggedname):

             return render(request,"Error.html",{"name":"Wrong User name","path":"cart"})

        if(len(cvv)!=3):

            

            return render(request,"Error.html",{"name":"Wrong cvv no","path":"cart"})

        if(len(dc)!=12 ):

            

            return render(request,"Error.html",{"name":"Wrong Card no","path":"cart"})

        products=""

        cartpro=CartCheckoutmk85.objects.all()

        for i in cartpro:

            products+=i.name+","

        total=0

        for i in cartpro:

            total+=(i.qty)*int(i.price)

        salestore=sales1(username=loggedname,products=products,total=total,userid=user_id)

        salestore.save()

        CartCheckoutmk85.objects.all().delete()

        return render(request,"checkout.html",{"bill":bill})

 

#Price calculator of elements in cart.    

def checkout(request):

    global inSearch

    cartpro=CartCheckoutmk85.objects.all()

    total=0

    for i in cartpro:

        total+=(i.qty)*int(i.price)

   

    inSearch=False

 

    return render(request,"Payment.html",{"bill":total})

 

#updating cart

def updateCart(request):

   

    if(request.method=="POST"):

        op=request.POST.get("op")

        name=request.POST.get("name")

        id=request.POST.get("id")   

        entry=CartCheckoutmk85.objects.filter(p_id=id)

        if(op=="inc"):

            newqty=entry[0].qty+1

            entry.update(qty=newqty)

        else:

            if(entry[0].qty>1):

                newqty=entry[0].qty-1

                entry.update(qty=newqty)

 

 

        print(entry,entry[0].qty)

        #return HttpResponse(op+" is pressed "+name+" is name"+"p_id is"+id + " qty is "+str(entry[0].qty))

        cartpro=CartCheckoutmk85.objects.all()

        total=0      

        for i in cartpro:

            total+=(i.qty)*int(i.price)

        return render(request,"Cart.html",{"data":cartpro,"name":"tony","total":total})

    return HttpResponse("FIGURE IT OUT")

    

 

    

def cart(request):

    global loggedname

    if(request.method=="POST"):

        name=request.POST.get("name")

        price=request.POST.get("price")

        p_id=request.POST.get("id")

        print(name)

        userid=user_id

        username=loggedname

        cartpro=CartCheckoutmk85.objects.all()

        toadd=True

        for i in cartpro:

            if(p_id==i.p_id):

                toadd=False

 

        if(toadd==True):

            inCart=CartCheckoutmk85(p_id=p_id,user_id=userid,username=username,name=name,price=price,qty=1)

            inCart.save()  

            print("added")

  

 

 

        return redirect("userendpoint")

    

    cartpro=CartCheckoutmk85.objects.all()

    total=0      

    for i in cartpro:

        total+=(i.qty)*int(i.price)

    return render(request,"Cart.html",{"data":cartpro,"name":loggedname,"total":total})

#deleting the elemnt quantity from cart.       

def DeleteCart(request):

    if(request.method=="POST"):

        id=request.POST.get("id")

        target=CartCheckoutmk85.objects.get(p_id=id)

        target.delete()

        print("target",target)

      

 

    cartpro=CartCheckoutmk85.objects.all()

    total=0       

     

    for i in cartpro:

        total+=(i.qty)*int(i.price)

    return render(request,"Cart.html",{"data":cartpro,"name":loggedname,"total":total})

#creating userid.

def Create(request):

    if(request.method=="POST"):

        name=request.POST.get("name")

        id=request.POST.get("id")

        password=request.POST.get("password")

        email=request.POST.get("email")

        allusers=customusers.objects.all()

        for i in allusers:

            if(i.id==id):

                return render(request,"Error.html",{"name":"id Already Registered please choose another id","path":"/Login"})

        adduser=customusers(username=name,id=id,password=password,Emailid=email)

        adduser.save()

        return render(request,"Success.html",{"name":"Account Creation","path":"/"})

    return render(request,"Createaccount.html")

#Back View

def UserBack(request):

            global auth

            global Searchbyname

            global byauth

            global loggedname

            global l

            global inMoreInfo

            global authlist

            global infilter

            global booklist

            global Searchbyprice

            global p

            if(byauth):

                inMoreInfo=False

                return render(request,"UserHome.html",{"books":authlist,"name":loggedname})

            if(Searchbyname):

                inMoreInfo=False

                return render(request,"UserHome.html",{"books":l,"name":loggedname})

            if(infilter):

                inMoreInfo=False

                return render(request,"UserHome.html",{"books":booklist,"name":loggedname})

            if(Searchbyprice):

                inMoreInfo=False

                return render(request,"UserHome.html",{"books":p,"name":loggedname})

 

 

 

            inMoreInfo=False

            books=productslist.objects.all()

            return render(request,"UserHome.html",{"books":books,"name":loggedname})

#Search the book by author name

def AuthorSearch(request):

    global loggedname

    global inSearch

    global auth

    global byauth

    global authlist

    global Searchbyname

    global Searchbyprice

    global infilter

    authlist=[]

    if(request.method=="POST"):

        auth=request.POST.get("author")

        inSearch=True

        byauth=True

        Searchbyname=False

        Searchbyprice=False

        infilter=False

        books=productslist.objects.all()

        for i in books:

            data=re.findall(auth,i.author)

            

            if(len(data)!=0):

                id=i.id

                name=i.name

                price=i.price

                author=i.author

                image=i.image

                Genre=i.Genre

                desc=i.desc

                Year=i.Year

                curr={"name":name,"price":price,"author":author,"image":image,"id":id,"Genre":Genre,"desc":desc,"Year":Year}

                dupli=False

 

                authlist.append(curr)

        if(len(authlist)!=0):

            return render(request,"UserHome.html",{"books":authlist,"name":loggedname})

        else:

            return HttpResponse("Nothing found")

    return render(request,"AuthorSearch.html")

#earch the book by book name

def NameSearch(request):

    global loggedname

    global inSearch

    global auth

    global byauth

    global Searchbyname

    global sname

    global l

    global infilter

    global Searchbyprice

    

    l=[]

    if(request.method=="POST"):

        Searchbyname=True

        inSearch=True

        Searchbyprice=False

        byauth=False

        infilter=False

        book=request.POST.get("query")

        print(book)

        allproducts=productslist.objects.all()

        for i in allproducts:

            data=re.findall(book,i.name)

            print(i.name,book)

            if(len(data)!=0):

                id=i.id

                name=i.name

                price=i.price

                author=i.author

                image=i.image

                Genre=i.Genre

                desc=i.desc

                Year=i.Year

                curr={"name":name,"price":price,"author":author,"image":image,"id":id,"Genre":Genre,"desc":desc,"Year":Year}

                dupli=False

 

                l.append(curr)

        if(len(l)!=0):

            return render(request,"UserHome.html",{"books":l,"name":loggedname})

        else:

            return HttpResponse("Nothing found")

    return render(request,"NameSearch.html")

#By searching price range.

def PriceSearch(request):

    global loggedname

    global inSearch

    global auth

    global byauth

    global Searchbyprice

    global sname

    global p

    global Searchbyname

    global infilter

    if(request.method=="POST"):

        Searchbyprice=True

        inSearch=True

        Searchbyname=False

        byauth=False

        infilter=False

        min=request.POST.get("Min")

        max=request.POST.get("Max")

        if(int(min)>int(max)):

            return render(request,"Error.html",{"name":"Wrong inputs Sir ","path":"PriceSearch"})

        allproducts=productslist.objects.all()

        for i in allproducts:

           

            if(int(min)<=int(i.price)<=int(max)):

                id=i.id

                name=i.name

                price=i.price

                author=i.author

                image=i.image

                Genre=i.Genre

                desc=i.desc

                Year=i.Year

                curr={"name":name,"price":price,"author":author,"image":image,"id":id,"Genre":Genre,"desc":desc,"Year":Year}

                p.append(curr)

               

              

        if(len(p)!=0):

            return render(request,"UserHome.html",{"books":p,"name":loggedname})

        else:

            return render(request,"Error.html",{"name":"Nothing Found in this range ","path":"PriceSearch"})

    return render(request,"PriceSearch.html")

def UserHome(request):

        global inSearch

        global auth

        global Searchbyname

        global byauth

        global p

        global l

        global booklist

        global inMoreInfo

        global authlist

        global Searchbyprice

        global infilter

        inMoreInfo=False

        infilter=False

        if(inSearch==True):

            byauth=False

            Searchbyname=False

            Searchbyprice=False

            l=[]

            p=[]

            booklist=[]

            authlist=[]

            inSearch=False

 

        books=productslist.objects.all()

        return render(request,"UserHome.html",{"books":books,"name":loggedname})

#Details page of book.

def MoreInfo(request):

        global inMoreInfo

        global info

        if(request.method=="POST"):

            inMoreInfo=True

            name=request.POST.get("name")

            id=request.POST.get("id")

            price=request.POST.get("price")

            image=request.POST.get("image")

            author=request.POST.get("author")

            Genre=request.POST.get("Genre")

            desc=request.POST.get("desc")

            Year=request.POST.get("Year")

            curr={"name":name,"price":price,"id":id,"image":image,"author":author,"Genre":Genre,"desc":desc,"Year":Year}

            info=curr

            reviewsall=reviewmk1.objects.all()

            reviews=[]

            total=0

            print("len ",len(reviewsall))

            if(len(reviewsall)==0):

               print("in here")

               return render(request,"MoreInfo.html",{"data":info,"reviews":["No reviews yet"],"rating":"N/A"})

            for i in reviewsall:

                print(i.name)

                if(i.name==name):

                    reviews.append(i)

                    total+=i.score

            if(total==0):

                total="No reviews yet"

            else:

                total=total//len(reviews)

            allusers=customusers.objects.all()

            users=[]

            for i in allusers:

                for j in reviews:

                    if(j.userid==i.id):

                        if(i.username not in users):

                            users.append(i.username)

 

 

 

                

            return render(request,"MoreInfo.html",{"data":info,"reviews":reviews,"rating":total})

#fetching books from database and rendering it

def View(request):

     books=productslist.objects.all()

     return render(request,"View.html",{"books":books})

#Filtering the d=books by genre

def GenreFilter(request):

     books=productslist.objects.all()

     genrelist=[]

     for i in books:

         if(i.Genre not in genrelist):

             genrelist.append(i.Genre)

     return render(request,"Genre.html",{"genrelist":genrelist})

def GenreView(request):

     global booklist

     global infilter

     global inSearch

     m=[]

     if(request.method=="POST"):

         genre=request.POST.get("genre")

         books=productslist.objects.all()

         infilter=True

         inSearch=False

         print(genre)

         for i in books:

             if(i.Genre==genre):

                 m.append(i)

         booklist=m

         return redirect("userendpoint")

 

     

"""def sales(request):

    sales=sales1.objects.all()

    print(sales)

    return render(request,"sales.html",{"sales":sales})"""

#All sales that have been made throughout time.

 

def sales(request):

    sales=sales1.objects.all()

    print(sales)

    return render(request,"sales.html",{"sales":sales})

 

 

#rendering review page

def reviews(request):

    if(request.method=="POST"):

        allreviews=reviewmk1.objects.all()

        pid=request.POST.get('id')

        book_name=request.POST.get('name')

        for i in allreviews:

            if(i.pid==pid and i.name==book_name and i.username==loggedname ):

                return render(request,"Error.html",{"name":"You Already reviewed this product","path":"Review"})

        return render(request,"ReviewForm.html",{"pid":pid,"name":book_name})

        

        

    books=productslist.objects.all()

    return render(request,"Review.html",{"books":books})

         

#rendering review form page.

def reviewsform(request):

    if(request.method=="POST"):

        uid=user_id

        name=request.POST.get("name")

        username=loggedname

        desc=request.POST.get('desc')

        score=request.POST.get('score')  

        if(int(score)>5):

              return render(request,"Error.html",{"name":"Score Bigger Than 5?? Are you serious","path":"Review"})

        pid=request.POST.get("pid")

        reviewadd=reviewmk1(username=username,userid=uid,desc=desc,name=name,pid=pid,score=score)

        reviewadd.save()

        return render(request,"Success.html",{"name":"Review adding","path":"UserHome"})

#forget password managemnt      

def ForgetManage(request):

    if(request.method=="POST"):

      path=request.POST.get('path')

      return render(request,"Forget.html",{"path":path})

              

def Forget(request):

    if(request.method=="POST"):

        uid=request.POST.get("id")

        email=request.POST.get("email")

        password=request.POST.get('password')

        path=request.POST.get("path")

        allcustomers=customusers.objects.all()

        alladmins=Adminusers.objects.all()

        list=[]

        searching=""

        if(path=="Login"):

            list=allcustomers

            searching=customusers

        elif(path=="Adminuser"):

            list=alladmins

            searching=Adminusers

        for i in list:

           

            if(i.id==uid and i.Emailid==email):

                userdata=searching.objects.get(id=uid)

                userdata.password=password

                userdata.save()

                return render(request,"Success.html",{"name":"Password reset","path":path})

        return render(request,"Error.html",{"name":"No user Found","path":"/"})

 

#View all orders of particular customer

def MyOrders(request):

    global user_id

    Orders=sales1.objects.filter(userid=user_id)

    print("Orders",Orders)

    return render(request,"MyOrders.html",{"sales":Orders})
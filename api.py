# from colorama import Cursor
from distutils.util import execute
from colorama import Cursor
from flask import *
import mysql.connector
from datetime import datetime, timedelta

app=Flask(__name__)

app.secret_key='user' 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shukurmern@786",
  database="project2"
)


mycursor = mydb.cursor(buffered=True)



@app.route('/index',methods=['POST','GET'])
def home0():
    session['fromlogin']=''
    session['fromtheator']=''
    session['city']=''
    session['ssid']=''
    session['cname']=''
    return render_template('index.html')



@app.route('/reg',methods=['POST','GET'])
def home2():
    return render_template('reg.html')


@app.route('/regf',methods=['POST','GET'])
def home4():
    r=dict(request.form)
    print(r)
    global mydb
    global mycursor
    if r['p']!=r['rp']:
        return render_template('reg.html',u="Password Not Matches")
    mycursor.execute("select c_name from customers")
    l=list(mycursor)
    l=[i[0] for i in l]
    if r['u'] in l:
        return render_template('reg.html',u="User Exists Try with new username")
    if len(r['m'])!=10:
        return render_template('reg.html',u="Please check mobile number")
    e=r['e'][::-1]
    if e[0:10]!='moc.liamg@':
        return render_template('reg.html',u="Check Your Mail")
    if len(r)!=7:
        return render_template('reg.html',u="Please Select gender")
    s="insert into customers(c_name,c_email,c_mobile,c_password,c_gender)  values(%s,%s,%s,%s,%s) "
    l=[r['u'],r['e'],r['m'],r['p'],r['g']]
    mycursor.execute(s,l)
    mydb.commit()
    return render_template('login.html',u="User Successfully Registered You Can login Now")


@app.route('/login',methods=['POST','GET'])
def home3():
    return render_template('login.html')


@app.route('/loginf',methods=['POST','GET'])
def home5():
    r=dict(request.form)
    print(r)
    if len(r)<2:
        return render_template('login.html',u="Please Enter All Fields")
    s="select * from customers where c_name=%s and c_password=%s"
    l=[r['u'],r['p']]
    mycursor.execute(s,l)
    l1=list(mycursor)
    if len(l1)<1:
        return render_template('login.html',u="Invalid Login")
    session['city']=""
    mycursor.execute("select c_id,c_name from customers where c_name=%s",[r['u']])
    session['username']=list(mycursor)[0][0]
    session['fromtheator']=''
    session['fromlogin']='true'
    session['cname']=r['u']
    return redirect(url_for('movies'))
    

@app.route('/alogin',methods=['POST','GET'])
def adlogin():
    return render_template('alogin.html')


@app.route('/aloginf',methods=['POST','GET'])
def adloginf():
        r=dict(request.form)
        if r['u']=='Irfan' and r['p']=='@123':
            session['msg']=""
            return render_template('admin.html',u="")
        else:
            
                global mycursor
                s="select * from t_owner where o_name=%s and o_pass=%s"
                print(r)
                mycursor.execute(s,[r['u'],r['p']])
                l=list(mycursor)
                if len(l)==0:
                    return render_template('alogin.html',u="Invalid login")

                mycursor.execute("select o_id from t_owner where o_name=%s",[r['u']])
                p=list(mycursor)[0][0]
                mycursor.execute("select t_id from theater where o_id=%s",[p])
    
                session['tid']=list(mycursor)[0][0]
                print(session['tid'])
                session['admin']=r['u']
                session['show']=""
                session['mmsg']=""
                return render_template('toadmin.html',u=r['u'])



@app.route('/addtheater',methods=['POST','GET'])
def addtheater():
    s="select * from city "
    global mydb
    global mycursor
    mycursor.execute(s)
    l=list(mycursor)
    print(l)
    s="select o_name from t_owner"
    mycursor.execute(s)
    l1=list(mycursor) 
    print(l1) 
    if len(session['msg'])>2:
             msg="Successfully Added"
    else:
        msg=""
    return render_template('addtheater.html',u=l,u1=l1,msg=msg)

@app.route('/temp/<m_id>',methods=['POST','GET'])
def temp(m_id):
    print(m_id)
    r=dict(request.form)
    print(r)
    return ""

@app.route('/addtheaterf',methods=['POST','GET'])
def addtheaterf():
    r=request.form
    print(r)
    s=f"select city_id from city where pincode={r['p']}"
    global mydb
    global mycursor
    mycursor.execute(s)
    p1=list(mycursor)[0][0]
    print(p1)
    s="select o_id from t_owner where o_name=%s"
    mycursor.execute(s,[r['o']])
    p2=list(mycursor)[0][0]
    print(p2)
    l=[r['n'],p2,r['y'],p1]
    s="insert into theater(t_name,o_id,e_year,c_id) values(%s,%s,%s,%s)"
    mycursor.execute(s,l)
    mydb.commit()
    mycursor.execute("select t_id from theater order by t_id desc limit 1")
    p3=list(mycursor)[0][0]
    print(p3)
    ts=int(r['ts'])
    for i in range(1,ts+1):
        s=f"insert into seats(t_id,se_id) values({p3},{i})"
        mycursor.execute(s)
        mydb.commit()
    session['msg']='successfully added'
    return redirect(url_for('addtheater'))


@app.route('/addmovie',methods=['POST','GET'])
def addmovie():   
    return render_template('addmovie.html',u= "")

@app.route('/addmovief',methods=['POST','GET'])
def addmovierf():    
        r=dict(request.form)
        print(r)
        global mydb
        global mycursor
        s="insert into movies(m_name,m_desc,m_genre,m_year,m_length) values(%s,%s,%s,%s,%s)"
        l=[r['m'],r['d'],r['g'],r['y'],r['l']]
        mycursor.execute(s,l)
        mydb.commit()
        return render_template('addmovie.html',u='Successfully Added')
            
@app.route('/toaddmovie',methods=['POST','GET'])
def toaddmovie():   
    return render_template('toaddmovie.html',u= "")

@app.route('/addmovief',methods=['POST','GET'])
def toaddmovierf():    
        r=dict(request.form)
        print(r)
        global mydb
        global mycursor
        s="insert into movies(m_name,m_desc,m_genre,m_year,m_length) values(%s,%s,%s,%s,%s)"
        l=[r['m'],r['d'],r['g'],r['y'],r['l']]
        mycursor.execute(s,l)
        mydb.commit()
        return render_template('toaddmovie.html',u='Successfully Added')
# addcity       
@app.route('/addcity',methods=['POST','GET'])
def addcity(): 
    return render_template('city.html',u= "")
#addcityf to add to database
@app.route('/addcityf',methods=['POST','GET'])
def addcityf(): 
    r=dict(request.form)
    global mydb
    global mycursor

    s="insert into city(c_name,pincode) values(%s,%s)"
    l=[r['c'],r['p']]
    try:
        mycursor.execute(s,l)
        mydb.commit()
        return render_template('city.html',u1='Successfully Added')
    except:
        return render_template('city.html',u='Already Exists')


#redirecting to addowner.html page
@app.route('/addowner',methods=['POST','GET'])
def addowner(): 
   return render_template('addowner.html',u="")

# to add a theater ownerfuntion 
@app.route('/addownerf',methods=['POST','GET'])
def addownerf(): 
    r=dict(request.form)
    print(r)
    l=[r['n'],r['b'],r['e'],r['m'],r['g'],r['id'],r['idnum'],r['p']]
    s="insert into t_owner(o_name,o_dob,email,o_mobile,gender,id_type,id_num,o_pass) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    global mycursor
    global mydb
    try :
        mycursor.execute(s,l)
        mydb.commit()
        return render_template("addowner.html",u="successffuly Added")
    except:
        return render_template("addowner.html",u="check details")

#theaterowneraddshowpage redirecting by taking all movienames,session[mgs] is used when coming from toaddshowf i.e after adding show
@app.route('/toaddshow',methods=['POST','GET'])
def addshow():
    s="select m_name,m_year,m_id from movies"
    global mycursor
    mycursor.execute(s)
    l=list(mycursor)
    if len(session['show'])>10:
        msg=session['show']
        session['show']=""
        return render_template('toaddshow.html',u=msg,u1=l)
    return render_template('toaddshow.html',u1=l)

#add show for theaterowner 
@app.route('/toaddshowf',methods=['POST','GET'])
def addshowf(): 
        r=dict(request.form)
        print(r['d'])
        now = datetime.now()
        print(now)
        pr = now.strftime('%Y-%m-%d')
        pd = datetime.strptime(pr,'%Y-%m-%d')
        sd=datetime.strptime(r['d'], '%Y-%m-%d')
        print(pd,sd,end='\n')
        print(sd >= pd )
        if sd >= pd :
                s_t=datetime.strptime(r['s']+':00', '%H:%M:%S')
                e_t=datetime.strptime(r['e']+':00', '%H:%M:%S')
                global mydb
                global mycursor
                try:
                        mycursor.execute("select s_end from shows where t_id=%s and s_date=%s order by s_end desc limit 1",[session['tid'],r['d']])
                        de=list(mycursor)[0][0]
                        print(de)
                        de=datetime.strptime(str(de), '%H:%M:%S')
                        print(s_t < de)
                        if s_t < de:
                            session['show']="time overlapse with previous show time"
                            return redirect(url_for('addshow'))

                        s="insert into shows(t_id,m_id,s_date,s_start,s_end)  values(%s,%s,%s,%s,%s)"
                        mycursor.execute(s,[session['tid'],r['m'],r['d'],s_t,e_t])
                        session['show']="Successfully Added"
                        return redirect(url_for('addshow'))
                except:
                        
                        s="insert into shows(t_id,m_id,s_date,s_start,s_end)  values(%s,%s,%s,%s,%s)"
                        mycursor.execute(s,[session['tid'],r['m'],r['d'],s_t,e_t])
                        session['show']="Successfully Added"
                        mydb.commit()
                        return redirect(url_for('addshow'))

        session['show']="Date Need to more then or equal to today date"
        return redirect(url_for('addshow'))

        
 #it will show all movies when open movies page       
@app.route('/movies',methods=['POST','GET'])
def movies():
    s="select * from city "
    global mydb
    global mycursor
    mycursor.execute(s)
    l1=list(mycursor)
    s="select distinct m.*  from movies m join shows s on s.m_id=m.m_id"
    mycursor.execute(s)
    l2=list(mycursor)
    if len(session['fromtheator'])>2 and session['fromlogin']=='true':
        msg=session['fromtheator']
        session['fromtheator']=''
        return render_template('movies.html',u="Add city to search",u1=l1,u2=l2,msg=msg,fromlogin=session['fromlogin'],user=session['cname'])

    return render_template('movies.html',u="Add city to search",u1=l1,u2=l2,fromlogin=session['fromlogin'],user=session['cname'])

#searching the movies by the city_id 
@app.route('/citymovie',methods=['POST','GET'])
def citymovies():
    r=dict(request.form)
    session['city']=r['city']
    # s="select *  from movies m join shows s on s.m_id=m.m_id join theater t on  t.t_id=s.t_id join city c on c.city_id=t.c_id where c.pincode=%s;
    s="select distinct m.* from movies m where m.m_id in ( select m_id from shows s where t_id in (select t_id from theater t join city on city.city_id=t.c_id where city.pincode=%s) ) "
    global mycursor
    mycursor.execute(s,[r['city']])
    l2=list(mycursor)
    if len(l2)<1:
        msg="You don't have any shows in your area"
    else:
        msg=""
    s="select * from city"
    mycursor.execute(s)
    l1=list(mycursor)
    return render_template('movies.html',u="Add city to search",u1=l1,u2=l2,msg=msg,fromlogin=session['fromlogin'],user=session['cname'])

# finding all theaters in which particular movie is playing, and finding particular showdate,s_start for that theater and movie for selectoptions 
@app.route('/theater/<m_id>',methods=['POST','GET'])
def theater(m_id):
    if len(session['fromlogin'])<2:
              return redirect(url_for('home3'))
    print(m_id)
    c=session['city']
    global mycursor
    if len(c)>0:
        s="select distinct t.*,c.* from movies m join shows s on s.m_id=m.m_id join theater t on t.t_id=s.t_id join city c on c.city_id=t.c_id where c.pincode=%s and m.m_id=%s and s.s_date > now() and s.s_status=1  "
        # now = datetime.now()
        # pd= now.strftime('%Y-%m-%d %H:%M:%S')
        mycursor.execute(s,[c,m_id])
        l1=list(mycursor)
        print(l1)
        if len(l1)<1:
            msg=f"Your Don't have any theaters in your area with the given movie"
        else:
            msg=""
        s="select * from city"
        mycursor.execute(s)
        l2=list(mycursor)
        timings=[]
        for i in l1:
                s="select s_date,s_start from shows where t_id=%s and m_id=%s "
                mycursor.execute(s,[i[0],m_id])
                n=tuple(mycursor)
                if len(n)<1:
                      n=("","")
                timings.append(n)
        print(timings)
        session['tid']=''
        session['city']=''
        return render_template('theater.html',u2=l1,timings=timings,msg=msg)
    session['fromtheator'] ="Please Select City Before selecting theator"  
    return redirect(url_for('movies')) 
    # s="select distinct t.*,c.* from shows s join theater t on s.t_id=s.t_id join city c on c.city_id=t.c_id where s.m_id=%s and s.s_date > now() ans s.status='1' "
    # mycursor.execute(s,[m_id])
    # l1=list(mycursor)
    # s="select * from city"
    # mycursor.execute(s)
    # l2=list(mycursor)
    # timings=[]
    # for i in l1:
    #     s="select s_date,s_start from shows where t_id=%s and m_id=%s"
    #     mycursor.execute(s,[i[0],m_id])
    #     n=tuple(mycursor)
    #     if len(n)<1:
    #         n=("","")
    #     timings.append(n)
    # print(timings)
    

#before redirecting to selectseats.html we are finding totatl number of seats of that theater and selected seats are making checked
@app.route('/selectseat/<tid>',methods=['POST','GET'])
def selectseat(tid):
        session['city']='' 
        session['ttid']=tid
        try:
            r=str(dict(request.form)['datetime']).split(',')
            print(r)
            global mycursor
        except:
            pass
    # try:
        s="select s_id from shows where s_date=%s and t_id=%s and s_start=%s"
        mycursor.execute(s,[r[0],tid,r[1]])
        sid=list(mycursor)[0][0]
        print(sid)
        session['sid']=sid
        mycursor.execute("select se_id from booking_seats where s_id='%s'",[sid])
        bookedseats=list(mycursor)
        bs=[int(i[0]) for i in bookedseats]

        mycursor.execute("select se_id from seats where t_id=%s",[tid])
        l=list(mycursor)
        print(l)
        str1="<div class='row1'>"
        c=0
        for i in l:
                if int(i[0]) in bs:
                     s=f'<input type="checkbox" name="{i[0]}" value="{i[0]}" checked>'
                else:
                    s=f'<input type="checkbox" name="{i[0]}" value="{i[0]}">'
                str1=str1+s
                c=c+1
                if c==10:
                    c=0
                    str1=str1+"</div><div class='row1'>"
        str1=str1+"</div>"
        return render_template('selectseats.html',seats=str1)
  
#after selecting seats saving data in bookings and booking_seats table ,taking seat numbers from checkbox to here using form
@app.route('/bookings',methods=['POST','GET'])
def boookings(): 
        r=list(dict(request.form).values())
        print("selected seats",r)
        # for success or failure booking  
        global mycursor
        mycursor.execute("select se_id from booking_seats where s_id='%s'",[session['sid']])
        print("showid is ",session['sid'])
        l=list(mycursor)
        l1=[int(i[0]) for i in l]
        print(">>>>>>>>>previous seats ",l1)
        print(">>>>>>>>>now selected seats along with previous",r)
        if len(r)<=len(l) or len(r)==0:
            return "<h1 align='center' style='color:red'>Your Transaction is Cancelled You din't selected any seats </h1> <p align='center'> <a href='/movies' >RedirectToMovies</a> </p>"
        
        mycursor.execute("insert into bookings(s_id,c_id) values(%s,%s)",[session['sid'],session['username']])
        mycursor.execute("select b_id from bookings order by b_id desc limit 1")
        bid=list(mycursor)[0][0]
        print(bid)
        print(session['sid'])
        for i in r:
            if int(i) not in l1:
                print(i)
                mycursor.execute("insert into booking_seats(b_id,s_id,se_id,price) values(%s,%s,%s,%s)",[bid,session['sid'],i,100])
        mydb.commit()
        session['city']=''
        return "<h1 align='center' style='color:green'>successfully Booked</h1> <p align='center'> <a href='/movies' >RedirectToMovies</a> </p>"
  


#before redirecting mybookings.html we are taking data from booking_seats for seatnumbers, show details from shows table by joining the tables
@app.route('/mybookings',methods=['POST','GET'])
def mybookings():
      session['city']='' 
      s='select b.b_id,bs.se_id,s.s_date,s.s_start,t.t_name,s.s_status,m.m_name from bookings b join booking_seats bs on bs.b_id=b.b_id join shows s on s.s_id=bs.s_id join theater t on t.t_id=s.t_id join movies m on m.m_id=s.m_id where b.c_id=%s'
      global mycursor
      mycursor.execute(s,[session['username']])
      l=list(mycursor)
      if len(l)<1:
          return render_template('mybookings.html',u="You didn't Started Your Bookings upto now")
      return render_template('mybookings.html',l=l)


# to redirect to cancelshows.html by taking shows that are active i.e status 1
@app.route('/cancelshows',methods=['POST','GET'])
def cancelshows():
    s="select m.m_id,m.m_name,s.s_date,s.s_start,s.s_end,m.m_length,s.s_id from shows s join movies m on m.m_id=s.m_id where t_id=%s and s.s_status='1' and s.s_date>=now()"
    global mycursor
    mycursor.execute(s,[session['tid']])
    l=list(mycursor)
    return render_template('cancelshows.html',l=l,var1='to')

#when user click the button to cancelshow we are making showstatus to 0 and redirecting to cancelshow fun to view the remaining active shows
@app.route('/cancelshowsf/<sid>',methods=['POST','GET'])
def cancelshowsf(sid):
    print(sid)
    global mycursor
    mycursor.execute("update shows set s_status='0' where s_id=%s",[sid])
    mycursor.execute("update booking_seats set bs_status='0' where s_id=%s",[sid])
    mydb.commit()
    return redirect(url_for('cancelshows'))


#when user clicks on calledshows to know which shows are cancelled we are redirecting to here and finding the status=0 shows
@app.route('/showscancelled',methods=['POST','GET'])
def showscancelled():
    s="select m.m_id,m.m_name,s.s_date,s.s_start,s.s_end,m.m_length,s.s_id from shows s join movies m on m.m_id=s.m_id where t_id=%s and s.s_status=%s and s.s_date>=now()"
    global mycursor
    mycursor.execute(s,[session['tid'],'0'])
    l=list(mycursor)
    return render_template('cancelshows.html',l1=l,var1='to')


#when user click on enable his 0 status show then we are making status=1 by using showid and redirect to showscancelled to know remaining shows that are cancelled
@app.route('/enableshows/<sid>',methods=['POST','GET'])
def enableshows(sid):
    print(sid)
    global mycursor
    mycursor.execute("update shows set s_status='1' where s_id=%s",[sid])
    mycursor.execute("update booking_seats set bs_status='1' where s_id=%s",[sid])
    mydb.commit()
    return redirect(url_for('showscancelled'))

# all theater shows for admin
@app.route('/adminc',methods=['POST','GET'])
def adminc():
    s="select m.m_id,m.m_name,s.s_date,s.s_start,s.s_end,m.m_length,s.s_id,t.t_name from shows s join movies m on m.m_id=s.m_id join theater t on t.t_id=s.t_id where s.s_status='1' and s.s_date>=now()"
    global mycursor
    mycursor.execute(s)
    l=list(mycursor)
    return render_template('cancelshows.html',l2=l,var1='admin')


# making status=0 for booking_seats and shows and redirecting back to acancelshows
@app.route('/admincf/<sid>',methods=['POST','GET'])
def admincf(sid):
    print(sid)
    global mycursor
    mycursor.execute("update shows set s_status='0' where s_id=%s",[sid])
    mycursor.execute("update booking_seats set bs_status='0' where s_id=%s",[sid])
    mydb.commit()
    return redirect(url_for('adminc'))



# all cancelledshows for admin
@app.route('/admine',methods=['POST','GET'])
def admine():
    s="select m.m_id,m.m_name,s.s_date,s.s_start,s.s_end,m.m_length,s.s_id,t.t_name from shows s join movies m on m.m_id=s.m_id join theater t on t.t_id=s.t_id where s.s_status='0' and s.s_date>=now()"
    global mycursor
    mycursor.execute(s)
    l=list(mycursor)
    return render_template('cancelshows.html',l3=l,var1='admin')


# enable the shows and booking_seats by admin
@app.route('/adminef/<sid>',methods=['POST','GET'])
def adminef(sid):
    print(sid)
    global mycursor
    mycursor.execute("update shows set s_status='1' where s_id=%s",[sid])
    mycursor.execute("update booking_seats set bs_status='1' where s_id=%s",[sid])
    return redirect(url_for('admine'))

@app.route('/analysis',methods=['POST','GET'])
def analysis():
        s1="select count(*) from theater"
        s2='select count(*) from shows where s_status=1'
        s3='select count(*)*100 from booking_seats where bs_status=1'
        s4='select count(*) from customers'
        s5='select count(*) from city'
        s6='select count(*) from bookings'
        s7='select count(*) from shows where s_status=1 and s_date = now()'
        global mycursor
        l=[]
        mycursor.execute(s1)
        l.append(list(mycursor)[0][0])
        mycursor.execute(s2)
        l.append(list(mycursor)[0][0])
        mycursor.execute(s3)
        l.append(list(mycursor)[0][0])
        mycursor.execute(s4)
        l.append(list(mycursor)[0][0])
        mycursor.execute(s5)
        l.append(list(mycursor)[0][0])
        mycursor.execute(s6)
        l.append(list(mycursor)[0][0])
        mycursor.execute(s7)
        l.append(list(mycursor)[0][0])
        print(l)
        return render_template('analysis.html',l=l)


@app.route('/toselectseat',methods=['POST','GET'])
def toselectseat():
        global mycursor
        mycursor.execute("select s_id,s_date from shows where t_id=%s",[session['tid']])
        l=[(i[0],i[1]) for i in list(mycursor)]
        return render_template('toselectseats.html',u1=l)
    

@app.route('/toselectseatf',methods=['POST','GET'])
def toselectseatf():
        global mycursor
        
        try:
            r=dict(request.form)
            session['ssid']=r['sid']
        except:
            r['sid']=session['ssid']

        
        mycursor.execute("select s_id,s_date from shows where t_id=%s",[session['tid']])
        l=[(i[0],i[1]) for i in list(mycursor)]
        if len(r)<1:
            return render_template('toselectseats.html',u1=l,msg="please select the show before search")
        print(r)
        mycursor.execute("select se_id from booking_seats where s_id=%s",[r['sid']])
        bookedseats=list(mycursor)
        bs=[int(i[0]) for i in bookedseats]
        print(bs)
        mycursor.execute("select se_id from seats where t_id='%s'",[session['tid']])
        ts=[int(i[0]) for i in list(mycursor)]
        str1="<div class='row1'>"
        c=0
        for i in ts:
                if i in bs:
                     s=f'<input type="checkbox" name="{i}" value="{i}" checked>'
                else:
                    s=f'<input type="checkbox" name="{i}" value="{i}">'
                str1=str1+s
                c=c+1
                if c==10:
                    c=0
                    str1=str1+"</div><div class='row1'>"
        str1=str1+"</div>"
        return render_template('toselectseats.html',seats=str1,u1=l,msg=session['mmsg'])


@app.route('/tobookings',methods=['POST','GET'])
def toboookings(): 
        r=list(dict(request.form).values())
        print("selected seats",r)
        # for success or failure booking  
        global mycursor
        mycursor.execute("select se_id from booking_seats where s_id=%s",[session['ssid']])
        print("showid is ",session['ssid'])
        l=list(mycursor)
        l1=[int(i[0]) for i in l]
        print(">>>>>>>>>previous seats ",l1)
        print(">>>>>>>>>now selected seats along with previous",r)
        if len(r)<=len(l) or len(r)==0:
            session['mmsg']='please select seat atleast one'
            return redirect(url_for('toselectseatf')) 
        
        mycursor.execute("insert into bookings(s_id) values(%s)",[session['ssid']])
        mydb.commit()
        mycursor.execute("select b_id from bookings order by b_id desc limit 1")
        bid=list(mycursor)[0][0]
        print(bid)
        print(session['ssid'])
        for i in r:
            if int(i) not in l1:
                print(i)
                mycursor.execute("insert into booking_seats(b_id,s_id,se_id,price) values(%s,%s,%s,%s)",[bid,session['ssid'],i,100])
        mydb.commit()
        session['mmsg']='successfully created'
        return redirect(url_for('toselectseatf'))



app.run(debug=True)
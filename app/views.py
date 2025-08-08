from django.db import IntegrityError
from django.shortcuts import render, redirect
import app.admin
from app.Exceptions import PDFException
from app.models import *
from datetime import datetime
from random import shuffle


def index(request):
    try:
        videos = list(Video.objects.all())[:3]
        shuffle(videos)
        return render(request, 'app/index.html', {'videos': videos})
    except Exception as ex:
        return render(request, 'app/index.html', {'message': ex})


def login(request):
    try:
        if request.method == 'POST':
            email = str(request.POST.get("email")).strip()
            password = str(request.POST.get("password")).strip()
            role = str(request.POST.get("role")).strip()
            request.session['email'] = email
            if role == 'admin':
                if email == app.admin.email and password == app.admin.password:
                    request.session['alogin'] = True
                    return redirect(eventmaster)
            elif role == 'member':
                member = Member.objects.get(email=email)
                if member.password == password:
                    request.session['mlogin'] = True
                    request.session['mid'] = member.id
                    request.session['mname'] = member.name
                    request.session['memail'] = email
                    request.session['mmobile'] = member.mobile
                    request.session['maddress'] = member.address
                    return redirect(jobs)
            elif role == 'volunteer':
                volunteer = Volunteer.objects.get(email=email)
                if volunteer.password == password:
                    request.session['vlogin'] = True
                    request.session['vid'] = volunteer.id
                    request.session['vname'] = volunteer.name
                    return redirect(addevent)
            elif role == 'employer':
                employer = Employer.objects.get(email=email)
                if employer.password == password:
                    request.session['elogin'] = True
                    request.session['eid'] = employer.id
                    request.session['ename'] = employer.name
                    request.session['company'] = employer.company
                    request.session['eemail'] = email
                    request.session['emobile'] = employer.mobile
                    request.session['eaddress'] = employer.address
                    return redirect(addjob)
            elif role == 'ngo':
                ngo = NGO.objects.get(email=email)
                if ngo.password == password:
                    request.session['nlogin'] = True
                    request.session['nid'] = ngo.id
                    request.session['nname'] = ngo.name
                    request.session['nemail'] = email
                    request.session['nmobile'] = ngo.mobile
                    request.session['naddress'] = ngo.address
                    return redirect(uploadadoptiondata)
            message = 'Invalid username or password'
            return render(request, 'app/login.html', {'message': message})
        else:
            request.session['alogin'] = False
            request.session['mlogin'] = False
            request.session['vlogin'] = False
            request.session['elogin'] = False
            request.session['nlogin'] = False
            return render(request, 'app/login.html')
    except Member.DoesNotExist:
        message = 'Invalid username or password'
    except Volunteer.DoesNotExist:
        message = 'Invalid username or password'
    except Employer.DoesNotExist:
        message = 'Invalid username or password'
    except NGO.DoesNotExist:
        message = 'Invalid username or password'
    except Exception as ex:
        message = ex
    return render(request, 'app/login.html', {'message': message})


def mregistration(request):
    try:
        message = ""
        if request.method == "POST":
            member = Member()
            member.id = datetime.now().strftime('%d%m%y%I%M%S')
            member.name = request.POST.get('name')
            member.age = request.POST.get('age')
            member.education = request.POST.get('education')
            member.skills = request.POST.get('skills')
            member.email = request.POST.get('email')
            member.mobile = str(request.POST.get('mobile')).strip()
            member.address = request.POST.get('address')
            member.password = str(request.POST.get('password')).strip()
            member.save(force_insert=True)
            message = 'Member registration done successfully...'
        return render(request, 'app/mregistration.html', {'message': message})
    except Exception as ex:
        return render(request, 'app/mregistration.html', {'message': ex})


def vregistration(request):
    try:
        message = ""
        if request.method == "POST":
            volunter = Volunteer()
            volunter.id = datetime.now().strftime('%d%m%y%I%M%S')
            volunter.name = request.POST.get('name')
            volunter.age = request.POST.get('age')
            volunter.education = request.POST.get('education')
            volunter.skills = request.POST.get('skills')
            volunter.email = request.POST.get('email')
            volunter.mobile = str(request.POST.get('mobile')).strip()
            volunter.address = request.POST.get('address')
            volunter.password = str(request.POST.get('password')).strip()
            volunter.save(force_insert=True)
            message = 'Volunteer registration done successfully...'
        return render(request, 'app/vregistration.html', {'message': message})
    except Exception as ex:
        return render(request, 'app/vregistration.html', {'message': ex})


def eregistration(request):
    try:
        message = ""
        if request.method == "POST":
            employer = Employer()
            employer.id = datetime.now().strftime('%d%m%y%I%M%S')
            employer.name = request.POST.get('name')
            employer.company = request.POST.get('company')
            employer.email = request.POST.get('email')
            employer.mobile = str(request.POST.get('mobile')).strip()
            employer.address = request.POST.get('address')
            employer.password = str(request.POST.get('password')).strip()
            employer.save(force_insert=True)
            message = 'Employer registration done successfully...'
        return render(request, 'app/eregistration.html', {'message': message})
    except Exception as ex:
        return render(request, 'app/eregistration.html', {'message': ex})


def videos(request):
    try:
        if 'mlogin' in request.session and request.session['mlogin']:
            videos = Video.objects.all()
            events = Event.objects.all()
            return render(request, 'member/videos.html', {'videos': videos, 'events': events})
        else:
            return redirect(login)
    except Exception as ex:
        return render(request, 'member/videos.html', {'message': ex})


def eventmaster(request):
    try:
        if 'alogin' in request.session and request.session['alogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                event = Event.objects.get(id=id_)
                event.delete()
            events = Event.objects.all()
        else:
            return redirect(login)
        return render(request, 'admin/viewevent.html', {'events': events})
    except Exception as ex:
        return render(request, 'admin/viewevent.html', {'message': ex})


def videomaster(request):
    try:
        if 'alogin' in request.session and request.session['alogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                video = Video.objects.get(id=id_)
                video.delete()
            videos = Video.objects.all()
        else:
            return redirect(login)
        return render(request, 'admin/viewvideo.html', {'videos': videos})
    except Exception as ex:
        return render(request, 'admin/viewvideo.html', {'message': ex})


def member(request):
    try:
        if 'alogin' in request.session and request.session['alogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                member_ = Member.objects.get(id=id_)
                member_.delete()
            members = Member.objects.all()
        else:
            return redirect(login)
        return render(request, 'admin/member.html', {'members': members})
    except Exception as ex:
        return render(request, 'admin/member.html', {'message': ex})


def volunteer(request):
    try:
        if 'alogin' in request.session and request.session['alogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                volunteer_ = Volunteer.objects.get(id=id_)
                volunteer_.delete()
            volunteers = Volunteer.objects.all()
        else:
            return redirect(login)
        return render(request, 'admin/volunteer.html', {'volunteers': volunteers})
    except Exception as ex:
        return render(request, 'admin/volunteer.html', {'message': ex})


def employer(request):
    try:
        if 'alogin' in request.session and request.session['alogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                employer_ = Employer.objects.get(id=id_)
                employer_.delete()
            employers = Employer.objects.all()
        else:
            return redirect(login)
        return render(request, 'admin/employer.html', {'employers': employers})
    except Exception as ex:
        return render(request, 'admin/employer.html', {'message': ex})


def ngo(request):
    try:
        if 'alogin' in request.session and request.session['alogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                ngo_ = NGO.objects.get(id=id_)
                ngo_.delete()
            ngos = NGO.objects.all()
        else:
            return redirect(login)
        return render(request, 'admin/ngo.html', {'ngos': ngos})
    except Exception as ex:
        return render(request, 'admin/ngo.html', {'message': ex})


def uploadadoptiondata(request):
    try:
        message = ""
        if 'nlogin' in request.session and request.session['nlogin']:
            if request.method == 'POST':
                if request.FILES:
                    id_ = datetime.now().strftime('%d%m%y%I%M%S')
                    pdf = request.FILES['pdf']
                    with open(f'media/adoption/{id_}.pdf', 'wb') as fw:
                        fw.write(pdf.read())
                    adoption = Adoption()
                    adoption.id = id_
                    adoption.description = request.POST.get('description')
                    adoption.nid = request.session["nid"]
                    adoption.nname = request.session["nname"]
                    adoption.nmobile = request.session["nmobile"]
                    adoption.naddress = request.session["naddress"]
                    adoption.save(force_insert=True)
                    message = 'Adoption details uploaded successfully...'
                else:
                    raise Exception('PDF uploading error')
        else:
            return redirect(login)
        return render(request, 'ngo/uploadadoptiondata.html', {'message': message})
    except Exception as ex:
        return render(request, 'ngo/uploadadoptiondata.html', {'message': ex})


def viewadoptiondata(request):
    try:
        if 'nlogin' in request.session and request.session['nlogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                adoption = Adoption.objects.get(id=id_)
                adoption.delete()
            adoptions = Adoption.objects.filter(nid=request.session["nid"])
        else:
            return redirect(login)
        return render(request, 'ngo/viewadoptiondata.html', {'adoptions': adoptions})
    except Exception as ex:
        return render(request, 'ngo/viewadoptiondata.html', {'message': ex})


def viewadoptionrequest(request):
    try:
        if 'nlogin' in request.session and request.session['nlogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                arequest = ARequest.objects.get(id=id_)
                arequest.status = request.POST.get('status')
                arequest.save(force_update=True)
            requests = ARequest.objects.filter(nid=request.session["nid"])
        else:
            return redirect(login)
        return render(request, 'ngo/viewadoptionrequest.html', {'requests': requests})
    except Exception as ex:
        return render(request, 'ngo/viewadoptionrequest.html', {'message': ex})


def addjob(request):
    try:
        message = ""
        if 'elogin' in request.session and request.session['elogin']:
            if request.method == "POST":
                job = Job()
                job.id = datetime.now().strftime('%d%m%y%I%M%S')
                job.date = datetime.now().strftime('%d %b %Y')
                job.title = request.POST.get('title')
                job.description = request.POST.get('description')
                job.salary = request.POST.get('salary')
                job.eid = request.session["eid"]
                job.company = request.session["company"]
                job.email = request.session["eemail"]
                job.mobile = request.session["emobile"]
                job.address = request.session["eaddress"]
                job.save(force_insert=True)
                message = 'Job details added successfully...'
        else:
            return redirect(login)
        return render(request, 'employer/addjob.html', {'message': message})
    except Exception as ex:
        return render(request, 'employer/addjob.html', {'message': ex})


def viewjob(request):
    try:
        if 'elogin' in request.session and request.session['elogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                job = Job.objects.get(id=id_)
                job.delete()
            jobs_ = Job.objects.filter(eid=request.session["eid"])
        else:
            return redirect(login)
        return render(request, 'employer/viewjob.html', {'jobs': jobs_})
    except Exception as ex:
        return render(request, 'employer/viewjob.html', {'message': ex})


def downloadresume(request):
    try:
        if 'elogin' in request.session and request.session['elogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                jrequest = JRequest.objects.get(id=id_)
                jrequest.status = request.POST.get('status')
                jrequest.save(force_update=True)
            requests = JRequest.objects.filter(eid=request.session["eid"])
        else:
            return redirect(login)
        return render(request, 'employer/downloadresume.html', {'requests': requests})
    except Exception as ex:
        return render(request, 'employer/downloadresume.html', {'message': ex})


def addevent(request):
    try:
        message = ""
        if 'vlogin' in request.session and request.session['vlogin']:
            if request.method == "POST":
                event = Event()
                event.id = datetime.now().strftime('%d%m%y%I%M%S')
                event.vid = request.session['vid']
                event.name = request.POST.get('name')
                event.details = request.POST.get('details')
                event.save(force_insert=True)
                message = 'Event details added successfully...'
        else:
            return redirect(login)
        return render(request, 'volunteer/addevent.html', {'message': message})
    except Exception as ex:
        return render(request, 'volunteer/addevent.html', {'message': ex})


def viewevent(request):
    try:
        if 'vlogin' in request.session and request.session['vlogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                event = Event.objects.get(id=id_)
                event.delete()
            events = Event.objects.filter(vid=request.session['vid'])
        else:
            return redirect(login)
        return render(request, 'volunteer/viewevent.html', {'events': events})
    except Exception as ex:
        return render(request, 'volunteer/viewevent.html', {'message': ex})


def addvideo(request):
    try:
        message = ""
        if 'vlogin' in request.session and request.session['vlogin']:
            if request.method == "POST":
                video = Video()
                video.name = request.POST.get('name')
                video.id = request.POST.get('id')
                video.vid = request.session['vid']
                video.save(force_insert=True)
                message = 'Video added successfully...'
        else:
            return redirect(login)
        return render(request, 'volunteer/addvideo.html', {'message': message})
    except Exception as ex:
        return render(request, 'volunteer/addvideo.html', {'message': ex})


def viewvideo(request):
    try:
        if 'vlogin' in request.session and request.session['vlogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                video = Video.objects.get(id=id_)
                video.delete()
            videos = Video.objects.filter(vid=request.session['vid'])
        else:
            return redirect(login)
        return render(request, 'volunteer/viewvideo.html', {'videos': videos})
    except Exception as ex:
        return render(request, 'volunteer/viewvideo.html', {'message': ex})


def jobs(request):
    try:
        message = ""
        if 'mlogin' in request.session and request.session['mlogin']:
            if request.method == 'POST':
                if request.FILES:
                    id_ = datetime.now().strftime('%d%m%y%I%M%S')
                    pdf = request.FILES['pdf']
                    with open(f'media/resume/{id_}.pdf', 'wb') as fw:
                        fw.write(pdf.read())
                    job = Job.objects.get(id=request.POST.get("id"))
                    jrequest = JRequest()
                    jrequest.id = id_
                    jrequest.date = datetime.now().strftime('%d %b %Y')
                    jrequest.jid = job.id
                    jrequest.title = job.title
                    jrequest.description = job.description
                    jrequest.salary = job.salary
                    jrequest.mid = request.session['mid']
                    jrequest.mname = request.session['mname']
                    jrequest.mmobile = request.session['mmobile']
                    jrequest.maddress = request.session['maddress']
                    jrequest.eid = job.eid
                    jrequest.company = job.company
                    jrequest.eemail = job.email
                    jrequest.emobile = job.mobile
                    jrequest.eaddress = job.address
                    jrequest.status = "Pending"
                    jrequest.save(force_insert=True)
                    message = "Job application sent successfully.."
                else:
                    raise PDFException('PDF uploading error')
            jobs_ = Job.objects.all()
        else:
            return redirect(login)
        return render(request, 'member/jobs.html', {'jobs': jobs_, 'message': message})
    except IntegrityError:
        message = "Job application already sent.."
        jobs_ = Job.objects.all()
        return render(request, 'member/jobs.html', {'jobs': jobs_, 'message': message})
    except PDFException as ex:
        jobs_ = Job.objects.all()
        return render(request, 'member/jobs.html', {'jobs': jobs_, 'message': ex})
    except Exception as ex:
        return render(request, 'member/jobs.html', {'message': ex})


def jstatus(request):
    try:
        if 'mlogin' in request.session and request.session['mlogin']:
            requests = JRequest.objects.filter(mid=request.session["mid"])
        else:
            return redirect(login)
        return render(request, 'member/jstatus.html', {'requests': requests})
    except Exception as ex:
        return render(request, 'member/jstatus.html', {'message': ex})


def adoptions(request):
    try:
        message = ""
        if 'mlogin' in request.session and request.session['mlogin']:
            if request.method == 'POST':
                id_ = str(request.POST.get('id')).strip()
                adoption = Adoption.objects.get(id=id_)
                arequest = ARequest()
                arequest.id = datetime.now().strftime('%d%m%y%I%M%S')
                arequest.date = datetime.now().strftime('%d %b %Y')
                arequest.aid = adoption.id
                arequest.description = adoption.description
                arequest.mid = request.session['mid']
                arequest.name = request.session['mname']
                arequest.mobile = request.session['mmobile']
                arequest.address = request.session['maddress']
                arequest.status = "Pending"
                arequest.nid = adoption.nid
                arequest.save(force_insert=True)
                message = "Request sent successfully.."
            adoptions_ = Adoption.objects.all()
        else:
            return redirect(login)
        return render(request, 'member/adoptions.html', {'adoptions': adoptions_, 'message': message})
    except IntegrityError:
        message = "Request already sent.."
        adoptions_ = Adoption.objects.all()
        return render(request, 'member/adoptions.html', {'adoptions': adoptions_, 'message': message})
    except Exception as ex:
        return render(request, 'member/adoptions.html', {'message': ex})


def astatus(request):
    try:
        if 'mlogin' in request.session and request.session['mlogin']:
            requests = ARequest.objects.filter(mid=request.session["mid"])
        else:
            return redirect(login)
        return render(request, 'member/astatus.html', {'requests': requests})
    except Exception as ex:
        return render(request, 'member/astatus.html', {'message': ex})


def changepassword(request):
    try:
        message = ''
        if 'mlogin' in request.session and request.session['mlogin']:
            email = request.session['memail']
            user = Member.objects.get(email=email)
            role = "member"
        elif 'vlogin' in request.session and request.session['vlogin']:
            vid = request.session['vid']
            user = Volunteer.objects.get(id=vid)
            role = "volunteer"
        elif 'elogin' in request.session and request.session['elogin']:
            email = request.session['eemail']
            user = Employer.objects.get(email=email)
            role = "employer"
        elif 'nlogin' in request.session and request.session['nlogin']:
            email = request.session['nemail']
            user = NGO.objects.get(email=email)
            role = "ngo"
        else:
            return redirect(login)
        if request.method == 'POST':
            if request.POST.get('submit'):
                oldpassword = str(request.POST.get('oldpassword')).strip()
                newpassword = str(request.POST.get('newpassword')).strip()
                if user.password == oldpassword:
                    user.password = newpassword
                    user.save(force_update=True)
                    message = 'Password changed successfully'
                else:
                    raise Exception('Password not match')
            else:
                if role == 'member':
                    return redirect(jobs)
                elif role == 'volunteer':
                    return redirect(addevent)
                elif role == 'employer':
                    return redirect(addjob)
                elif role == 'ngo':
                    return redirect(uploadadoptiondata)
    except Exception as ex:
        message = ex
    return render(request, 'app/changepassword.html', {'message': message})


def nregistration(request):
    try:
        message = ""
        if request.method == "POST":
            ngo = NGO()
            ngo.id = datetime.now().strftime('%d%m%y%I%M%S')
            ngo.name = request.POST.get('name')
            ngo.email = request.POST.get('email')
            ngo.mobile = str(request.POST.get('mobile')).strip()
            ngo.address = request.POST.get('address')
            ngo.password = str(request.POST.get('password')).strip()
            ngo.save(force_insert=True)
            message = 'NGO registration done successfully...'
        return render(request, 'app/nregistration.html', {'message': message})
    except Exception as ex:
        return render(request, 'app/nregistration.html', {'message': ex})

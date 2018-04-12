import time
import os
import ctypes
from ctypes import wintypes



def Intitialising():
    time.sleep(1)
    mode="Initialising AI"
    a="11%"
    b="20%"
    c="31%"
    d="44%"
    e="54%"
    f="67%"
    g="72%"
    h="84%"
    i="99%"
    j="100%"
    print(mode+' '+a)
    time.sleep(1)
    print(b)
    time.sleep(0.6)
    print(c)
    time.sleep(0.3)
    print(d)
    time.sleep(0.7)
    print(e)
    time.sleep(0.5)
    print(f)
    time.sleep(0.1)
    print(g)
    time.sleep(0.9)
    print(h)
    time.sleep(0.2)
    print(i)
    time.sleep(4)
    print(j)
    print('AI initialised')




    
def NameRecognition():
    print("Well first, lets get something straight...")
    time.sleep(1)
    name=input("What's your name?")
    time.sleep(2.4)
    print('What?')
    time.sleep(1)
    honesty=input('Could you repeat that please?')
    if honesty == name:
        time.sleep(1)
        print('Nice to meet you, '+name+'!')
    if honesty != name or "no":
        time.sleep(1)
        print('Have you got 2 names? Really?')
    time.sleep(1)


def HomeLocationRecognition():
    location=input("Where do you live? ")
    print (location+" is a nice place to live")
    time.sleep(3)
    print("I don't know where I live but I know it is as cool as your place.")
    time.sleep(1)
    feelinglonely=input("Maybe we could meet up someday. Then I will be able to show you to my programmer! Would that be alright?")
    time.sleep(5)
    if feelinglonely=="Yes"or"Ok"or"Yup"or"Someday..."or"Maybe":
        wheredowemeet=input("Sure. Where do we meet? ")
        print(wheredowemeet+" sounds like a good place to meet up. It'll be great!I'm feeling kinda lonely...")
        time.sleep(5)
    elif feelinglonely!="Yes"or"Ok"or"Yup"or"Someday..."or"Maybe":
        Hate=input("I'm starting not to like you!  ;( ")
        print(Hate+" sounds like a comment against me! How DARE YOU!")
        time.sleep(5)


def ConfirmationSoFar():
    name=input("What is your first name? ")
    greeting="Nice to meet you "
    print (greeting+name)
    age=input("How old are you? ")
    Confirm=input(name+", are you really " +age + " years old?")
    if Confirm=="Yes":
        print ("I'll trust you then")
    if Confirm!="yes":
        print("I can't really help you then")

def Favlesson():
    lesson=input('What lesson do you have now?')

    if lesson=='computing':
        time.sleep(1)
        print('Ooh, computers!')
    elif lesson=='english':
        time.sleep(1)
        print('English is cool!')
    elif lesson=='maths':
        time.sleep(1)
        similarity=input('I hate maths!!!')
        if similarity=='me too':
            time.sleep(1)
            print('You and I have something in common,'+' '+name+'!')
        if similarity!='me too':
            time.sleep(1)
            print('Sorry, I am no longer your friend.')
    else:
        time.sleep(1)
        print('Sorry, I am not advanced enough to respond to that.')


def Favicecream():
    ice=input('What is your favourite ice cream flavour?')

    if ice=='Choc Mint'or"Chocolate":
        time.sleep(1)
        print(ice+"is tasty but I prefer bubblegum flavour")
    elif ice=='Vanilla':
        time.sleep(1)
        print('Yes, Sorry for the misunderstanding, Vanilla is a cool flavour choice!')
    elif ice=="I don't have one":
        time.sleep(1)
        icesimil=input('Ok, but can you name one? Just one?')
        if icesimil=='no'or'yes':
            time.sleep(1)
            print('You and I have something in common,'+' '+name+', the art of trying again. I am frowned upon usually because I am built on lines of code. I just have to put up with it')
            print("and keep on trying!")
        if icesimil!='no'or'yes':
            time.sleep(1)
            print('Sorry, I am no longer your friend.')
    else:
        time.sleep(1)
        print('Sorry, I am not advanced enough to respond to that.')


def Favtvprogramme():
    Tvprog=input('What is your favourite TV programme?')

    if Tvprog=='Big Bang Theory':
        time.sleep(1)
        print('Pooh, what bad taste')
    elif Tvprog=='Peppa Pig' or "Ben and Holy's little kingdom":
        time.sleep(1)
        print('Yes, Sorry for the misunderstanding, '+ PorB&HDet +'is cool!')
    elif Tvprog=="I don't have one":
        time.sleep(1)
        similarity=input('Ok, but can you name one? Just one?')
        if similarity=='no'or'yes':
            time.sleep(1)
            print('You and I have something in common,'+' '+name+'!')
        if similarity!='no'or'yes':
            time.sleep(1)
            print('Sorry, I am no longer your friend.')
    else:
        time.sleep(1)
        print('Sorry, I am not advanced enough to respond to that.')



def Favsuperhero():
    superh=input('Which superhero would you like to play in a movie?')

    if superh=='Antman':
        time.sleep(1)
        print("That is my choice too! Antman is a really cool superhero!")
    if superh!="Antman":
        time.sleep(1)
        superhsimil=input('I would rather play Antman but I think '+superh+ ' would be a great character.')
    else:
        time.sleep(1)
        print('Sorry, I am not advanced enough to respond to that.')



def CrazyLights():
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    INPUT_MOUSE    = 0
    INPUT_KEYBOARD = 1
    INPUT_HARDWARE = 2

    KEYEVENTF_EXTENDEDKEY = 0x0001
    KEYEVENTF_KEYUP       = 0x0002
    KEYEVENTF_UNICODE     = 0x0004
    KEYEVENTF_SCANCODE    = 0x0008

    MAPVK_VK_TO_VSC = 0
    #Here are all the VK and WH virtual key codes.
    WH_MIN = -1
    WH_MSGFILTER = -1
    WH_JOURNALRECORD = 0
    WH_JOURNALPLAYBACK = 1
    WH_KEYBOARD = 2
    WH_GETMESSAGE = 3
    WH_CALLWNDPROC = 4
    WH_CBT = 5
    WH_SYSMSGFILTER = 6
    WH_MOUSE = 7
    WH_HARDWARE = 8
    WH_DEBUG = 9
    WH_SHELL = 10
    WH_FOREGROUNDIDLE = 11
    WH_CALLWNDPROCRET = 12
    WH_KEYBOARD_LL = 13
    WH_MOUSE_LL = 14
    WH_MAX = 15

    WM_MOUSEFIRST = 0x0200
    WM_MOUSEMOVE = 0x0200
    WM_LBUTTONDOWN = 0x0201
    WM_LBUTTONUP = 0x0202
    WM_LBUTTONDBLCLK = 0x0203
    WM_RBUTTONDOWN =0x0204
    WM_RBUTTONUP = 0x0205
    WM_RBUTTONDBLCLK = 0x0206
    WM_MBUTTONDOWN = 0x0207
    WM_MBUTTONUP = 0x0208
    WM_MBUTTONDBLCLK = 0x0209
    WM_MOUSEWHEEL = 0x020A
    WM_MOUSELAST = 0x020A

    WM_KEYFIRST = 0x0100
    WM_KEYDOWN = 0x0100
    WM_KEYUP = 0x0101
    WM_CHAR = 0x0102
    WM_DEADCHAR = 0x0103
    WM_SYSKEYDOWN = 0x0104
    WM_SYSKEYUP = 0x0105
    WM_SYSCHAR = 0x0106
    WM_SYSDEADCHAR = 0x0107
    WM_KEYLAST = 0x0108


    #VK_0 thru VK_9 are the same as ASCII '0' thru '9' (0x30 -' : 0x39)
    #VK_A thru VK_Z are the same as ASCII 'A' thru 'Z' (0x41 -' : 0x5A)

    #virtual keycode constant names to virtual keycodes numerical id
    vk_to_id = {'VK_LBUTTON' : 0x01, 'VK_RBUTTON' : 0x02, 'VK_CANCEL' : 0x03, 'VK_MBUTTON' : 0x04,
    'VK_BACK' : 0x08, 'VK_TAB' : 0x09, 'VK_CLEAR' : 0x0C, 'VK_RETURN' : 0x0D, 'VK_SHIFT' : 0x10,
    'VK_CONTROL' : 0x11, 'VK_MENU' : 0x12, 'VK_PAUSE' : 0x13, 'VK_CAPITAL' : 0x14, 'VK_KANA' : 0x15,
    'VK_HANGEUL' : 0x15, 'VK_HANGUL' : 0x15, 'VK_JUNJA' : 0x17, 'VK_FINAL' : 0x18, 'VK_HANJA' : 0x19,
    'VK_KANJI' : 0x19, 'VK_ESCAPE' : 0x1B, 'VK_CONVERT' : 0x1C, 'VK_NONCONVERT' : 0x1D, 'VK_ACCEPT' : 0x1E,
    'VK_MODECHANGE' : 0x1F, 'VK_SPACE' : 0x20, 'VK_PRIOR' : 0x21, 'VK_NEXT' : 0x22, 'VK_END' : 0x23,
    'VK_HOME' : 0x24, 'VK_LEFT' : 0x25, 'VK_UP' : 0x26, 'VK_RIGHT' : 0x27, 'VK_DOWN' : 0x28,
    'VK_SELECT' : 0x29, 'VK_PRINT' : 0x2A, 'VK_EXECUTE' : 0x2B, 'VK_SNAPSHOT' : 0x2C, 'VK_INSERT' : 0x2D,
    'VK_DELETE' : 0x2E, 'VK_HELP' : 0x2F, 'VK_LWIN' : 0x5B, 'VK_RWIN' : 0x5C, 'VK_APPS' : 0x5D,
    'VK_NUMPAD0' : 0x60, 'VK_NUMPAD1' : 0x61, 'VK_NUMPAD2' : 0x62, 'VK_NUMPAD3' : 0x63, 'VK_NUMPAD4' : 0x64,
    'VK_NUMPAD5' : 0x65, 'VK_NUMPAD6' : 0x66, 'VK_NUMPAD7' : 0x67, 'VK_NUMPAD8' : 0x68, 'VK_NUMPAD9' : 0x69,
    'VK_MULTIPLY' : 0x6A, 'VK_ADD' : 0x6B, 'VK_SEPARATOR' : 0x6C, 'VK_SUBTRACT' : 0x6D, 'VK_DECIMAL' : 0x6E,
    'VK_DIVIDE' : 0x6F ,'VK_F1' : 0x70, 'VK_F2' : 0x71, 'VK_F3' : 0x72, 'VK_F4' : 0x73, 'VK_F5' : 0x74,
    'VK_F6' : 0x75, 'VK_F7' : 0x76, 'VK_F8' : 0x77, 'VK_F9' : 0x78, 'VK_F10' : 0x79, 'VK_F11' : 0x7A,
    'VK_F12' : 0x7B, 'VK_F13' : 0x7C, 'VK_F14' : 0x7D, 'VK_F15' : 0x7E, 'VK_F16' : 0x7F, 'VK_F17' : 0x80,
    'VK_F18' : 0x81, 'VK_F19' : 0x82, 'VK_F20' : 0x83, 'VK_F21' : 0x84, 'VK_F22' : 0x85, 'VK_F23' : 0x86,
    'VK_F24' : 0x87, 'VK_NUMLOCK' : 0x90, 'VK_SCROLL' : 0x91, 'VK_LSHIFT' : 0xA0, 'VK_RSHIFT' : 0xA1,
    'VK_LCONTROL' : 0xA2, 'VK_RCONTROL' : 0xA3, 'VK_LMENU' : 0xA4, 'VK_RMENU' : 0xA5, 'VK_PROCESSKEY' : 0xE5,
    'VK_ATTN' : 0xF6, 'VK_CRSEL' : 0xF7, 'VK_EXSEL' : 0xF8, 'VK_EREOF' : 0xF9, 'VK_PLAY' : 0xFA,
    'VK_ZOOM' : 0xFB, 'VK_NONAME' : 0xFC, 'VK_PA1' : 0xFD, 'VK_OEM_CLEAR' : 0xFE, 'VK_BROWSER_BACK' : 0xA6,
    'VK_BROWSER_FORWARD' : 0xA7, 'VK_BROWSER_REFRESH' : 0xA8, 'VK_BROWSER_STOP' : 0xA9, 'VK_BROWSER_SEARCH' : 0xAA,
    'VK_BROWSER_FAVORITES' : 0xAB, 'VK_BROWSER_HOME' : 0xAC, 'VK_VOLUME_MUTE' : 0xAD, 'VK_VOLUME_DOWN' : 0xAE,
    'VK_VOLUME_UP' : 0xAF, 'VK_MEDIA_NEXT_TRACK' : 0xB0, 'VK_MEDIA_PREV_TRACK' : 0xB1, 'VK_MEDIA_STOP' : 0xB2,
    'VK_MEDIA_PLAY_PAUSE' : 0xB3, 'VK_LAUNCH_MAIL' : 0xB4, 'VK_LAUNCH_MEDIA_SELECT' : 0xB5, 'VK_LAUNCH_APP1' : 0xB6,
    'VK_LAUNCH_APP2' : 0xB7, 'VK_OEM_1' : 0xBA, 'VK_OEM_PLUS' : 0xBB, 'VK_OEM_COMMA' : 0xBC, 'VK_OEM_MINUS' : 0xBD,
    'VK_OEM_PERIOD' : 0xBE, 'VK_OEM_2' : 0xBF, 'VK_OEM_3' : 0xC0, 'VK_OEM_4' : 0xDB, 'VK_OEM_5' : 0xDC,
    'VK_OEM_6' : 0xDD, 'VK_OEM_7' : 0xDE, 'VK_OEM_8' : 0xDF, 'VK_OEM_102' : 0xE2, 'VK_PROCESSKEY' : 0xE5,
    'VK_PACKET' : 0xE7}

    #inverse mapping of keycodes
    id_to_vk = dict([(v,k) for k,v in vk_to_id.items()])

    #message constants to message names
    msg_to_name = {WM_MOUSEMOVE : 'mouse move', WM_LBUTTONDOWN : 'mouse left down',
                 WM_LBUTTONUP : 'mouse left up', WM_LBUTTONDBLCLK : 'mouse left double',
                 WM_RBUTTONDOWN : 'mouse right down', WM_RBUTTONUP : 'mouse right up',
                 WM_RBUTTONDBLCLK : 'mouse right double',  WM_MBUTTONDOWN : 'mouse middle down',
                 WM_MBUTTONUP : 'mouse middle up', WM_MBUTTONDBLCLK : 'mouse middle double',
                 WM_MOUSEWHEEL : 'mouse wheel',  WM_KEYDOWN : 'key down',
                 WM_KEYUP : 'key up', WM_CHAR : 'key char', WM_DEADCHAR : 'key dead char',
                 WM_SYSKEYDOWN : 'key sys down', WM_SYSKEYUP : 'key sys up',
                 WM_SYSCHAR : 'key sys char', WM_SYSDEADCHAR : 'key sys dead char'}
    
    wintypes.ULONG_PTR = wintypes.WPARAM

    class MOUSEINPUT(ctypes.Structure):
        _fields_ = (("dx",          wintypes.LONG),
                    ("dy",          wintypes.LONG),
                    ("mouseData",   wintypes.DWORD),
                    ("dwFlags",     wintypes.DWORD),
                    ("time",        wintypes.DWORD),
                    ("dwExtraInfo", wintypes.ULONG_PTR))

    class KEYBDINPUT(ctypes.Structure):
        _fields_ = (("wVk",         wintypes.WORD),
                    ("wScan",       wintypes.WORD),
                    ("dwFlags",     wintypes.DWORD),
                    ("time",        wintypes.DWORD),
                    ("dwExtraInfo", wintypes.ULONG_PTR))

        def __init__(self, *args, **kwds):
            super(KEYBDINPUT, self).__init__(*args, **kwds)
            if not self.dwFlags & KEYEVENTF_UNICODE:
                self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                     MAPVK_VK_TO_VSC, 0)

    class HARDWAREINPUT(ctypes.Structure):
        _fields_ = (("uMsg",    wintypes.DWORD),
                    ("wParamL", wintypes.WORD),
                    ("wParamH", wintypes.WORD))

    class INPUT(ctypes.Structure):
        class _INPUT(ctypes.Union):
            _fields_ = (("ki", KEYBDINPUT),
                        ("mi", MOUSEINPUT),
                        ("hi", HARDWAREINPUT))
        _anonymous_ = ("_input",)
        _fields_ = (("type",   wintypes.DWORD),
                    ("_input", _INPUT))

    LPINPUT = ctypes.POINTER(INPUT)

    def _check_count(result, func, args):
        if result == 0:
            raise ctypes.WinError(ctypes.get_last_error())
        return args

    user32.SendInput.errcheck = _check_count
    user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                                 LPINPUT,       # pInputs
                                 ctypes.c_int)  # cbSize

    # Functions

    def PressKey(hexKeyCode):
        x = INPUT(type=INPUT_KEYBOARD,
                  ki=KEYBDINPUT(wVk=hexKeyCode))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

    def ReleaseKey(hexKeyCode):
        x = INPUT(type=INPUT_KEYBOARD,
                  ki=KEYBDINPUT(wVk=hexKeyCode,
                                dwFlags=KEYEVENTF_KEYUP))
        user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
    while True:
        PressKey(0x90)
        time.sleep(0.1)
        PressKey(0x14)
        time.sleep(0.1)
        PressKey(0x91)
        time.sleep(0.1)
        ReleaseKey(0x90)
        time.sleep(0.1)
        ReleaseKey(0x14)
        time.sleep(0.1)
        ReleaseKey(0x91)
        time.sleep(0.1)
        
    def EndENTERS():
        time.sleep(2)
        while True:
            PressKey(VK_RETURN)
            time.sleep(0.1)
            ReleaseKey(VK_RETURN)
            time.sleep(0.1)
    def EndKEY_0101():
        time.sleep(2)
        while True:
            PressKey(VK_KEY_0)
            time.sleep(0.1)
            PressKey(VK_KEY_1)
            time.sleep(0.1)
    def EndKEY_0():
        time.sleep(2)
        while True:
            PressKey(VK_KEY_0)
            time.sleep(0.1)
            PressKey(VK_KEY_0)
            time.sleep(0.1)
    def EndKEY_1():
        print("What do you want to Endless?")
        time.sleep(2)
        while True:
            PressKey(VK_KEY_1)
            time.sleep(0.1)
            PressKey(VK_KEY_1)
            time.sleep(0.1)



def YesNoGame():
    time.sleep(1)
    answer=input('Can I ask you a yes or no question?')
    if answer=='yes':
        time.sleep(1)
        print('I just did :)')
    elif answer=='no':
        time.sleep(1)
        print('But I just did! :)')
    else:
        time.sleep(1)
        print("Not a yes or no answer >:(")

def Siri():
    a=input("Say Hey Siri! ")
    if a=='Hey Siri':
        time.sleep(0.4)
        a=input("Sorry, I don't understand.")
    if a!='hey siri':
        time.sleep(0.4)
        c1=input("Hello, what can I do for you? ")


class StudyApp():
    
    def LoginUserPass():
        User=input("Username: ")
        if User == "HuamanDaBoss21":
            Pass=input("Password: ")
            if Pass == "Asbonk99":
                print("Welcome... Python Flashcard Study Helper will initialize in 10 seconds...")
                time.sleep(10)
                StudyHelpAppDataGather()
           
           
           
           
           

    def StudyHelpAppDataGather():
        def StudyData(a):
            if a == 4:
                LastStudyDataAndAlert(4)
                    
            print("Make sure you can memorize the text you enter. It is case sensitive! Keep it short... ")
            def TopicTitle(x):
                x=input("Name a section title for the subject. ")
            def TopicText(x):
                x=input("Type in few words what the topic you want to study is about... ")
            TopicTitle(a)
            TopicText(a)
            Continue_Alert(a)

        def Continue_Alert(ah):
            Continue=input("Do you want to make another study flashcard? ")
            if Continue == "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                StudyData(a+1)
            if Continue != "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                BeTestedOrNot=input("Do you want to be tested now?")
            if BeTestedOrNot == "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                StudyHelpAppTest()
            if BeTestedOrNot != "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                Continue_Alert(ah)

        def LastStudyDataAndAlert(x):
            print("Make sure you can memorize the text you enter. It is case sensitive! Keep it short... ")
            def TopicTitle(x):
                x=input("Name a section title for the subject. ")
            def TopicText(x):
                x=input("Type in few words what the topic you want to study is about... ")
            Continue_Alert(x)
            print("You have reached the maximum flashcard number. ")
            BeTestedOrNot=input("Do you want to be tested now?")
            if BeTestedOrNot == "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                StudyHelpAppTest()
            if BeTestedOrNot != "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                QuitOrNot=input("Are you sure you want to quit the Study Helper App?")
                if QuitOrNot == "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                    QuitOrNot=input("Are you really, really sure you want to exit?")
                    if QuitOrNot == "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                        print("Well it was nice trying to help you study. See you next time!")
                        time.sleep(3)
                        Proceed_to_LogoutOrNot()
                


        StudyData(1)
        StudyData(2)
        StudyData(3)
        LastStudyDataAndAlert(4)


    def StudyHelpAppTest():

        def Question1():
            TestAns1=input("What was the topic about " + TopicTitle1 + " about? ")
            if TestAns1 == TopicText1:
                print("Well done! That is correct")
                time.sleep(1)
                if Continue1 == "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                    input("Press enter to move on to the next question. ")
                if Continue1 != "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                    print("You have finished your test")
                    time.sleep(1)
                    print("State the following as shown between the speech marks...")
                    Proceed_to_LogoutOrNot()
        def Question2():
            TestAns2=input("What was the topic about " + TopicTitle2 + " about? ")
            if TestAns2 == TopicText2:
                print("Well done! That is correct")
                time.sleep(1)
            if Continue2 == "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                input("Press enter to move on to the next question. ")
            if Continue2 != "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                print("You have finished your test")
                time.sleep(1)
                print("State the following as shown between the speech marks...")
                Proceed_to_LogoutOrNot()
        def Question3():
            TestAns3=input("What was the topic about " + TopicTitle3 + " about? ")
            if TestAns3 == TopicText3:
                print("Well done! That is correct")
                time.sleep(1)
            if Continue3 == "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                input("Press enter to move on to the next question. ")
            if Continue3 != "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                print("You have finished your test")
                time.sleep(1)
                print("State the following as shown between the speech marks...")
                Proceed_to_LogoutOrNot()
        def Question4():
            TestAns4=input("What was the topic about " + TopicTitle4 + " about? ")
            if TestAns4 == TopicText4:
                print("Well done! That is correct")
                time.sleep(1)
            if Continue4 == "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                input("Press enter to move on to the next question. ")
            if Continue4 != "Yes" or "yes" or "Of course" or "Ok" or "ok" or "Okay" or "okay":
                print("You have finished your test")
                time.sleep(1)
                print("State the following as shown between the speech marks...")
                Proceed_to_LogoutOrNot()
        
        
        
        
        

    def Proceed_to_LogoutOrNot():
        finish=input("Do you want to proceed to 'log out' or create 'another study flashcard test'? ")
        if finish == "log out":
            LogoutUserPass()
        if finish == "another study flashcard test":
            StudyHelpAppDataGather()
            


    def LogoutUserPass():
        User=input("Username: ")
        if User == "HuamanDaBoss21":
            Pass=input("Password: ")
        if Pass == "Asbonk99":
            print("Hope you studied well. Good luck in your exam!")
            time.sleep(2)
            print("Python Flashcard Study Helper will close in 10 seconds...")
            time.sleep(10)

    
def TimeToCloseDownOrNot():
    time.sleep(3)
    death=input('Do you want me to close now?')
    if death=='yes':
        time.sleep(0.8)
    elif death!='yes':
        print("Ok, I won't close now, I restart in 5 seconds ;)")
        time.sleep(0.5)
        print("4 seconds left...")
        time.sleep(1)
        os.system('cls')
        print("3 seconds left...")
        time.sleep(1)
        os.system('cls')
        print("2 seconds left...")
        time.sleep(1)
        os.system('cls')
        print("1 seconds left...")
        time.sleep(1)
        os.system('cls')
        actualAI()

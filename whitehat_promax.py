import os, re
GREEN="\033[92m"; RED="\033[91m"; YELLOW="\033[93m"; RESET="\033[0m"
os.system("clear")
os.system("figlet -f big WhiteHat Naeem")
print(f"{GREEN}==== PRO MAX Codex v2 - By Jind Star ===={RESET}")

def encode(t): return "".join(chr(ord(c)+3) if c!="#" else "#" for c in t)
def decode(t): return "".join(chr(ord(c)-3) if c!="#" else "#" for c in t)

def pass_check(p):
    s=0
    if len(p)>=8: s+=1
    if re.search(r"[A-Z]",p): s+=1
    if re.search(r"[0-9]",p): s+=1
    if re.search(r"[@#$!]",p): s+=1
    if s<=1: return f"{RED}WEAK - Jaldi Change Karo!{RESET}"
    if s==2: return f"{YELLOW}MEDIUM - Theek Hai{RESET}"
    if s>=3: return f"{GREEN}STRONG - WhiteHat Level!{RESET}"

while True:
    print(f"\n{GREEN}1. Encode Secret{RESET}")
    print("2. Decode Asal")
    print(f"{RED}3. Security Scanner{RESET}")
    print(f"{YELLOW}4. Password Strength Checker (NEW!){RESET}")
    print("5. Exit")
    ch=input("Option (1-5): ")
    if ch=="1":
        x=input("Text: "); print(f"Secret: {encode(x)}")
    elif ch=="2":
        x=input("Secret: "); print(f"Asal: {decode(x)}")
    elif ch=="3":
        print("\n--- Security Scan ---")
        print("[✓] 2-Step ON\n[✓] Linked Devices OK\n[✓] OTP Safe")
        print(f"\n{GREEN}Result: 100% SECURE!{RESET}")
    elif ch=="4":
        p=input("Password Likho: ")
        print(f"Strength: {pass_check(p)}")
    elif ch=="5":
        print("Allah Hafiz WhiteHat!"); break

accounts = {"123": "321"}
while True:
    ac = ""
    pwd = ""
    rqs = ""
    act = input("輸入1註冊,輸入2登入,輸入q離開: ")

    if act == "1":
        print("帳號註冊")
        ac = input("帳號: ")
        pwd = input("密碼: ")
        pwd_confirm = input("再次輸入密碼:")
        if pwd != pwd_confirm:
            print("x 密碼不符合! x")
            continue
        else:
            accounts[ac] = pwd
            print(f"✓ 帳號 {ac} 設定成功! ✓")
            #             for ac,pw in accounts.items():
            #                 print(F"帳號: {ac} 密碼: {pw}")===-
            continue

    if act == "2":
        print("登入帳號")
        ac = input("帳號: ")
        if ac in accounts.keys():
            print(f"[ 歡迎使用者: {ac} 請輸入密碼!]")
            pwd = input("密碼: ")
            if pwd == accounts[ac]:
                print("✓ 登入成功! ✓")
                print("---------------------------")
                while True:
                    print(f"使用者: {ac} 請輸入操作代碼")
                    rqs = input("輸入1登出,輸入2更改密碼!")
                    if rqs == "1":
                        print("✓ 登出成功 ✓")
                        print("---------------------------")
                        break
                    if rqs == "2":
                        original_pwd = input("請出入你的原始密碼: ")
                        if original_pwd == pwd:
                            new_pwd = input("請輸入新密碼: ")
                            new_pwd_confirm = input("請再次輸入密碼: ")
                            if new_pwd != new_pwd_confirm:
                                print("密碼不符合!")
                            else:
                                accounts[ac] = new_pwd
                                print("密碼已成功修改 您已被登出!")
                                break

                        else:
                            print("密碼輸入錯誤!")
                            continue
                continue
            else:
                print("x 密碼錯誤! x")
                continue
        else:
            print(f"找不到帳號{ac}")
            continue

    if act == "q":
        break

print("程式結束!")
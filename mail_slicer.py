def mail():
    email=input("Lütfen mailinizi giriniz; ")

    (username, domain) = email.split("@")

    print(f"Username; {username}\nDomain; {domain}")

mail()
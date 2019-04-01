print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램 입니다.")
cel=input("변환하고 싶은 섭씨온도를 입력하시오.")
far=(float(cel)*1.8)+32
print("섭씨온도:",cel,"C")
print("화씨온도:",far,"F")
print("이 프로그램은 화씨온도를 섭씨온도로 변환하는 프로그램입니다")
far=input("변환하고 싶은 화씨온도를 입력하시오.")
cel=(float(far)-32)*5/9
print("섭씨온도:""%0.1f"%cel,"C")
print("화씨온도:",far,"F")
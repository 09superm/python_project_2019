import pandas as pd
import numpy as np

# 수익률 정보 불러오기, returnD 수익률 정보 저장
returnD = pd.read_csv("returndata.csv")

# stock list 안내하기
print("____________ + Stock List + ____________\n\n"
      "[1] SK텔레콤, SK하이닉스, S-Oil, 고려아연, 기아차\n"
      "[2] 농심, 대한항공, 롯데케미칼, 삼성전자, LG\n"
      "[3] 오뚜기, POSCO, 한국전력, 한온시스템, 현대모비스\n"
      "[4] 현대건설, 현대차, 현대제철, 현대중공업, 호텔신라\n")

# 포트폴리오 입력 받기, your_input 입력값 저장
S1, S2, S3, S4, S5 = input("다음 20개의 종목 중 포트폴리오를 구성할 종목 5개를 입력하세요.(구분은 콤마)").split(",")
your_input = [S1, S2, S3, S4, S5]

# 입력값에 따른 열의 이름 불러오기, your_data 입력값에 따른 열이름 저장
your_data = []
stockDic = {"SK텔레콤":"A017670", "Sk하이닉스":"A000660", "S-Oil":"A010950", "고려아연":"A010130", "기아차":"A000270",
            "농심":"A004370", "대한항공":"A003490", "롯데케미칼":"A011170", "삼성전자":"A005930", "LG":"A003550",
            "오뚜기":"A007310", "POSCO":"A005490","한국전력":"A015760", "한온시스템":"A018880", "현대모비스":"A012330",
            "현대건설":"A000720", "현대차":"A005380", "현대제철":"A004020","현대중공업":"A009540", "호텔신라":"A008770"}

for s in your_input :
    if s in stockDic.keys() :
        s = stockDic[s]
        your_data.append(s)
    else:
        print("올바른 종목 이름을 입력하세요.")
        break


# 입력값에 따른 수익률 정보 저장하기, return_data 입력값 열이름에 따라 수익률 정보 저장
return_data = returnD.loc[5:237,your_data]

# pandas 데이터를 numpy 데이터로 변환하기 return_data_np
return_data_np = return_data.values
return_data_np = return_data_np.astype("float64") # 데이터 타입은 실수로 함

# 각 종목의 평균, 분산, 표준편차 ret, var, std
rt_ret = return_data_np.sum(axis=0)/ 233
rt_var = return_data_np.var(axis=0)
rt_std = return_data_np.std(axis=0)

# 각 종목의 공분산 covmat
covmat = np.cov(return_data_np, rowvar=0)

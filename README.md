<위험자산을 이용한 최소분산포트폴리오 도출>
=============
학과 | 학번 | 성명
---- | ---- | ---- 
경영학과 | 201743143 | 김수민

## 🛠 프로젝트 목적 및 동기
'계란을 한 바구니에 담지 말라.' 투자를 시작한다면 듣게 되는 투자 격언입니다. 계란을 한 바구니에 담으면 쉽게 깨지듯이,하나의 자산에 올인하기보다 포트폴리오를 통한 분산투자로 위험을 최소화하라는 의미입니다. 그렇다면 개개인은 포트폴리오를 구성한 후, 개별 자산의 투자비중을 어떻게 설정해야 가장 효율적이고 최적화된 투자를 할 수 있을까요?  2개의 자산으로 포트폴리오를 구성한다면 각각의 투자비중을 구하기 쉬울 것입니다. A,B 자산으로 구성했을 때,A 기업이 경영난을 겪고 있다고 가정한다면 A 10%, B 90%로 투자비중을 정하면 될 것입니다. 하지만 포트폴리오 구성 자산 수가 5개, 10개, 그리고 150개가 될 경우에는 어떻게 투자비중을 배분하나요? 감과 촉으로만으로는 개개인이 희망수익률에 따른 가장 효율적인 자산 투자비중을 알아내기 어렵습니다. 또한 임의로 투자비중을 정한다면 이에 따른 예상수익을 예측하기도 힘듭니다.   

따라서 저는 fnguide 에서 제공하는 수정주가 데이터를 이용하여 포트폴리오 최적화 자산배분 비율(투자비중)을 구하는 과정 중
최소분산포트폴리오(위험이 최소가 되는 투자비중)를 도출하는 프로그램을 만들어보려고 합니다.
개인이 선택한 포트폴리오에 따라 가장 위험이 최소가 되는 투자비중을 구하고, 그 비중에 따른 수익과 위험을 구할 것입니다.
차입,대출이 가능한 무위험자산은 제외하고 위험자산만 고려할 예정입니다.

## 🛠 프로젝트 개요
![기말보고서 흐름도파일](https://github.com/09superm/python_project_2019/blob/master/흐름도1.jpeg)
![기말보고서 흐름도파일](https://github.com/09superm/python_project_2019/blob/master/흐름도2.jpeg)



## 📊 사용한 공공데이터
* fnguide 수정주가 수익률 데이터

    [데이터보기](https://github.com/09superm/python_project_2019/blob/master/returndata.csv)
    (선택 가능한 자산은 KOSPI 200 중 2000 년 이후 모든 가격정보를 갖는 자산으로 한정, 20개 주식종목)



## 🛠 소스
1. 데이터 파일 불러오기 ~ 최적화함수 인풋 요소 만들기
* [링크로 소스 내용 보기](https://github.com/09superm/python_project_2019/blob/master/1.py) 

2. 최소분산포트폴리오 구하기 
* [링크로 소스 내용 보기](https://github.com/09superm/python_project_2019/blob/master/2.py) 

3. 그래프 그리기 
* [링크로 소스 내용 보기](https://github.com/09superm/python_project_2019/blob/master/3.py) 

* 코드 삽입
~~~python
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
# print(return_data)

# pandas 데이터를 numpy 데이터로 변환하기 return_data_np
return_data_np = return_data.values
return_data_np = return_data_np.astype("float64") # 데이터 타입은 실수로 함
# print(return_data_np)
# print("-----------------------")

# 각 종목의 평균, 분산, 표준편차 ret, var, std
rt_ret = return_data_np.sum(axis=0)/ 233
rt_var = return_data_np.var(axis=0)
rt_std = return_data_np.std(axis=0)

# 각 종목의 공분산 covmat
covmat = np.cov(return_data_np, rowvar=0)

# GMVP

def MinVol_objective(x): # 목적함수
    variance = x.T @ covmat @ x # 포트폴리오의 위험 = 비중 * 공분산 * 비중
    standard_deviation = variance ** 0.5  # std는 variance의 루트값
    return (standard_deviation)

def weight_sum_constraint(x): # 제약함수 x값의 합이 1
    return (x.sum() - 1.0)

def MinVol(covmat, lb, ub): # 최적화 구하는 함수 인풋 값은 covmat(공분산 매트릭스),lb(최소비중), ub(최대비중)
    x0 = np.repeat(1 / covmat.shape[1], covmat.shape[1]) # 동일 비중만큼 줌
    lbound = np.repeat(lb, covmat.shape[1]) # 최소비중
    ubound = np.repeat(ub, covmat.shape[1]) # 최대비중
    bnds = tuple(zip(lbound, ubound)) # 최소비중과 최대비중의 짝을 만들어줌

    constraints = ({"type": "eq", "fun": weight_sum_constraint}) # 제약조건

    result = minimize(fun=MinVol_objective,
                      x0=x0,
                      method="SLSQP",
                      constraints=constraints,
                      bounds=bnds)
    return (result.x)

gmvpwgt = MinVol(covmat,0,1)
# print("gmvp_wgt:",gmvpwgt)

gmvpret = "%0.6f" % rt_ret.dot(gmvpwgt)
gmvpvar = gmvpwgt.dot(gmvpwgt.dot(covmat))
gmvpstd = "%0.6f" % math.sqrt(gmvpvar)

# print("gmvp_ret:",gmvpret)
# print("gmvp_std:",gmvpstd)

print("\n===== 결과 =====\n")
print(str(your_input) + "로 포트폴리오를 구성했을 때,\n",
      your_input[0], gmvpwgt[0:1], your_input[1], gmvpwgt[1:2], your_input[2], gmvpwgt[2:3], your_input[3], gmvpwgt[3:4],your_input[4],str(gmvpwgt[4:5])
      + "만큼 투자하면 위험을 최소화할 수 있습니다.\n", "이 때 발생되는 위험은",gmvpstd, "수익률의 평균은", str(gmvpret), "입니다.")

# 그래프 만들기
font_name = font_manager.FontProperties(fname="/System/Library/Fonts/AppleSDGothicNeo.ttc").get_name()
rc('font', family=font_name)
style.use('ggplot')

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
labels = your_input
ratio = gmvpwgt
explode = (0.1, 0.1, 0.1, 0.1, 0.1)

plt.title("Global Minimum Volatility Portfolio\n")
plt.pie(ratio, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()
~~~

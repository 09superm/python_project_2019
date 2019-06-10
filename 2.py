import numpy as np
from scipy.optimize import minimize
import math

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

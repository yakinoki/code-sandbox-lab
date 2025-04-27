import math

def entropy(probabilities):
    entropy_val = 0.0
    for p in probabilities:
        if p > 0:
            entropy_val += -p * math.log2(p)
    return entropy_val


def kl_divergence(p, q):
    divergence = 0.0
    for i in range(len(p)):
        if p[i] > 0 and q[i] > 0:
            divergence += p[i] * math.log2(p[i] / q[i])
    return divergence


# 二つの確率分布を定義
p = [0.7, 0.2, 0.1]
q = [0.1, 0.4, 0.5]

# エントロピーを計算
entropy_p = entropy(p)
entropy_q = entropy(q)

# Kullback-Leibler ダイバージェンスを計算
kl_divergence_pq = kl_divergence(p, q)
kl_divergence_qp = kl_divergence(q, p)

# 結果を出力
print("Entropy of p:", entropy_p)
print("Entropy of q:", entropy_q)
# カルバック・ライブラー情報量には対称性がない。
print("KL Divergence from p to q:", kl_divergence_pq)
print("KL Divergence from q to p:", kl_divergence_qp)

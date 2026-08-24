# LeetCode 3343 - Count Number of Balanced Permutations
# https://leetcode.com/problems/count-number-of-balanced-permutations/


def modPow(a: int, e: int, mod: int) -> int:
    r = 1
    a %= mod
    while e > 0:
        if e & 1:
            r = r * a % mod
        a = a * a % mod
        e >>= 1
    return r


def key(a: int, b: int) -> int:
    return (a << 32) | (b & 0xFFFFFFFF)


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 1000000007
        cnt = [0] * 10
        ssum = 0
        for c in num:
            d = ord(c) - 48
            cnt[d] += 1
            ssum += d
        if ssum % 2 == 1:
            return 0
        n = len(num)
        half_n = n // 2
        half_s = ssum // 2
        fact = [0] * (n + 1)
        inv_f = [0] * (n + 1)
        fact[0] = 1
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % mod
        inv_f[n] = modPow(fact[n], mod - 2, mod)
        for i in range(n, 0, -1):
            inv_f[i - 1] = inv_f[i] * i % mod
        dp = {key(0, 0): 1}
        for d in range(10):
            ndp = {}
            for st, ways in dp.items():
                used = st >> 32
                s = st & 0xFFFFFFFF
                for take in range(cnt[d] + 1):
                    nu = used + take
                    ns = s + take * d
                    if nu > half_n or ns > half_s:
                        continue
                    w = ways * inv_f[take] % mod * inv_f[cnt[d] - take] % mod
                    nk = key(nu, ns)
                    ndp[nk] = (ndp.get(nk, 0) + w) % mod
            dp = ndp
        ans = dp.get(key(half_n, half_s), 0)
        ans = ans * fact[half_n] % mod * fact[n - half_n] % mod
        for d in range(10):
            ans = ans * fact[cnt[d]] % mod
        return ans

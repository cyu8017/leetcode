// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

#include <algorithm>
#include <vector>

class Solution {
    static constexpr int MX = 500000;
    static std::vector<int> S;
    static bool inited;

    static void ensureInit() {
        if (inited) return;
        std::vector<bool> isPrime(MX + 1, true);
        isPrime[0] = isPrime[1] = false;
        std::vector<int> primes;
        for (int i = 2; i <= MX; i++) {
            if (isPrime[i]) {
                primes.push_back(i);
                if (1LL * i * i <= MX) {
                    for (int j = i * i; j <= MX; j += i) isPrime[j] = false;
                }
            }
        }
        S = {0};
        int t = 0;
        for (int x : primes) {
            t += x;
            if (t > MX) break;
            if (isPrime[t]) S.push_back(t);
        }
        inited = true;
    }

public:
    int largestPrime(int n) {
        ensureInit();
        auto it = std::upper_bound(S.begin(), S.end(), n);
        return *std::prev(it);
    }
};

std::vector<int> Solution::S;
bool Solution::inited = false;

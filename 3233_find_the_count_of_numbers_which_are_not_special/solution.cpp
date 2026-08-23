// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

#include <cmath>
#include <vector>

class Solution {
    static constexpr int M = 31623;
    static std::vector<bool> primes;
    static bool inited;

    static void initPrimes() {
        if (inited) return;
        primes.assign(M + 1, true);
        primes[0] = primes[1] = false;
        for (int i = 2; i <= M; i++) {
            if (primes[i]) {
                for (int j = i * 2; j <= M; j += i) primes[j] = false;
            }
        }
        inited = true;
    }

public:
    int nonSpecialCount(int l, int r) {
        initPrimes();
        int lo = (int)std::ceil(std::sqrt((double)l));
        int hi = (int)std::floor(std::sqrt((double)r));
        int cnt = 0;
        for (int i = lo; i <= hi; i++) {
            if (primes[i]) cnt++;
        }
        return r - l + 1 - cnt;
    }
};

std::vector<bool> Solution::primes;
bool Solution::inited = false;

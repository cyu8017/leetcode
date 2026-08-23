// LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

#include <algorithm>
#include <vector>

class Solution {
    static inline bool ready = false;
    static inline bool isPrime[1001];

    static void init() {
        if (ready) return;
        for (int i = 0; i <= 1000; i++) isPrime[i] = true;
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= 1000; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= 1000; j += i) isPrime[j] = false;
            }
        }
        ready = true;
    }

public:
    int sumOfPrimesInRange(int n) {
        init();
        int r = 0;
        for (int x = n; x > 0; x /= 10) r = r * 10 + x % 10;
        int low = std::min(n, r), high = std::max(n, r);
        int ans = 0;
        for (int x = low; x <= high; x++) {
            if (isPrime[x]) ans += x;
        }
        return ans;
    }
};

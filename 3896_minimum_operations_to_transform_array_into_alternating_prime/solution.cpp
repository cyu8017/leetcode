// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

#include <algorithm>
#include <vector>

class Solution {
    static constexpr int MX = 200000;
    static inline std::vector<bool> isPrime;
    static inline std::vector<int> primes;
    static inline bool ready = false;

    static void init() {
        if (ready) return;
        isPrime.assign(MX + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i <= MX / i; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= MX; j += i) isPrime[j] = false;
            }
        }
        for (int i = 2; i <= MX; i++) {
            if (isPrime[i]) primes.push_back(i);
        }
        ready = true;
    }

public:
    int minOperations(std::vector<int>& nums) {
        init();
        int ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            int x = nums[i];
            if (i % 2 == 0) {
                auto it = std::lower_bound(primes.begin(), primes.end(), x);
                ans += *it - x;
            } else if (isPrime[x]) {
                ans += (x == 2) ? 2 : 1;
            }
        }
        return ans;
    }
};

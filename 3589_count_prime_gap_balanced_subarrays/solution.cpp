// LeetCode 3589 - Count Prime-Gap Balanced Subarrays
// https://leetcode.com/problems/count-prime-gap-balanced-subarrays/

#include <algorithm>
#include <vector>

class Solution {
public:
    int primeSubarray(std::vector<int>& nums, int k) {
        int mx = 0;
        for (int v : nums) mx = std::max(mx, v);
        std::vector<bool> isPrime(mx + 1, false);
        for (int i = 2; i <= mx; i++) isPrime[i] = true;
        for (int i = 2; i * i <= mx; i++)
            if (isPrime[i])
                for (int j = i * i; j <= mx; j += i) isPrime[j] = false;
        int n = (int)nums.size(), ans = 0;
        for (int l = 0; l < n; l++) {
            std::vector<int> primes;
            for (int r = l; r < n; r++) {
                if (isPrime[nums[r]]) primes.push_back(nums[r]);
                if ((int)primes.size() >= 2) {
                    int mn = primes[0], mxp = primes[0];
                    for (int p : primes) {
                        mn = std::min(mn, p);
                        mxp = std::max(mxp, p);
                    }
                    if (mxp - mn <= k) ans++;
                }
            }
        }
        return ans;
    }
};

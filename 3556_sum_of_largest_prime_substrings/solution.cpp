// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <cmath>

class Solution {
    bool isPrime(long long x) {
        if (x < 2) return false;
        long long sqrtX = (long long)std::sqrt((double)x);
        for (long long i = 2; i <= sqrtX; i++) if (x % i == 0) return false;
        return true;
    }
public:
    long long sumOfLargestPrimes(std::string s) {
        std::unordered_set<long long> st;
        int n = (int)s.size();
        for (int i = 0; i < n; i++) {
            long long x = 0;
            for (int j = i; j < n; j++) {
                x = x * 10 + (s[j] - '0');
                if (isPrime(x)) st.insert(x);
            }
        }
        std::vector<long long> nums(st.begin(), st.end());
        std::sort(nums.begin(), nums.end());
        long long ans = 0;
        for (int i = (int)nums.size() - 1; i >= 0 && (int)nums.size() - i <= 3; i--)
            ans += nums[i];
        return ans;
    }
};

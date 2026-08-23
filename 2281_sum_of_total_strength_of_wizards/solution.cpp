// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

#include <vector>

class Solution {
public:
    int totalStrength(std::vector<int>& strength) {
        const int mod = 1000000007;
        int n = (int)strength.size();
        std::vector<int> left(n), right(n), stack;
        for (int i = 0; i < n; ++i) {
            while (!stack.empty() && strength[stack.back()] >= strength[i]) stack.pop_back();
            left[i] = stack.empty() ? -1 : stack.back();
            stack.push_back(i);
        }
        stack.clear();
        for (int i = n - 1; i >= 0; --i) {
            while (!stack.empty() && strength[stack.back()] > strength[i]) stack.pop_back();
            right[i] = stack.empty() ? n : stack.back();
            stack.push_back(i);
        }
        std::vector<long long> pref(n + 1), prefPref(n + 2);
        for (int i = 0; i < n; ++i) pref[i + 1] = (pref[i] + strength[i]) % mod;
        for (int i = 0; i <= n; ++i) prefPref[i + 1] = (prefPref[i] + pref[i]) % mod;
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            int l = left[i] + 1, r = right[i] - 1;
            long long leftSum = (prefPref[i + 1] - prefPref[l] + mod) % mod;
            long long rightSum = (prefPref[r + 2] - prefPref[i + 1] + mod) % mod;
            long long leftCnt = i - l + 1, rightCnt = r - i + 1;
            long long contrib = (rightCnt * leftSum % mod - leftCnt * rightSum % mod + mod) % mod;
            ans = (ans + contrib * strength[i] % mod) % mod;
        }
        return (int)ans;
    }
};

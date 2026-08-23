// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

#include <algorithm>
#include <vector>

class Solution {
    static int encrypt(int x) {
        int mx = 0, p = 0;
        for (; x > 0; x /= 10) {
            mx = std::max(mx, x % 10);
            p = p * 10 + 1;
        }
        return mx * p;
    }
public:
    int sumOfEncryptedInt(std::vector<int>& nums) {
        int ans = 0;
        for (int x : nums) ans += encrypt(x);
        return ans;
    }
};

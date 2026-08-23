// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int specialTriplets(std::vector<int>& nums) {
        std::unordered_map<int, int> left, right;
        for (int x : nums) right[x]++;
        long long ans = 0, mod = 1000000007;
        for (int x : nums) {
            right[x]--;
            ans = (ans + 1LL * left[x * 2] * right[x * 2] % mod) % mod;
            left[x]++;
        }
        return (int)ans;
    }
};

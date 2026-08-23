// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

#include <vector>
#include <algorithm>

class Solution {
public:
    int uniqueXorTriplets(std::vector<int>& nums) {
        int mx = *std::max_element(nums.begin(), nums.end()) << 1;
        std::vector<char> st(mx);
        for (int a : nums) for (int b : nums) st[a ^ b] = 1;
        std::vector<int> s(mx);
        for (int ab = 0; ab < mx; ab++) {
            if (st[ab]) for (int c : nums) s[ab ^ c] = 1;
        }
        int ans = 0;
        for (int v : s) ans += v;
        return ans;
    }
};

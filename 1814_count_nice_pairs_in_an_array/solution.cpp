// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int countNicePairs(std::vector<int>& nums) {
        const int MOD = 1000000007;
        std::unordered_map<int, int> freq;
        long long ans = 0;
        for (int num : nums) {
            int diff = num - rev(num);
            ans = (ans + freq[diff]) % MOD;
            freq[diff] += 1;
        }
        return static_cast<int>(ans);
    }

private:
    int rev(int x) {
        std::string s = std::to_string(x);
        std::reverse(s.begin(), s.end());
        return std::stoi(s);
    }
};

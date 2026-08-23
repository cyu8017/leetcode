// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int beautifulSubsets(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        std::unordered_map<int, std::vector<int>> groups;
        for (auto& [x, _] : freq) groups[x % k].push_back(x);
        int ans = 1;
        for (auto& [_, vals] : groups) {
            std::sort(vals.begin(), vals.end());
            int prevTake = 0, prevSkip = 1;
            int prevVal = -(1 << 30);
            for (int v : vals) {
                int ways = 1;
                for (int i = 0; i < freq[v]; ++i) ways *= 2;
                ways--;
                int skip = prevTake + prevSkip;
                int take = ways * prevSkip;
                if (prevVal + k != v) take += ways * prevTake;
                prevTake = take;
                prevSkip = skip;
                prevVal = v;
            }
            ans *= prevTake + prevSkip;
        }
        return ans - 1;
    }
};

// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> longestCommonSubsequence(std::vector<std::vector<int>>& arrays) {
        std::unordered_map<int, int> cnt;
        for (auto& arr : arrays) for (int x : arr) cnt[x]++;
        int m = (int)arrays.size();
        std::vector<int> ans;
        for (int x : arrays[0]) if (cnt[x] == m) ans.push_back(x);
        return ans;
    }
};

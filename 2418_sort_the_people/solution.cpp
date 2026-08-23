// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> sortPeople(std::vector<std::string>& names, std::vector<int>& heights) {
        int n = (int)names.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b) { return heights[a] > heights[b]; });
        std::vector<std::string> ans(n);
        for (int i = 0; i < n; i++) ans[i] = names[idx[i]];
        return ans;
    }
};

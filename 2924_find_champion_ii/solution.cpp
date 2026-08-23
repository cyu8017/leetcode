// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

#include <vector>

class Solution {
public:
    int findChampion(int n, std::vector<std::vector<int>>& edges) {
        std::vector<int> indeg(n);
        for (auto& e : edges) indeg[e[1]]++;
        int ans = -1;
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0) {
                if (ans != -1) return -1;
                ans = i;
            }
        }
        return ans;
    }
};

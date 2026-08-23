// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

#include <vector>

class Solution {
public:
    int edgeScore(std::vector<int>& edges) {
        int n = (int)edges.size();
        std::vector<long long> score(n);
        for (int i = 0; i < n; i++) score[edges[i]] += i;
        int ans = 0;
        for (int i = 1; i < n; i++) {
            if (score[i] > score[ans]) ans = i;
        }
        return ans;
    }
};

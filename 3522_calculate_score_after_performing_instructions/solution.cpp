// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

#include <string>
#include <vector>

class Solution {
public:
    long long calculateScore(std::vector<std::string>& instructions, std::vector<int>& values) {
        int n = (int)values.size();
        std::vector<char> vis(n);
        long long ans = 0;
        int i = 0;
        while (i >= 0 && i < n && !vis[i]) {
            vis[i] = 1;
            if (instructions[i][0] == 'a') {
                ans += values[i];
                i += 1;
            } else {
                i += values[i];
            }
        }
        return ans;
    }
};

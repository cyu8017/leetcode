// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

#include <vector>

class Solution {
public:
    std::vector<int> circularGameLosers(int n, int k) {
        std::vector<char> seen(n + 1);
        int cur = 1, step = 1;
        while (!seen[cur]) {
            seen[cur] = 1;
            cur = (cur - 1 + step * k) % n + 1;
            step++;
        }
        std::vector<int> ans;
        for (int i = 1; i <= n; i++) if (!seen[i]) ans.push_back(i);
        return ans;
    }
};

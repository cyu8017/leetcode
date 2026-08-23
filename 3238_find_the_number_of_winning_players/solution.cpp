// LeetCode 3238 - Find the Number of Winning Players
// https://leetcode.com/problems/find-the-number-of-winning-players/

#include <array>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int winningPlayerCount(int n, std::vector<std::vector<int>>& pick) {
        std::vector<std::array<int, 11>> cnt(n);
        for (auto& a : cnt) a.fill(0);
        std::unordered_set<int> s;
        for (auto& p : pick) {
            int x = p[0], y = p[1];
            cnt[x][y]++;
            if (cnt[x][y] > x) s.insert(x);
        }
        return (int)s.size();
    }
};

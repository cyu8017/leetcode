// LeetCode 1583 - Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int unhappyFriends(int n, std::vector<std::vector<int>>& preferences,
                       std::vector<std::vector<int>>& pairs) {
        std::vector<std::unordered_map<int, int>> rank(n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < static_cast<int>(preferences[i].size()); ++j) {
                rank[i][preferences[i][j]] = j;
            }
        }
        std::vector<int> partner(n);
        for (const auto& pair : pairs) {
            partner[pair[0]] = pair[1];
            partner[pair[1]] = pair[0];
        }
        int unhappy = 0;
        for (int x = 0; x < n; ++x) {
            const int y = partner[x];
            const int limit = rank[x][y];
            bool isUnhappy = false;
            for (int i = 0; i < limit; ++i) {
                const int u = preferences[x][i];
                if (rank[u][x] < rank[u][partner[u]]) {
                    isUnhappy = true;
                    break;
                }
            }
            if (isUnhappy) {
                ++unhappy;
            }
        }
        return unhappy;
    }
};

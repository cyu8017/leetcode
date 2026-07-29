// LeetCode 1222 - Queens That Can Attack the King
// https://leetcode.com/problems/queens-that-can-attack-the-king/

#include <set>
#include <utility>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> queensAttacktheKing(std::vector<std::vector<int>>& queens, std::vector<int>& king) {
        std::set<std::pair<int, int>> occupied;
        for (const auto& q : queens) {
            occupied.insert({q[0], q[1]});
        }
        std::vector<std::vector<int>> answer;
        for (int dr = -1; dr <= 1; ++dr) {
            for (int dc = -1; dc <= 1; ++dc) {
                if (dr == 0 && dc == 0) {
                    continue;
                }
                int r = king[0] + dr, c = king[1] + dc;
                while (r >= 0 && r < 8 && c >= 0 && c < 8) {
                    if (occupied.count({r, c})) {
                        answer.push_back({r, c});
                        break;
                    }
                    r += dr;
                    c += dc;
                }
            }
        }
        return answer;
    }
};

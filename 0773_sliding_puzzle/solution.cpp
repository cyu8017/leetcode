// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    int slidingPuzzle(std::vector<std::vector<int>>& board) {
        std::string start;
        for (const auto& row : board) {
            for (int cell : row) {
                start.push_back(static_cast<char>('0' + cell));
            }
        }
        const std::string target = "123450";
        static const std::unordered_map<int, std::vector<int>> neighbors{
            {0, {1, 3}}, {1, {0, 2, 4}}, {2, {1, 5}},
            {3, {0, 4}}, {4, {1, 3, 5}}, {5, {2, 4}},
        };
        std::queue<std::pair<std::string, int>> q;
        std::unordered_set<std::string> seen{start};
        q.push({start, 0});
        while (!q.empty()) {
            auto [state, steps] = q.front();
            q.pop();
            if (state == target) {
                return steps;
            }
            int zero = static_cast<int>(state.find('0'));
            for (int nei : neighbors.at(zero)) {
                std::string nxt = state;
                std::swap(nxt[zero], nxt[nei]);
                if (!seen.count(nxt)) {
                    seen.insert(nxt);
                    q.push({nxt, steps + 1});
                }
            }
        }
        return -1;
    }
};

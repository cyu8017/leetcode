// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

#include <algorithm>
#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int snakesAndLadders(std::vector<std::vector<int>>& board) {
        int n = (int)board.size();
        int target = n * n;

        auto pos = [&](int square) {
            square--;
            int row = square / n;
            int rem = square % n;
            int r = n - 1 - row;
            int c = (row % 2 == 0) ? rem : n - 1 - rem;
            return std::pair<int, int>{r, c};
        };

        std::queue<int> q;
        std::vector<char> seen(target + 1, 0);
        q.push(1);
        seen[1] = 1;
        int moves = 0;
        while (!q.empty()) {
            int sz = (int)q.size();
            for (int s = 0; s < sz; s++) {
                int cur = q.front();
                q.pop();
                if (cur == target) return moves;
                int lim = std::min(cur + 6, target);
                for (int nxt = cur + 1; nxt <= lim; nxt++) {
                    auto [r, c] = pos(nxt);
                    int dest = board[r][c] != -1 ? board[r][c] : nxt;
                    if (!seen[dest]) {
                        seen[dest] = 1;
                        q.push(dest);
                    }
                }
            }
            moves++;
        }
        return -1;
    }
};

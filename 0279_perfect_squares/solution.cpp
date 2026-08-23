// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int numSquares(int n) {
        std::vector<int> squares;
        for (int value = 1; value * value <= n; value++) {
            squares.push_back(value * value);
        }

        std::queue<std::pair<int, int>> queue;
        queue.push({ n, 0 });
        std::unordered_set<int> visited;
        visited.insert(n);

        while (!queue.empty()) {
            auto [remain, steps] = queue.front();
            queue.pop();
            if (remain == 0) {
                return steps;
            }
            for (int square : squares) {
                int next = remain - square;
                if (next < 0) {
                    break;
                }
                if (visited.insert(next).second) {
                    queue.push({ next, steps + 1 });
                }
            }
        }
        return 0;
    }
};

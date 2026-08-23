// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int minimumOperationsToMakeEqual(int x, int y) {
        if (x <= y) return y - x;
        std::queue<std::pair<int, int>> q;
        q.push({x, 0});
        std::unordered_set<int> seen{x};
        while (!q.empty()) {
            auto [v, d] = q.front();
            q.pop();
            if (v == y) return d;
            std::vector<int> cands{v + 1, v - 1};
            if (v % 11 == 0) cands.push_back(v / 11);
            if (v % 5 == 0) cands.push_back(v / 5);
            for (int nxt : cands) {
                if (nxt > 0 && nxt < 2 * x + 20 && !seen.count(nxt)) {
                    seen.insert(nxt);
                    q.push({nxt, d + 1});
                }
            }
        }
        return -1;
    }
};

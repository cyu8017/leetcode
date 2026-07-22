// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

#include <algorithm>
#include <queue>
#include <unordered_set>
#include <utility>
#include <vector>

class Solution {
public:
    int minimumJumps(std::vector<int>& forbidden, int a, int b, int x) {
        std::unordered_set<int> bad(forbidden.begin(), forbidden.end());
        int limit = x;
        if (!forbidden.empty()) {
            limit = std::max(limit, *std::max_element(forbidden.begin(), forbidden.end()));
        }
        limit += a + b;
        std::queue<std::tuple<int, int, bool>> q;
        q.emplace(0, 0, false);
        std::unordered_set<long long> seen;
        seen.insert(0LL);
        auto key = [](int pos, bool back) -> long long {
            return (static_cast<long long>(pos) << 1) | (back ? 1 : 0);
        };
        while (!q.empty()) {
            auto [pos, dist, back] = q.front();
            q.pop();
            if (pos == x) {
                return dist;
            }
            int forward = pos + a;
            if (forward >= 0 && forward <= limit && !bad.count(forward) && !seen.count(key(forward, false))) {
                seen.insert(key(forward, false));
                q.emplace(forward, dist + 1, false);
            }
            if (!back) {
                int backward = pos - b;
                if (backward >= 0 && backward <= limit && !bad.count(backward) && !seen.count(key(backward, true))) {
                    seen.insert(key(backward, true));
                    q.emplace(backward, dist + 1, true);
                }
            }
        }
        return -1;
    }
};

// LeetCode 1815 - Maximum Number of Groups Getting Fresh Donuts
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/

#include <algorithm>
#include <map>
#include <utility>
#include <vector>

class Solution {
public:
    int maxHappyGroups(int batchSize, std::vector<int>& groups) {
        std::vector<int> count(batchSize, 0);
        for (int size : groups) {
            count[size % batchSize] += 1;
        }
        memo.clear();
        int ans = dfs(0, count, batchSize);
        if (count[0]) {
            ans += count[0] - 1;
        }
        return ans;
    }

private:
    std::map<std::pair<int, std::vector<int>>, int> memo;

    int dfs(int remainder, std::vector<int> state, int batchSize) {
        auto key = std::make_pair(remainder, state);
        auto it = memo.find(key);
        if (it != memo.end()) {
            return it->second;
        }
        int best = 0;
        for (int mod = 1; mod < batchSize; ++mod) {
            if (state[mod] == 0) {
                continue;
            }
            state[mod] -= 1;
            best = std::max(best, dfs((remainder + mod) % batchSize, state, batchSize));
            state[mod] += 1;
        }
        if (remainder == 0) {
            ++best;
        }
        return memo[key] = best;
    }
};

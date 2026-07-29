// LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
#include <algorithm>
#include <climits>
#include <cstdlib>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int minimizeTheDifference(std::vector<std::vector<int>>& mat, int target) {
        std::unordered_set<int> possible = {0};
        for (auto& row : mat) {
            std::unordered_set<int> uniq(row.begin(), row.end());
            std::unordered_set<int> nxt;
            for (int s : possible) for (int x : uniq) nxt.insert(s + x);
            std::unordered_set<int> kept;
            int minAbove = INT_MAX;
            for (int v : nxt) {
                if (v <= target) kept.insert(v);
                else minAbove = std::min(minAbove, v);
            }
            if (minAbove != INT_MAX) kept.insert(minAbove);
            if (kept.empty()) {
                int mn = *std::min_element(nxt.begin(), nxt.end());
                kept.insert(mn);
            }
            possible.swap(kept);
        }
        int ans = INT_MAX;
        for (int v : possible) ans = std::min(ans, std::abs(v - target));
        return ans;
    }
};

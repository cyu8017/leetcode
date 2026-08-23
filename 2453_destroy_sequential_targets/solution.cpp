// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int destroyTargets(std::vector<int>& nums, int space) {
        std::unordered_map<int, int> cnt;
        for (int x : nums) cnt[x % space]++;
        int bestCnt = 0;
        for (auto& [mod, c] : cnt) {
            (void)mod;
            if (c > bestCnt) bestCnt = c;
        }
        int ans = 1000000000;
        for (auto& [mod, c] : cnt) {
            if (c == bestCnt) {
                for (int x : nums) {
                    if (x % space == mod && x < ans) ans = x;
                }
            }
        }
        return ans;
    }
};

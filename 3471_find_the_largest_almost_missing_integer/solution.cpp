// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

#include <vector>
#include <unordered_map>
#include <unordered_set>

class Solution {
public:
    int largestInteger(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::unordered_map<int, int> cnt;
        for (int i = 0; i + k <= n; i++) {
            std::unordered_set<int> seen;
            for (int j = i; j < i + k; j++) seen.insert(nums[j]);
            for (int x : seen) cnt[x]++;
        }
        int ans = -1;
        for (auto& [x, c] : cnt) {
            if (c == 1 && x > ans) ans = x;
        }
        return ans;
    }
};

// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

#include <unordered_set>
#include <vector>

class Solution {
public:
    long long countExcellentPairs(std::vector<int>& nums, int k) {
        std::unordered_set<int> uniq(nums.begin(), nums.end());
        std::vector<int> cnt(32);
        for (int x : uniq) {
            int bits = 0;
            for (int y = x; y > 0; y >>= 1) bits += y & 1;
            cnt[bits]++;
        }
        long long ans = 0;
        for (int i = 0; i < 32; i++) {
            for (int j = 0; j < 32; j++) {
                if (i + j >= k) ans += 1LL * cnt[i] * cnt[j];
            }
        }
        return ans;
    }
};

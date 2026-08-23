// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int mostFrequentEven(std::vector<int>& nums) {
        std::unordered_map<int, int> cnt;
        int ans = -1, best = 0;
        for (int x : nums) {
            if (x % 2 != 0) continue;
            cnt[x]++;
            if (cnt[x] > best || (cnt[x] == best && (ans == -1 || x < ans))) {
                best = cnt[x];
                ans = x;
            }
        }
        return ans;
    }
};

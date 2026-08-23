// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int minArrivalsToDiscard(std::vector<int>& arrivals, int w, int m) {
        std::unordered_map<int, int> cnt;
        int n = (int)arrivals.size();
        std::vector<int> marked(n, 0);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x = arrivals[i];
            if (i >= w) cnt[arrivals[i - w]] -= marked[i - w];
            if (cnt[x] >= m) ans++;
            else {
                marked[i] = 1;
                cnt[x]++;
            }
        }
        return ans;
    }
};

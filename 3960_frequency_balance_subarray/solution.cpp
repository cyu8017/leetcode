// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int getLength(std::vector<int>& nums) {
        int n = (int)nums.size();
        int ans = 1;
        for (int l = 0; l < n; l++) {
            std::unordered_map<int, int> cnt, freq;
            for (int r = l; r < n; r++) {
                int x = nums[r];
                int c = cnt[x];
                if (freq[c] > 0) {
                    if (--freq[c] == 0) freq.erase(c);
                }
                cnt[x] = c + 1;
                freq[cnt[x]]++;
                int cx = cnt[x];
                if ((int)cnt.size() == 1 || ((int)freq.size() == 2 && (freq[cx * 2] > 0 || (cx % 2 == 0 && freq[cx / 2] > 0)))) {
                    ans = std::max(ans, r - l + 1);
                }
            }
        }
        return ans;
    }
};

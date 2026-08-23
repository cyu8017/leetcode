// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

#include <vector>

class Solution {
public:
    int earliestSecondToMarkIndices(std::vector<int>& nums, std::vector<int>& changeIndices) {
        int n = (int)nums.size(), m = (int)changeIndices.size();
        auto ok = [&](int t) {
            std::vector<int> last(n + 1, 0);
            for (int s = 0; s < t; s++) last[changeIndices[s]] = s;
            int decrement = 0, marked = 0;
            for (int s = 0; s < t; s++) {
                int i = changeIndices[s];
                if (last[i] == s) {
                    if (decrement < nums[i - 1]) return false;
                    decrement -= nums[i - 1];
                    marked++;
                } else {
                    decrement++;
                }
            }
            return marked == n;
        };
        int l = 0, r = m + 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (ok(mid)) r = mid;
            else l = mid + 1;
        }
        return l > m ? -1 : l;
    }
};

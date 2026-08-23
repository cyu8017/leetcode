// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int countSubarrays(std::vector<int>& nums, int k) {
        int pos = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (nums[i] == k) {
                pos = i;
                break;
            }
        }
        std::unordered_map<int, int> bal;
        bal[0] = 1;
        int cur = 0;
        for (int i = pos - 1; i >= 0; i--) {
            cur += nums[i] < k ? -1 : 1;
            bal[cur]++;
        }
        int ans = bal[0] + bal[1];
        cur = 0;
        for (int i = pos + 1; i < (int)nums.size(); i++) {
            cur += nums[i] < k ? -1 : 1;
            ans += bal[-cur] + bal[1 - cur];
        }
        return ans;
    }
};

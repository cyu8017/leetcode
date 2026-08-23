// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countSubarrays(int[] nums, int k) {
        int pos = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == k) {
                pos = i;
                break;
            }
        }
        Map<Integer, Integer> bal = new HashMap<>();
        bal.put(0, 1);
        int cur = 0;
        for (int i = pos - 1; i >= 0; i--) {
            cur += nums[i] < k ? -1 : 1;
            bal.put(cur, bal.getOrDefault(cur, 0) + 1);
        }
        int ans = bal.getOrDefault(0, 0) + bal.getOrDefault(1, 0);
        cur = 0;
        for (int i = pos + 1; i < nums.length; i++) {
            cur += nums[i] < k ? -1 : 1;
            ans += bal.getOrDefault(-cur, 0) + bal.getOrDefault(1 - cur, 0);
        }
        return ans;
    }
}

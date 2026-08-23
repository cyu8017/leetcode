// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

using System.Collections.Generic;

public class Solution {
    public int CountSubarrays(int[] nums, int k) {
        int pos = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == k) {
                pos = i;
                break;
            }
        }
        var bal = new Dictionary<int, int>();
        bal[0] = 1;
        int cur = 0;
        for (int i = pos - 1; i >= 0; i--) {
            cur += nums[i] < k ? -1 : 1;
            if (!bal.ContainsKey(cur)) bal[cur] = 0;
            bal[cur]++;
        }
        int Get(int key) => bal.ContainsKey(key) ? bal[key] : 0;
        int ans = Get(0) + Get(1);
        cur = 0;
        for (int i = pos + 1; i < nums.Length; i++) {
            cur += nums[i] < k ? -1 : 1;
            ans += Get(-cur) + Get(1 - cur);
        }
        return ans;
    }
}

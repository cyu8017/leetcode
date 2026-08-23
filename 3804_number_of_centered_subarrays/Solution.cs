// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

using System.Collections.Generic;

public class Solution {
    public int CenteredSubarrays(int[] nums) {
        int n = nums.Length, ans = 0;
        for (int i = 0; i < n; i++) {
            var st = new HashSet<int>();
            int s = 0;
            for (int j = i; j < n; j++) {
                s += nums[j];
                st.Add(nums[j]);
                if (st.Contains(s)) ans++;
            }
        }
        return ans;
    }
}

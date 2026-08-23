// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int centeredSubarrays(int[] nums) {
        int n = nums.length, ans = 0;
        for (int i = 0; i < n; i++) {
            var st = new HashSet<Integer>();
            int s = 0;
            for (int j = i; j < n; j++) {
                s += nums[j];
                st.add(nums[j]);
                if (st.contains(s)) ans++;
            }
        }
        return ans;
    }
}

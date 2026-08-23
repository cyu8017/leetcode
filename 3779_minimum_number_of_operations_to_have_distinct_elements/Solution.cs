// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums) {
        var st = new HashSet<int>();
        for (int i = nums.Length - 1; i >= 0; i--) {
            if (st.Contains(nums[i])) return i / 3 + 1;
            st.Add(nums[i]);
        }
        return 0;
    }
}

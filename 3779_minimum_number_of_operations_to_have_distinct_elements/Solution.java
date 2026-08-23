// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minOperations(int[] nums) {
        var st = new HashSet<Integer>();
        for (int i = nums.length - 1; i >= 0; i--) {
            if (st.contains(nums[i])) return i / 3 + 1;
            st.add(nums[i]);
        }
        return 0;
    }
}

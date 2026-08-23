// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] occurrencesOfElement(int[] nums, int[] queries, int x) {
        var ids = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i++) if (nums[i] == x) ids.add(i);
        int[] ans = new int[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int i = queries[qi];
            if (i - 1 < ids.size()) ans[qi] = ids.get(i - 1);
            else ans[qi] = -1;
        }
        return ans;
    }
}

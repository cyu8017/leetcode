// LeetCode 0830 - Positions of Large Groups
// https://leetcode.com/problems/positions-of-large-groups/

import java.util.*;

class Solution {
    public List<List<Integer>> largeGroupPositions(String s) {
        List<List<Integer>> ans = new ArrayList<>();
        int n = s.length(), i = 0;
        while (i < n) {
            int j = i;
            while (j < n && s.charAt(j) == s.charAt(i)) j++;
            if (j - i >= 3) ans.add(Arrays.asList(i, j - 1));
            i = j;
        }
        return ans;
    }
}

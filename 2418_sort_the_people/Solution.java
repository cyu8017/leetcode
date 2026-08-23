// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

import java.util.Arrays;

class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        int n = names.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Integer.compare(heights[b], heights[a]));
        String[] ans = new String[n];
        for (int i = 0; i < n; i++) ans[i] = names[idx[i]];
        return ans;
    }
}

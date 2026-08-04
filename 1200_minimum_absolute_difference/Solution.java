// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

import java.util.*;

class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int best = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length - 1; i++) best = Math.min(best, arr[i + 1] - arr[i]);
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i + 1] - arr[i] == best) ans.add(Arrays.asList(arr[i], arr[i + 1]));
        }
        return ans;
    }
}

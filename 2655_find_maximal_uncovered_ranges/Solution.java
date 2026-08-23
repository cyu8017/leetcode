// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

import java.util.*;

class Solution {
    public int[][] findMaximalUncoveredRanges(int n, int[][] ranges) {
        Arrays.sort(ranges, Comparator.comparingInt(a -> a[0]));
        List<int[]> ans = new ArrayList<>();
        int cur = 0;
        for (int[] r : ranges) {
            if (r[0] > cur) ans.add(new int[] {cur, r[0] - 1});
            if (r[1] + 1 > cur) cur = r[1] + 1;
        }
        if (cur < n) ans.add(new int[] {cur, n - 1});
        return ans.toArray(new int[0][]);
    }
}

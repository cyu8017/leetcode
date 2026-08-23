// LeetCode 1560 - Most Visited Sector in a Circular Track
// https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

import java.util.*;

class Solution {
    public List<Integer> mostVisited(int n, int[] rounds) {
        int start = rounds[0], end = rounds[rounds.length - 1];
        List<Integer> ans = new ArrayList<>();
        if (start <= end) {
            for (int i = start; i <= end; i++) {
                ans.add(i);
            }
        } else {
            for (int i = 1; i <= end; i++) {
                ans.add(i);
            }
            for (int i = start; i <= n; i++) {
                ans.add(i);
            }
        }
        return ans;
    }
}

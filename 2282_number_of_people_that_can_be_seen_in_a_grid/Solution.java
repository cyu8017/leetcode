// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] seePeople(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        int[][] ans = new int[m][];
        for (int i = 0; i < m; i++) ans[i] = new int[n];
        for (int i = 0; i < m; i++) {
            var stack = new ArrayList<Integer>();
            for (int j = n - 1; j >= 0; j--) {
                int cnt = 0;
                while (stack.size() > 0 && heights[i][stack.get(stack.size() - 1)] < heights[i][j]) { stack.remove(stack.size() - 1); cnt++; }
                if (stack.size() > 0) cnt++;
                ans[i][j] += cnt;
                while (stack.size() > 0 && heights[i][stack.get(stack.size() - 1)] == heights[i][j]) stack.remove(stack.size() - 1);
                stack.add(j);
            }
        }
        for (int j = 0; j < n; j++) {
            var stack = new ArrayList<Integer>();
            for (int i = m - 1; i >= 0; i--) {
                int cnt = 0;
                while (stack.size() > 0 && heights[stack.get(stack.size() - 1)][j] < heights[i][j]) { stack.remove(stack.size() - 1); cnt++; }
                if (stack.size() > 0) cnt++;
                ans[i][j] += cnt;
                while (stack.size() > 0 && heights[stack.get(stack.size() - 1)][j] == heights[i][j]) stack.remove(stack.size() - 1);
                stack.add(i);
            }
        }
        return ans;
    }
}

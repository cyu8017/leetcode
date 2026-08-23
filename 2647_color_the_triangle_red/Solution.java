// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/

import java.util.*;

class Solution {
    public int[][] colorRed(int n) {
        List<int[]> ans = new ArrayList<>();
        for (int i = 1; i <= n; i++) ans.add(new int[] {i, 1});
        for (int i = n % 2 + 2; i <= n; i += 2)
            for (int j = 2; j <= 2 * (n - i) + 2; j++)
                ans.add(new int[] {i, j});
        return ans.toArray(new int[0][]);
    }
}

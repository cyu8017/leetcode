// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

import java.util.*;

class Solution {
    public int[] beautifulArray(int n) {
        if (n == 1) return new int[] {1};
        int[] left = beautifulArray((n + 1) / 2);
        int[] right = beautifulArray(n / 2);
        int[] ans = new int[n];
        int k = 0;
        for (int x : left) ans[k++] = 2 * x - 1;
        for (int x : right) ans[k++] = 2 * x;
        return ans;
    }
}

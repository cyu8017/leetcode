// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

import java.util.Arrays;

class Solution {
    public boolean simpleGraphExists(int[] degrees) {
        int n = degrees.length;
        int[] d = degrees.clone();
        Arrays.sort(d);
        for (int i = 0, j = n - 1; i < j; i++, j--) {
            int tmp = d[i];
            d[i] = d[j];
            d[j] = tmp;
        }
        long sum = 0;
        for (int x : d) {
            if (x < 0 || x >= n) return false;
            sum += x;
        }
        if (sum % 2 == 1) return false;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + d[i];
        for (int k = 1; k <= n; k++) {
            long right = 0;
            for (int i = k; i < n; i++) right += d[i] < k ? d[i] : k;
            if (prefix[k] > 1L * k * (k - 1) + right) return false;
        }
        return true;
    }
}

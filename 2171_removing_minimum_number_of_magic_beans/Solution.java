// LeetCode 2171 - Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

import java.util.Arrays;

class Solution {
    public long minimumRemoval(int[] beans) {
        Arrays.sort(beans);
        int n = beans.length;
        long sum = 0;
        for (int b : beans) sum += b;
        long ans = sum;
        for (int i = 0; i < n; i++) {
            long remain = 1L * (n - i) * beans[i];
            ans = Math.min(ans, sum - remain);
        }
        return ans;
    }
}

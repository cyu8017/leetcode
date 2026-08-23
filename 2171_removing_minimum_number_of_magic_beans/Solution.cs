// LeetCode 2171 - Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

public class Solution {
    public long MinimumRemoval(int[] beans) {
        Array.Sort(beans);
        int n = beans.Length;
        long sum = 0;
        foreach (int b in beans) sum += b;
        long ans = sum;
        for (int i = 0; i < n; i++) {
            long remain = 1L * (n - i) * beans[i];
            ans = Math.Min(ans, sum - remain);
        }
        return ans;
    }
}

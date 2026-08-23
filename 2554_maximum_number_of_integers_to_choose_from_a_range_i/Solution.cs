// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

using System.Collections.Generic;

public class Solution {
    public int MaxCount(int[] banned, int n, int maxSum) {
        var ban = new HashSet<int>(banned);
        int ans = 0, sum = 0;
        for (int i = 1; i <= n; ++i) {
            if (ban.Contains(i)) continue;
            if (sum + i > maxSum) break;
            sum += i;
            ans++;
        }
        return ans;
    }
}

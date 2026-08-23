// LeetCode 2554 - Maximum Number of Integers to Choose From a Range I
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int maxCount(int[] banned, int n, int maxSum) {
        Set<Integer> ban = new HashSet<>();
        for (int x : banned) ban.add(x);
        int ans = 0;
        long sum = 0;
        for (int i = 1; i <= n; i++) {
            if (ban.contains(i)) continue;
            if (sum + i > maxSum) break;
            sum += i;
            ans++;
        }
        return ans;
    }
}

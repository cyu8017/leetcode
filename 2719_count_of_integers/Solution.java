// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/

import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    private int minSum, maxSum;

    public int count(String num1, String num2, int min_sum, int max_sum) {
        this.minSum = min_sum;
        this.maxSum = max_sum;
        return (dp(num2) - dp(dec(num1)) + MOD) % MOD;
    }

    private String dec(String s) {
        char[] arr = s.toCharArray();
        int i = arr.length - 1;
        while (i >= 0 && arr[i] == '0') {
            arr[i] = '9';
            i--;
        }
        if (i >= 0) arr[i]--;
        int j = 0;
        while (j < arr.length - 1 && arr[j] == '0') j++;
        return new String(arr, j, arr.length - j);
    }

    private int dp(String s) {
        Map<String, Integer> memo = new HashMap<>();
        return dfs(s, 0, 0, true, memo);
    }

    private int dfs(String s, int pos, int sum, boolean tight, Map<String, Integer> memo) {
        if (sum > maxSum) return 0;
        if (pos == s.length()) return sum >= minSum ? 1 : 0;
        String key = pos + "," + sum + "," + (tight ? 1 : 0);
        Integer cached = memo.get(key);
        if (cached != null) return cached;
        int up = tight ? s.charAt(pos) - '0' : 9;
        int res = 0;
        for (int d = 0; d <= up; d++)
            res = (res + dfs(s, pos + 1, sum + d, tight && d == up, memo)) % MOD;
        memo.put(key, res);
        return res;
    }
}

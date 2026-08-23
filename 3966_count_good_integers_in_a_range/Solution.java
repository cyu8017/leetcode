// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countGoodIntegers(long l, long r, int k) {
        return count(r, k) - count(l - 1, k);
    }

    private long count(long bound, int k) {
        if (bound <= 0) return 0;
        String digits = Long.toString(bound);
        Map<String, Long> memo = new HashMap<>();
        return dfs(0, 0, false, true, digits, k, memo);
    }

    private long dfs(int position, int previous, boolean started, boolean tight, String digits, int k, Map<String, Long> memo) {
        if (position == digits.length()) return started ? 1 : 0;
        String key = position + "," + previous + "," + started;
        if (!tight && memo.containsKey(key)) return memo.get(key);
        int limit = tight ? digits.charAt(position) - '0' : 9;
        long result = 0;
        for (int digit = 0; digit <= limit; digit++) {
            boolean nextStarted = started || digit != 0;
            if (started && Math.abs(previous - digit) > k) continue;
            int nextPrevious = nextStarted ? digit : previous;
            result += dfs(position + 1, nextPrevious, nextStarted, tight && digit == limit, digits, k, memo);
        }
        if (!tight) memo.put(key, result);
        return result;
    }
}

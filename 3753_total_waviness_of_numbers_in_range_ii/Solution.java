// LeetCode 3753 - Total Waviness Of Numbers In Range Ii
// https://leetcode.com/problems/total_waviness_of_numbers_in_range_ii/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    static class Result {
        long count, sum;
        Result() {}
        Result(long c, long s) { count = c; sum = s; }
    }

    private long wavinessUpTo(long limit) {
        if (limit < 0) return 0;
        List<Integer> digits = new ArrayList<>();
        if (limit == 0) digits.add(0);
        else {
            for (long value = limit; value > 0; value /= 10) digits.add((int) (value % 10));
            Collections.reverse(digits);
        }
        Map<String, Result> memo = new HashMap<>();
        return dfs(0, 10, 10, false, true, digits, memo).sum;
    }

    private Result dfs(int position, int secondLast, int last, boolean started, boolean tight,
                       List<Integer> digits, Map<String, Result> memo) {
        if (position == digits.size()) return new Result(1, 0);
        String key = position + "," + secondLast + "," + last + "," + started;
        if (!tight && memo.containsKey(key)) return memo.get(key);
        int upper = tight ? digits.get(position) : 9;
        Result result = new Result();
        for (int digit = 0; digit <= upper; digit++) {
            boolean nextTight = tight && digit == upper;
            int nextSecondLast = secondLast, nextLast = last;
            boolean nextStarted = started || digit != 0;
            long add = 0;
            if (!nextStarted) {
                nextSecondLast = nextLast = 10;
            } else if (!started) {
                nextSecondLast = 10;
                nextLast = digit;
            } else {
                if (secondLast != 10 &&
                    ((last > secondLast && last > digit) || (last < secondLast && last < digit))) {
                    add = 1;
                }
                nextSecondLast = last;
                nextLast = digit;
            }
            Result child = dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight, digits, memo);
            result.count += child.count;
            result.sum += child.sum + add * child.count;
        }
        if (!tight) memo.put(key, result);
        return result;
    }

    public long totalWaviness(long a, long b) {
        return wavinessUpTo(b) - wavinessUpTo(a - 1);
    }
}

// LeetCode 3753 - Total Waviness of Numbers in Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

using System.Collections.Generic;

public class Solution {
    struct Result {
        public long Count, Sum;
        public Result(long c, long s) { Count = c; Sum = s; }
    }

    long WavinessUpTo(long limit) {
        if (limit < 0) return 0;
        var digits = new List<int>();
        if (limit == 0) digits.Add(0);
        else {
            for (long value = limit; value > 0; value /= 10) digits.Add((int)(value % 10));
            digits.Reverse();
        }
        var memo = new Dictionary<(int, int, int, bool), Result>();
        Result Dfs(int position, int secondLast, int last, bool started, bool tight) {
            if (position == digits.Count) return new Result(1, 0);
            var key = (position, secondLast, last, started);
            if (!tight && memo.ContainsKey(key)) return memo[key];
            int upper = tight ? digits[position] : 9;
            Result result = new Result(0, 0);
            for (int digit = 0; digit <= upper; digit++) {
                bool nextTight = tight && digit == upper;
                int nextSecondLast = secondLast, nextLast = last;
                bool nextStarted = started || digit != 0;
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
                Result child = Dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight);
                result.Count += child.Count;
                result.Sum += child.Sum + add * child.Count;
            }
            if (!tight) memo[key] = result;
            return result;
        }
        return Dfs(0, 10, 10, false, true).Sum;
    }

    public long TotalWaviness(long a, long b) {
        return WavinessUpTo(b) - WavinessUpTo(a - 1);
    }
}

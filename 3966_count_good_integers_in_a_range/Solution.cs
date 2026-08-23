// LeetCode 3966 - Count Good Integers in a Range
// https://leetcode.com/problems/count-good-integers-in-a-range/

using System;
using System.Collections.Generic;

public class Solution {
    public long CountGoodIntegers(long l, long r, int k) {
        long Count(long bound) {
            if (bound <= 0) return 0;
            string digits = bound.ToString();
            var memo = new Dictionary<(int, int, bool), long>();
            long Dfs(int position, int previous, bool started, bool tight) {
                if (position == digits.Length) return started ? 1 : 0;
                var key = (position, previous, started);
                if (!tight && memo.TryGetValue(key, out long cached)) return cached;
                int limit = tight ? digits[position] - '0' : 9;
                long result = 0;
                for (int digit = 0; digit <= limit; digit++) {
                    bool nextStarted = started || digit != 0;
                    if (started && Math.Abs(previous - digit) > k) continue;
                    int nextPrevious = nextStarted ? digit : previous;
                    result += Dfs(position + 1, nextPrevious, nextStarted, tight && digit == limit);
                }
                if (!tight) memo[key] = result;
                return result;
            }
            return Dfs(0, 0, false, true);
        }
        return Count(r) - Count(l - 1);
    }
}

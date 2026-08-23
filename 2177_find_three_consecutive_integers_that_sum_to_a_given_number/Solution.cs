// LeetCode 2177 - Find Three Consecutive Integers That Sum to a Given Number
// https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

public class Solution {
    public long[] SumOfThree(long num) {
        if (num % 3 != 0) return Array.Empty<long>();
        long x = num / 3;
        return new[] { x - 1, x, x + 1 };
    }
}

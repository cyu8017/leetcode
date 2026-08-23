// LeetCode 2177 - Find Three Consecutive Integers That Sum to a Given Number
// https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution {
    public long[] sumOfThree(long num) {
        if (num % 3 != 0) return new long[0];
        long x = num / 3;
        return new long[] {x - 1, x, x + 1};
    }
}

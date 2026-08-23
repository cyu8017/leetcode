// LeetCode 0600 - Non-negative Integers without Consecutive Ones
// https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

class Solution {
    public int findIntegers(int n) {
        int[] fib = new int[32];
        fib[0] = 1;
        fib[1] = 2;
        for (int i = 2; i < 32; ++i) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }

        int answer = 0;
        int prevBit = 0;
        for (int bit = 30; bit >= 0; --bit) {
            if ((n & (1 << bit)) != 0) {
                answer += fib[bit];
                if (prevBit == 1) {
                    return answer;
                }
                prevBit = 1;
            } else {
                prevBit = 0;
            }
        }
        return answer + 1;
    }
}

// LeetCode 0509 - Fibonacci Number
// https://leetcode.com/problems/fibonacci-number/

public class Solution {
    public int Fib(int n) {
        if (n <= 1) {
            return n;
        }
        int previous = 0;
        int current = 1;
        for (int index = 2; index <= n; index++) {
            int next = previous + current;
            previous = current;
            current = next;
        }
        return current;
    }
}

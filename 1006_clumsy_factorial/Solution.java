// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int clumsy(int n) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(n--);
        int op = 0;
        while (n > 0) {
            if (op % 4 == 0) stack.push(stack.pop() * n);
            else if (op % 4 == 1) stack.push(stack.pop() / n);
            else if (op % 4 == 2) stack.push(n);
            else stack.push(-n);
            n--;
            op++;
        }
        int sum = 0;
        for (int x : stack) sum += x;
        return sum;
    }
}

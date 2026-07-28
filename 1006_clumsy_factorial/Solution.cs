// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

using System.Collections.Generic;

public class Solution {
    public int Clumsy(int n) {
        var stack = new List<int> { n };
        n--;
        int op = 0;
        while (n > 0) {
            if (op % 4 == 0) {
                stack[stack.Count - 1] *= n;
            } else if (op % 4 == 1) {
                stack[stack.Count - 1] = stack[stack.Count - 1] / n;
            } else if (op % 4 == 2) {
                stack.Add(n);
            } else {
                stack.Add(-n);
            }
            n--;
            op++;
        }
        int sum = 0;
        foreach (int x in stack) sum += x;
        return sum;
    }
}

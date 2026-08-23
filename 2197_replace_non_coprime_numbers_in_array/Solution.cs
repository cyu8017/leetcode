// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

using System.Collections.Generic;

public class Solution {
    public int[] ReplaceNonCoprimes(int[] nums) {
        int Gcd(int a, int b) {
            while (b != 0) { int t = a % b; a = b; b = t; }
            return a;
        }
        var stack = new List<int>();
        foreach (int x0 in nums) {
            int x = x0;
            while (stack.Count > 0) {
                int g = Gcd(stack[stack.Count - 1], x);
                if (g == 1) break;
                x = stack[stack.Count - 1] / g * x;
                stack.RemoveAt(stack.Count - 1);
            }
            stack.Add(x);
        }
        return stack.ToArray();
    }
}

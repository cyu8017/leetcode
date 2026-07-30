// LeetCode 1414 - Find The Minimum Number Of Fibonacci Numbers Whose Sum Is K
// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

using System.Collections.Generic;
public class Solution {
    public int FindMinFibonacciNumbers(int k) {
        var fib = new List<int> { 1, 1 };
        while (fib[fib.Count - 1] < k) fib.Add(fib[fib.Count - 1] + fib[fib.Count - 2]);
        int answer = 0;
        for (int i = fib.Count - 1; i >= 0; i--)
            if (fib[i] <= k) { k -= fib[i]; answer++; }
        return answer;
    }
}

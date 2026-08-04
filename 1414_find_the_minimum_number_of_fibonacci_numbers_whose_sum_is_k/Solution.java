// LeetCode 1414 - Find The Minimum Number Of Fibonacci Numbers Whose Sum Is K
// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

import java.util.*;

class Solution {
    public int findMinFibonacciNumbers(int k) {
        List<Integer> fib = new ArrayList<>();
        fib.add(1);
        fib.add(1);
        while (fib.get(fib.size() - 1) < k) {
            fib.add(fib.get(fib.size() - 1) + fib.get(fib.size() - 2));
        }
        int answer = 0;
        for (int i = fib.size() - 1; i >= 0; i--) {
            if (fib.get(i) <= k) {
                k -= fib.get(i);
                answer++;
            }
        }
        return answer;
    }
}

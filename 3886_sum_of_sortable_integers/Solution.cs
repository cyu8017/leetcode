// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

using System;
using System.Collections.Generic;

public class Solution {
    bool RotationMatches(int[] block, int[] target) {
        int k = block.Length;
        var prefix = new int[k];
        for (int i = 1; i < k; i++) {
            int j = prefix[i - 1];
            while (j > 0 && target[i] != target[j]) j = prefix[j - 1];
            if (target[i] == target[j]) j++;
            prefix[i] = j;
        }
        int matched = 0;
        for (int i = 0; i < 2 * k - 1; i++) {
            int x = block[i % k];
            while (matched > 0 && x != target[matched]) matched = prefix[matched - 1];
            if (x == target[matched]) matched++;
            if (matched == k) return true;
        }
        return false;
    }

    public int SumOfSortableIntegers(int[] nums) {
        int n = nums.Length;
        var sorted = (int[])nums.Clone();
        Array.Sort(sorted);
        var divisors = new List<int>();
        for (int d = 1; d * d <= n; d++) {
            if (n % d == 0) {
                divisors.Add(d);
                if (d * d != n) divisors.Add(n / d);
            }
        }
        int answer = 0;
        foreach (int k in divisors) {
            bool ok = true;
            for (int start = 0; start < n; start += k) {
                var block = new int[k];
                var target = new int[k];
                Array.Copy(nums, start, block, 0, k);
                Array.Copy(sorted, start, target, 0, k);
                if (!RotationMatches(block, target)) {
                    ok = false;
                    break;
                }
            }
            if (ok) answer += k;
        }
        return answer;
    }
}

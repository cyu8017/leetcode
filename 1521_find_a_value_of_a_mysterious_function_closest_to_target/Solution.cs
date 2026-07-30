// LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int ClosestToTarget(int[] arr, int target) {
        int answer = int.MaxValue;
        var current = new HashSet<int>();
        foreach (int value in arr) {
            var next = new HashSet<int> { value };
            foreach (int previous in current) next.Add(value & previous);
            current = next;
            foreach (int candidate in current) {
                answer = Math.Min(answer, Math.Abs(candidate - target));
            }
        }
        return answer;
    }
}

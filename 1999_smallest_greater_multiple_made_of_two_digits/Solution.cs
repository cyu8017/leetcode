// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int FindInteger(int k, int digit1, int digit2) {
        var digits = new SortedSet<int> { digit1, digit2 }.ToList();
        var q = new Queue<long>();
        var seen = new HashSet<long>();
        foreach (int d in digits) {
            if (d != 0) { q.Enqueue(d); seen.Add(d); }
        }
        if (q.Count == 0) return -1;
        while (q.Count > 0) {
            long x = q.Dequeue();
            if (x > k && x % k == 0) return (int)x;
            foreach (int d in digits) {
                long nx = x * 10 + d;
                if (nx <= int.MaxValue && seen.Add(nx)) q.Enqueue(nx);
            }
        }
        return -1;
    }
}
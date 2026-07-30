// LeetCode 1354 - Construct Target Array With Multiple Sums
// https://leetcode.com/problems/construct-target-array-with-multiple-sums/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    public bool IsPossible(int[] target) {
        if (target.Length == 1) return target[0] == 1;
        long total = target.Sum(x => (long)x);
        var h = new PriorityQueue<int, long>();
        foreach (int x in target) h.Enqueue(x, -x);
        while (true) {
            int x = h.Dequeue();
            long rest = total - x;
            if (x == 1 || rest == 1) return true;
            if (rest == 0 || x <= rest) return false;
            long prev = x % rest;
            if (prev == 0) return false;
            total = rest + prev;
            h.Enqueue((int)prev, -prev);
        }
    }
}

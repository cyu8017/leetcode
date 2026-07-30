// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> CountSteppingNumbers(int low, int high) {
        var answer = new List<int>();
        if (low == 0) answer.Add(0);
        var q = new Queue<int>();
        for (int i = 1; i < 10; i++) q.Enqueue(i);

        while (q.Count > 0) {
            int x = q.Dequeue();
            if (x > high) continue;
            if (x >= low) answer.Add(x);
            int last = x % 10;
            if (last > 0) q.Enqueue(x * 10 + last - 1);
            if (last < 9) q.Enqueue(x * 10 + last + 1);
        }
        return answer.OrderBy(v => v).ToList();
    }
}

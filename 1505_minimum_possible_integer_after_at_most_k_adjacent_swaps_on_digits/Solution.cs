// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

using System.Collections.Generic;
using System.Text;

public class Solution {
    private class Fenwick {
        private readonly int[] bit;
        public Fenwick(int n) { bit = new int[n + 1]; }
        public void Add(int i, int delta) {
            for (i++; i < bit.Length; i += i & -i) bit[i] += delta;
        }
        public int Sum(int i) {
            int outVal = 0;
            while (i > 0) {
                outVal += bit[i];
                i -= i & -i;
            }
            return outVal;
        }
    }

    public string MinInteger(string num, int k) {
        var positions = new Queue<int>[10];
        for (int d = 0; d < 10; d++) positions[d] = new Queue<int>();
        for (int i = 0; i < num.Length; i++) positions[num[i] - '0'].Enqueue(i);
        var fw = new Fenwick(num.Length);
        var sb = new StringBuilder();
        for (int t = 0; t < num.Length; t++) {
            for (int digit = 0; digit < 10; digit++) {
                if (positions[digit].Count == 0) continue;
                int index = positions[digit].Peek();
                int cost = index - fw.Sum(index);
                if (cost <= k) {
                    k -= cost;
                    positions[digit].Dequeue();
                    fw.Add(index, 1);
                    sb.Append((char)('0' + digit));
                    break;
                }
            }
        }
        return sb.ToString();
    }
}

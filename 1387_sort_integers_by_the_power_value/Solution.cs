// LeetCode 1387 - Sort Integers By The Power Value
// https://leetcode.com/problems/sort-integers-by-the-power-value/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    Dictionary<int, int> memo = new Dictionary<int, int>();
    public int GetKth(int lo, int hi, int k) {
        return Enumerable.Range(lo, hi - lo + 1).OrderBy(Power).ThenBy(x => x).ElementAt(k - 1);
    }
    int Power(int x) {
        if (x == 1) return 0;
        if (memo.ContainsKey(x)) return memo[x];
        return memo[x] = 1 + Power(x % 2 == 0 ? x / 2 : 3 * x + 1);
    }
}

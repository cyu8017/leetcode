// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> PowerfulIntegers(int x, int y, int bound) {
        var ans = new HashSet<int>();
        for (long a = 1; a < bound; a *= x) {
            for (long b = 1; a + b <= bound; b *= y) {
                ans.Add((int)(a + b));
                if (y == 1) break;
            }
            if (x == 1) break;
        }
        return ans.ToList();
    }
}

// LeetCode 1387 - Sort Integers By The Power Value
// https://leetcode.com/problems/sort-integers-by-the-power-value/

import java.util.*;

class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();

    public int getKth(int lo, int hi, int k) {
        Integer[] vals = new Integer[hi - lo + 1];
        for (int i = lo; i <= hi; i++) vals[i - lo] = i;
        Arrays.sort(vals, (a, b) -> {
            int pa = power(a), pb = power(b);
            return pa != pb ? Integer.compare(pa, pb) : Integer.compare(a, b);
        });
        return vals[k - 1];
    }

    private int power(int x) {
        if (x == 1) return 0;
        if (memo.containsKey(x)) return memo.get(x);
        int res = 1 + power(x % 2 == 0 ? x / 2 : 3 * x + 1);
        memo.put(x, res);
        return res;
    }
}

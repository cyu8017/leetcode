// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

using System;

public class Solution {
    public int[] SuccessfulPairs(int[] spells, int[] potions, long success) {
        Array.Sort(potions);
        int m = potions.Length;
        int[] ans = new int[spells.Length];
        for (int i = 0; i < spells.Length; i++) {
            int lo = 0, hi = m;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if ((long)spells[i] * potions[mid] >= success) hi = mid;
                else lo = mid + 1;
            }
            ans[i] = m - lo;
        }
        return ans;
    }
}

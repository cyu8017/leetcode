// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

using System.Collections.Generic;

public class Solution {
    public IList<int> AddToArrayForm(int[] num, int k) {
        var list = new List<int>(num);
        int i = list.Count - 1;
        while (k > 0 || i >= 0) {
            if (i >= 0) {
                k += list[i];
                list[i] = k % 10;
                i--;
            } else {
                list.Insert(0, k % 10);
            }
            k /= 10;
        }
        return list;
    }
}

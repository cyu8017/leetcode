// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

import java.util.*;

class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> list = new ArrayList<>();
        for (int x : num) list.add(x);
        int i = list.size() - 1;
        while (k > 0 || i >= 0) {
            if (i >= 0) {
                k += list.get(i);
                list.set(i, k % 10);
                i--;
            } else {
                list.add(0, k % 10);
            }
            k /= 10;
        }
        return list;
    }
}

// LeetCode 1471 - The K Strongest Values In An Array
// https://leetcode.com/problems/the-k-strongest-values-in-an-array/

import java.util.*;

class Solution {
    public int[] getStrongest(int[] arr, int k) {
        Arrays.sort(arr);
        int median = arr[(arr.length - 1) / 2];
        Integer[] boxed = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(boxed, (a, b) -> {
            int da = Math.abs(a - median), db = Math.abs(b - median);
            return da != db ? Integer.compare(db, da) : Integer.compare(b, a);
        });
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) ans[i] = boxed[i];
        return ans;
    }
}

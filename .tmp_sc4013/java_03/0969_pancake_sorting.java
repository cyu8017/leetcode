// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

import java.util.*;

class Solution {
    public List<Integer> pancakeSort(int[] arr) {
        int[] a = arr.clone();
        List<Integer> ans = new ArrayList<>();
        for (int size = a.length; size > 1; size--) {
            int i = indexOf(a, size);
            if (i == size - 1) continue;
            if (i > 0) {
                ans.add(i + 1);
                reverse(a, 0, i);
            }
            ans.add(size);
            reverse(a, 0, size - 1);
        }
        return ans;
    }

    private int indexOf(int[] a, int v) {
        for (int i = 0; i < a.length; i++) if (a[i] == v) return i;
        return -1;
    }

    private void reverse(int[] a, int l, int r) {
        while (l < r) {
            int t = a[l]; a[l] = a[r]; a[r] = t;
            l++; r--;
        }
    }
}

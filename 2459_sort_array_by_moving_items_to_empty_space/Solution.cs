// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

using System;
using System.Collections.Generic;

public class Solution {
    public int SortArray(int[] nums) {
        return Math.Min(SolveOne(nums, true), SolveOne(nums, false));
    }

    private int SolveOne(int[] nums, bool startZero) {
        int n = nums.Length;
        int[] arr = (int[])nums.Clone();
        var pos = new Dictionary<int, int>();
        for (int i = 0; i < n; i++) pos[arr[i]] = i;
        int ops = 0;
        while (true) {
            int empty = pos[0];
            int should = startZero ? empty : (empty == n - 1 ? 0 : empty + 1);
            if (arr[empty] == should) {
                int found = -1;
                for (int i = 0; i < n; i++) {
                    int want = startZero ? i : (i == n - 1 ? 0 : i + 1);
                    if (arr[i] != want) {
                        found = i;
                        break;
                    }
                }
                if (found == -1) return ops;
                int v = arr[found];
                (arr[empty], arr[found]) = (arr[found], arr[empty]);
                pos[0] = found;
                pos[v] = empty;
                ops++;
                continue;
            }
            int j = pos[should];
            int vv = arr[j];
            (arr[empty], arr[j]) = (arr[j], arr[empty]);
            pos[0] = j;
            pos[vv] = empty;
            ops++;
        }
    }
}

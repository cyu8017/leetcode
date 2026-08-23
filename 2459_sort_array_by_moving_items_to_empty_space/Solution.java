// LeetCode 2459 - Sort Array By Moving Items to Empty Space
// https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int sortArray(int[] nums) {
        return Math.min(SolveOne(nums, true), SolveOne(nums, false));
    }

    private int solveOne(int[] nums, boolean startZero) {
        int n = nums.length;
        int[] arr = nums.clone();
        var pos = new HashMap<Integer, Integer>();
        for (int i = 0; i < n; i++) pos.put(arr[i], i);
        int ops = 0;
        while (true) {
            int empty = pos.get(0);
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
                pos.put(0, found);
                pos.put(v, empty);
                ops++;
                continue;
            }
            int j = pos.get(should);
            int vv = arr[j];
            (arr[empty], arr[j]) = (arr[j], arr[empty]);
            pos.put(0, j);
            pos.put(vv, empty);
            ops++;
        }
    }
}

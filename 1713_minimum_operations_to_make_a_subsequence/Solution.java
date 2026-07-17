// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minOperations(int[] target, int[] arr) {
        Map<Integer, Integer> pos = new HashMap<>();
        for (int i = 0; i < target.length; i++) {
            pos.put(target[i], i);
        }
        int[] lis = new int[arr.length];
        int size = 0;
        for (int value : arr) {
            Integer idx = pos.get(value);
            if (idx == null) {
                continue;
            }
            int lo = 0;
            int hi = size;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (lis[mid] < idx) {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            lis[lo] = idx;
            if (lo == size) {
                size++;
            }
        }
        return target.length - size;
    }
}

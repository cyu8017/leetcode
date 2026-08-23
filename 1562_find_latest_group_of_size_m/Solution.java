// LeetCode 1562 - Find Latest Group of Size M
// https://leetcode.com/problems/find-latest-group-of-size-m/

import java.util.*;

class Solution {
    public int findLatestStep(int[] arr, int m) {
        if (m == arr.length) {
            return m;
        }
        Map<Integer, Integer> lengths = new HashMap<>();
        int answer = -1;
        for (int step = 1; step <= arr.length; step++) {
            int x = arr[step - 1];
            int left = lengths.getOrDefault(x - 1, 0);
            int right = lengths.getOrDefault(x + 1, 0);
            int size = left + 1 + right;
            lengths.put(x - left, size);
            lengths.put(x + right, size);
            if (left == m || right == m) {
                answer = step - 1;
            }
        }
        return answer;
    }
}

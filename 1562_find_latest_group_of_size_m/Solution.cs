// LeetCode 1562 - Find Latest Group of Size M
// https://leetcode.com/problems/find-latest-group-of-size-m/

using System.Collections.Generic;

public class Solution {
    public int FindLatestStep(int[] arr, int m) {
        if (m == arr.Length) return m;
        var lengths = new Dictionary<int, int>();
        int answer = -1;
        for (int step = 1; step <= arr.Length; step++) {
            int x = arr[step - 1];
            lengths.TryGetValue(x - 1, out int left);
            lengths.TryGetValue(x + 1, out int right);
            int size = left + 1 + right;
            lengths[x - left] = size;
            lengths[x + right] = size;
            if (left == m || right == m) answer = step - 1;
        }
        return answer;
    }
}

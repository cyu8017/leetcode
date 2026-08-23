// LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

using System.Collections.Generic;

public class Solution {
    public int MinSwaps(int[][] grid) {
        int n = grid.Length;
        var zeros = new List<int>();
        foreach (var row in grid) {
            int count = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (row[j] != 0) break;
                count++;
            }
            zeros.Add(count);
        }
        int answer = 0;
        for (int i = 0; i < n; i++) {
            int required = n - i - 1;
            int j = i;
            while (j < n && zeros[j] < required) j++;
            if (j == n) return -1;
            answer += j - i;
            int val = zeros[j];
            zeros.RemoveAt(j);
            zeros.Insert(i, val);
        }
        return answer;
    }
}

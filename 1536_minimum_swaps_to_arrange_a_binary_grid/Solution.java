// LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

class Solution {
    public int minSwaps(int[][] grid) {
        int n = grid.length;
        int[] zeros = new int[n];
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] != 0) {
                    break;
                }
                count++;
            }
            zeros[i] = count;
        }
        int answer = 0;
        for (int i = 0; i < n; i++) {
            int required = n - i - 1;
            int j = i;
            while (j < n && zeros[j] < required) {
                j++;
            }
            if (j == n) {
                return -1;
            }
            answer += j - i;
            int value = zeros[j];
            for (int row = j; row > i; row--) {
                zeros[row] = zeros[row - 1];
            }
            zeros[i] = value;
        }
        return answer;
    }
}

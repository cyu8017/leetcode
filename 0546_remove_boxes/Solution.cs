// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

public class Solution {
    private int[] boxes;
    private int[,,] memo;

    public int RemoveBoxes(int[] boxes) {
        this.boxes = boxes;
        int n = boxes.Length;
        memo = new int[n, n, n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int s = 0; s < n; s++) {
                    memo[i, j, s] = -1;
                }
            }
        }
        return Dp(0, n - 1, 0);
    }

    private int Dp(int left, int right, int streak) {
        if (left > right) {
            return 0;
        }
        if (memo[left, right, streak] != -1) {
            return memo[left, right, streak];
        }

        while (right > left && boxes[right] == boxes[right - 1]) {
            right--;
            streak++;
        }

        int best = (streak + 1) * (streak + 1) + Dp(left, right - 1, 0);
        for (int i = left; i < right; i++) {
            if (boxes[i] == boxes[right]) {
                best = System.Math.Max(best, Dp(left, i, streak + 1) + Dp(i + 1, right - 1, 0));
            }
        }

        memo[left, right, streak] = best;
        return best;
    }
}

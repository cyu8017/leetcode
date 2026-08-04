// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

class Solution {
    private int best;

    public int tilingRectangle(int n, int m) {
        if (n > m) {
            int t = n;
            n = m;
            m = t;
        }
        int[] heights = new int[m];
        best = n * m;
        search(heights, n, m, 0);
        return best;
    }

    private void search(int[] heights, int n, int m, int used) {
        if (used >= best) return;
        int low = Integer.MAX_VALUE;
        for (int h : heights) low = Math.min(low, h);
        if (low == n) {
            best = used;
            return;
        }
        int left = 0;
        while (left < m && heights[left] != low) left++;
        int right = left;
        while (right < m && heights[right] == low) right++;
        int maxSize = Math.min(n - low, right - left);
        for (int size = maxSize; size >= 1; size--) {
            for (int i = left; i < left + size; i++) heights[i] = low + size;
            search(heights, n, m, used + 1);
            for (int i = left; i < left + size; i++) heights[i] = low;
        }
    }
}


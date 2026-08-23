// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private int lis(List<Integer> a) {
        List<Integer> tails = new ArrayList<>();
        for (int x : a) {
            int lo = 0, hi = tails.size();
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (tails.get(mid) < x) lo = mid + 1;
                else hi = mid;
            }
            if (lo == tails.size()) tails.add(x);
            else tails.set(lo, x);
        }
        return tails.size();
    }

    public int maxPathLength(int[][] coordinates, int k) {
        int n = coordinates.length;
        int[][] arr = new int[n][3];
        for (int i = 0; i < n; i++) {
            arr[i][0] = coordinates[i][0];
            arr[i][1] = coordinates[i][1];
            arr[i][2] = i;
        }
        Arrays.sort(arr, (a, b) -> a[0] == b[0] ? Integer.compare(b[1], a[1]) : Integer.compare(a[0], b[0]));
        int kx = coordinates[k][0], ky = coordinates[k][1];
        List<Integer> left = new ArrayList<>(), right = new ArrayList<>();
        for (int[] p : arr) {
            if (p[0] < kx && p[1] < ky) left.add(p[1]);
            if (p[0] > kx && p[1] > ky) right.add(p[1]);
        }
        return lis(left) + 1 + lis(right);
    }
}

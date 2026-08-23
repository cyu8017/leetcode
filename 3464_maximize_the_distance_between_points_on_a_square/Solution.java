// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

import java.util.Arrays;

class Solution {
    private boolean canPlace(int[] arr, int perim, int k, int mid) {
        int n = arr.length;
        for (int s = 0; s < n; s++) {
            int cnt = 1;
            int last = arr[s];
            int idx = s;
            for (; cnt < k; ) {
                int target = last + mid;
                boolean found = false;
                for (int step = 1; step < n; step++) {
                    int ni = (idx + step) % n;
                    int val = arr[ni];
                    int add = (ni <= idx) ? perim : 0;
                    if (val + add >= target) {
                        last = val + add;
                        idx = ni;
                        cnt++;
                        found = true;
                        break;
                    }
                }
                if (!found) break;
            }
            if (cnt == k && last - arr[s] <= perim - mid) return true;
        }
        return false;
    }

    public int maxDistance(int side, int[][] points, int k) {
        int[] arr = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            int x = points[i][0], y = points[i][1];
            int d;
            if (y == 0) d = x;
            else if (x == side) d = side + y;
            else if (y == side) d = 2 * side + (side - x);
            else d = 3 * side + (side - y);
            arr[i] = d;
        }
        Arrays.sort(arr);
        int perim = 4 * side;
        int lo = 0, hi = 2 * side;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (canPlace(arr, perim, k, mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}

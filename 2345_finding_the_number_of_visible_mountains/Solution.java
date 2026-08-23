// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int visibleMountains(int[][] peaks) {
        List<int[]> arr = new ArrayList<>();
        for (int[] p : peaks) arr.add(new int[] {p[0] - p[1], p[0] + p[1]});
        arr.sort((a, b) -> {
            if (a[0] == b[0]) return Integer.compare(b[1], a[1]);
            return Integer.compare(a[0], b[0]);
        });
        int ans = 0;
        int maxR = Integer.MIN_VALUE;
        for (int i = 0; i < arr.size(); ) {
            int j = i;
            while (j < arr.size() && arr.get(j)[0] == arr.get(i)[0] && arr.get(j)[1] == arr.get(i)[1]) j++;
            if (arr.get(i)[1] > maxR) {
                if (j - i == 1) ans++;
                maxR = arr.get(i)[1];
            }
            i = j;
        }
        return ans;
    }
}

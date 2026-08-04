// LeetCode 1552 - Magnetic Force Between Two Balls
// https://leetcode.com/problems/magnetic-force-between-two-balls/

import java.util.*;

class Solution {
    public int maxDistance(int[] position, int m) {
        Arrays.sort(position);
        int lo = 1, hi = (position[position.length - 1] - position[0]) / (m - 1);
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int count = 1, last = position[0];
            for (int i = 1; i < position.length; i++) {
                if (position[i] - last >= mid) {
                    count++;
                    last = position[i];
                }
            }
            if (count >= m) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return hi;
    }
}

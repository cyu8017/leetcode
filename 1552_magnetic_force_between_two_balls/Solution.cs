// LeetCode 1552 - Magnetic Force Between Two Balls
// https://leetcode.com/problems/magnetic-force-between-two-balls/

using System;

public class Solution {
    public int MaxDistance(int[] position, int m) {
        Array.Sort(position);
        int lo = 1, hi = (position[position.Length - 1] - position[0]) / (m - 1);
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int count = 1, last = position[0];
            for (int i = 1; i < position.Length; i++) {
                if (position[i] - last >= mid) {
                    count++;
                    last = position[i];
                }
            }
            if (count >= m) lo = mid + 1;
            else hi = mid - 1;
        }
        return hi;
    }
}

// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

import java.util.Arrays;

class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(heaters);
        int radius = 0;
        for (int house : houses) {
            int position = Arrays.binarySearch(heaters, house);
            if (position < 0) {
                position = -position - 1;
            }
            int best = Integer.MAX_VALUE;
            if (position < heaters.length) {
                best = Math.min(best, Math.abs(heaters[position] - house));
            }
            if (position > 0) {
                best = Math.min(best, Math.abs(heaters[position - 1] - house));
            }
            radius = Math.max(radius, best);
        }
        return radius;
    }
}

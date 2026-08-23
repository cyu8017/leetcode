// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

import java.util.Arrays;

class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        Arrays.sort(capacity);
        int s = 0;
        for (int x : apple) s += x;
        for (int i = 1; ; i++) {
            s -= capacity[capacity.length - i];
            if (s <= 0) return i;
        }
    }
}

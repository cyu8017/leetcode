// LeetCode 1580 - Put Boxes Into the Warehouse II
// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

import java.util.*;

class Solution {
    public int maxBoxesInWarehouse(int[] boxes, int[] warehouse) {
        int n = warehouse.length;
        int[] left = warehouse.clone();
        int[] right = warehouse.clone();
        for (int i = 1; i < n; i++) {
            left[i] = Math.min(left[i], left[i - 1]);
        }
        for (int i = n - 2; i >= 0; i--) {
            right[i] = Math.min(right[i], right[i + 1]);
        }
        int[] capacity = new int[n];
        for (int i = 0; i < n; i++) {
            capacity[i] = Math.max(left[i], right[i]);
        }
        Arrays.sort(capacity);
        Arrays.sort(boxes);
        int i = 0;
        for (int room : capacity) {
            if (i < boxes.length && boxes[i] <= room) {
                i++;
            }
        }
        return i;
    }
}

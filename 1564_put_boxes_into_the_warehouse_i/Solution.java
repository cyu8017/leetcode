// LeetCode 1564 - Put Boxes Into the Warehouse I
// https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

import java.util.*;

class Solution {
    public int maxBoxesInWarehouse(int[] boxes, int[] warehouse) {
        for (int i = 1; i < warehouse.length; i++) {
            warehouse[i] = Math.min(warehouse[i], warehouse[i - 1]);
        }
        Arrays.sort(boxes);
        int room = warehouse.length - 1;
        int used = 0;
        for (int box : boxes) {
            while (room >= 0 && warehouse[room] < box) {
                room--;
            }
            if (room < 0) {
                break;
            }
            used++;
            room--;
        }
        return used;
    }
}

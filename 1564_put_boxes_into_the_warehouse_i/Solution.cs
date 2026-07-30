// LeetCode 1564 - Put Boxes Into the Warehouse I
// https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

using System;

public class Solution {
    public int MaxBoxesInWarehouse(int[] boxes, int[] warehouse) {
        for (int i = 1; i < warehouse.Length; i++)
            warehouse[i] = Math.Min(warehouse[i], warehouse[i - 1]);
        Array.Sort(boxes);
        int room = warehouse.Length - 1, used = 0;
        foreach (int box in boxes) {
            while (room >= 0 && warehouse[room] < box) room--;
            if (room < 0) break;
            used++;
            room--;
        }
        return used;
    }
}

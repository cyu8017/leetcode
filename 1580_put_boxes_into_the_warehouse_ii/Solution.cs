// LeetCode 1580 - Put Boxes Into the Warehouse II
// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

using System;
using System.Linq;

public class Solution {
    public int MaxBoxesInWarehouse(int[] boxes, int[] warehouse) {
        int n = warehouse.Length;
        int[] left = (int[])warehouse.Clone();
        int[] right = (int[])warehouse.Clone();
        for (int i = 1; i < n; i++) left[i] = Math.Min(left[i], left[i - 1]);
        for (int i = n - 2; i >= 0; i--) right[i] = Math.Min(right[i], right[i + 1]);
        int[] capacity = new int[n];
        for (int i = 0; i < n; i++) capacity[i] = Math.Max(left[i], right[i]);
        Array.Sort(capacity);
        Array.Sort(boxes);
        int idx = 0;
        foreach (int room in capacity) {
            if (idx < boxes.Length && boxes[idx] <= room) idx++;
        }
        return idx;
    }
}

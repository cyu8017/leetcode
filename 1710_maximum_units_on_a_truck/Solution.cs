// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/

public class Solution {
    public int MaximumUnits(int[][] boxTypes, int truckSize) {
        Array.Sort(boxTypes, (a, b) => b[1].CompareTo(a[1]));
        int total = 0;
        foreach (int[] box in boxTypes) {
            int take = Math.Min(box[0], truckSize);
            total += take * box[1];
            truckSize -= take;
            if (truckSize == 0) {
                break;
            }
        }
        return total;
    }
}

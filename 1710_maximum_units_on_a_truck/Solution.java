// LeetCode 1710 - Maximum Units on a Truck
// https://leetcode.com/problems/maximum-units-on-a-truck/

import java.util.Arrays;

class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a, b) -> Integer.compare(b[1], a[1]));
        int total = 0;
        for (int[] box : boxTypes) {
            int take = Math.min(box[0], truckSize);
            total += take * box[1];
            truckSize -= take;
            if (truckSize == 0) {
                break;
            }
        }
        return total;
    }
}

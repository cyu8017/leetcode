// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        int total = 0;
        for (int x : arr) total += x;
        if (total % 3 != 0) return false;
        int target = total / 3, parts = 0, cur = 0;
        for (int x : arr) {
            cur += x;
            if (cur == target) {
                parts++;
                cur = 0;
            }
        }
        return parts >= 3;
    }
}

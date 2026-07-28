// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

using System.Linq;

public class Solution {
    public bool CanThreePartsEqualSum(int[] arr) {
        int total = arr.Sum();
        if (total % 3 != 0) return false;
        int target = total / 3, parts = 0, cur = 0;
        foreach (int x in arr) {
            cur += x;
            if (cur == target) {
                parts++;
                cur = 0;
            }
        }
        return parts >= 3;
    }
}

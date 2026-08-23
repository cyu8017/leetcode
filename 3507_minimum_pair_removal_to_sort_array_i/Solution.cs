// LeetCode 3507 - Minimum Pair Removal to Sort Array I
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

using System.Collections.Generic;

public class Solution {
    bool IsNonDecreasing(List<int> a) {
        for (int i = 1; i < a.Count; i++) if (a[i] < a[i - 1]) return false;
        return true;
    }
    public int MinimumPairRemoval(int[] nums) {
        var arr = new List<int>(nums);
        int ans = 0;
        while (!IsNonDecreasing(arr)) {
            int k = 0, s = arr[0] + arr[1];
            for (int i = 1; i + 1 < arr.Count; i++) {
                int t = arr[i] + arr[i + 1];
                if (s > t) { s = t; k = i; }
            }
            arr[k] = s;
            arr.RemoveAt(k + 1);
            ans++;
        }
        return ans;
    }
}

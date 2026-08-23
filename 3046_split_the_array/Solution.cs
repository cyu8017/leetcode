// LeetCode 3046 - Split the Array
// https://leetcode.com/problems/split-the-array/

public class Solution {
    public bool IsPossibleToSplit(int[] nums) {
        int[] cnt = new int[101];
        foreach (int x in nums) {
            cnt[x]++;
            if (cnt[x] >= 3) return false;
        }
        return true;
    }
}

// LeetCode 1186 - Maximum Subarray Sum with One Deletion
// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution {
    public int maximumSum(int[] arr) {
        int keep = arr[0], delete = arr[0], ans = arr[0];
        for (int i = 1; i < arr.length; i++) {
            int x = arr[i];
            delete = Math.max(keep, delete + x);
            keep = Math.max(keep + x, x);
            ans = Math.max(ans, Math.max(keep, delete));
        }
        return ans;
    }
}

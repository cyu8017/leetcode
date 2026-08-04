// LeetCode 1477 - Find Two Non Overlapping Sub Arrays Each With Target Sum
// https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int inf = 1000000000, left = 0, total = 0, best = inf, ans = inf;
        var shortest = new int[arr.length];
        for (int right = 0; right < arr.length; right++) {
            total += arr[right];
            while (total > target) total -= arr[left++];
            if (total == target) {
                int length = right - left + 1;
                if (left > 0) ans = Math.min(ans, length + shortest[left - 1]);
                best = Math.min(best, length);
            }
            shortest[right] = best;
        }
        return ans == inf ? -1 : ans;
    }
}

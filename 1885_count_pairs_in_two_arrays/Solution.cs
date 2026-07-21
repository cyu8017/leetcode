// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

public class Solution {
    public long CountPairs(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        var diff = new int[n];
        for (int i = 0; i < n; i++) {
            diff[i] = nums1[i] - nums2[i];
        }
        Array.Sort(diff);
        long answer = 0;
        for (int i = 0; i < n; i++) {
            int target = -diff[i];
            int lo = i + 1;
            int hi = n;
            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;
                if (diff[mid] <= target) {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            answer += n - lo;
        }
        return answer;
    }
}

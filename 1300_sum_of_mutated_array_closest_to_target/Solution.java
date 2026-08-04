// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

class Solution {
    public int findBestValue(int[] arr, int target) {
        int lo = 0, hi = 0;
        for (int x : arr) hi = Math.max(hi, x);
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            long sum = 0;
            for (int x : arr) sum += Math.min(x, mid);
            if (sum < target) lo = mid + 1;
            else hi = mid;
        }
        long before = 0, after = 0;
        for (int x : arr) {
            before += Math.min(x, lo - 1);
            after += Math.min(x, lo);
        }
        return target - before <= after - target ? lo - 1 : lo;
    }
}

// LeetCode 1300 - Sum Of Mutated Array Closest To Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

public class Solution {
    public int FindBestValue(int[] arr, int target) {
        int lo = 0, hi = 0;
        foreach (int x in arr) hi = System.Math.Max(hi, x);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            long sum = 0;
            foreach (int x in arr) sum += System.Math.Min(x, mid);
            if (sum < target) lo = mid + 1;
            else hi = mid;
        }
        long Before(int v) {
            long s = 0;
            foreach (int x in arr) s += System.Math.Min(x, v);
            return s;
        }
        long before = Before(lo - 1), after = Before(lo);
        return target - before <= after - target ? lo - 1 : lo;
    }
}

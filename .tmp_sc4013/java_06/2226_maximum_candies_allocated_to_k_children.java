// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution {
    public int maximumCandies(int[] candies, long k) {
        int mx = 0;
        for (int c : candies) mx = Math.max(mx, c);
        int lo = 0, hi = mx;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (can(candies, k, mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }

    private boolean can(int[] candies, long k, int mid) {
        if (mid == 0) return true;
        long cnt = 0;
        for (int c : candies) {
            cnt += c / mid;
            if (cnt >= k) return true;
        }
        return false;
    }
}

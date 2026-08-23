// LeetCode 0278 - First Bad Version
// https://leetcode.com/problems/first-bad-version/

public class Solution {
    protected bool IsBadVersion(int version) {
        return false;
    }

    public int FirstBadVersion(int n) {
        int left = 1;
        int right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (IsBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}

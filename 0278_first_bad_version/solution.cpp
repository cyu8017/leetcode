// LeetCode 0278 - First Bad Version
// https://leetcode.com/problems/first-bad-version/

bool isBadVersion(int version) {
    return false;
}

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};

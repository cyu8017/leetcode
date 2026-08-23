// LeetCode 3782 - Last Remaining Integer After Alternating Deletion Operations
// https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/

class Solution {
    public long lastRemaining(long n) {
        long first = 1, step = 2;
        boolean left = true;
        while (n > 1) {
            if (!left && n % 2 == 0) first += step;
            n = (n + 1) / 2;
            step *= 2;
            left = !left;
        }
        return first;
    }
}

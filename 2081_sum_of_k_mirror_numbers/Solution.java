// LeetCode 2081 - Sum of k-Mirror Numbers
// https://leetcode.com/problems/sum-of-k-mirror-numbers/

import java.util.*;

class Solution {
    public long kMirror(int k, int n) {
        long ans = 0;
        int count = 0;
        for (int length = 1; count < n; length++) {
            int start = 1;
            for (int i = 1; i < (length + 1) / 2; i++) start *= 10;
            int end = start * 10;
            for (int half = start; half < end && count < n; half++) {
                long pal = half;
                if (length % 2 == 0) {
                    int x = half;
                    while (x > 0) { pal = pal * 10 + x % 10; x /= 10; }
                } else {
                    int x = half / 10;
                    while (x > 0) { pal = pal * 10 + x % 10; x /= 10; }
                }
                if (isPalBase(pal, k)) { ans += pal; count++; }
            }
        }
        return ans;
    }

    private boolean isPalBase(long x, int bas) {
        List<Integer> digits = new ArrayList<>();
        while (x > 0) { digits.add((int) (x % bas)); x /= bas; }
        for (int l = 0, r = digits.size() - 1; l < r; l++, r--)
            if (!digits.get(l).equals(digits.get(r))) return false;
        return true;
    }
}

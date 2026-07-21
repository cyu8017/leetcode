// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

public class Solution {
    public int MaxLength(int[] ribbons, int k) {
        bool Can(int length) {
            long total = 0;
            foreach (int ribbon in ribbons) {
                total += ribbon / length;
                if (total >= k) {
                    return true;
                }
            }
            return total >= k;
        }

        int lo = 1;
        int hi = 0;
        foreach (int ribbon in ribbons) {
            hi = Math.Max(hi, ribbon);
        }
        while (lo < hi) {
            int mid = lo + (hi - lo + 1) / 2;
            if (Can(mid)) {
                lo = mid;
            } else {
                hi = mid - 1;
            }
        }
        return Can(lo) ? lo : 0;
    }
}

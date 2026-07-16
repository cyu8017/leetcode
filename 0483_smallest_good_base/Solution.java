// LeetCode 0483 - Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/

class Solution {
    public String smallestGoodBase(String n) {
        long num = Long.parseLong(n);
        for (int length = (int) (Math.log(num) / Math.log(2)) + 1; length > 1; length--) {
            long low = 2;
            long high = num - 1;
            while (low <= high) {
                long mid = low + (high - low) / 2;
                long total = 1;
                long power = 1;
                boolean ok = true;
                for (int i = 1; i < length; i++) {
                    if (power > (Long.MAX_VALUE / mid)) {
                        ok = false;
                        break;
                    }
                    power *= mid;
                    total += power;
                    if (total > num) {
                        ok = false;
                        break;
                    }
                }
                if (ok && total == num) {
                    return Long.toString(mid);
                }
                if (!ok || total > num) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
        }
        return Long.toString(num - 1);
    }
}

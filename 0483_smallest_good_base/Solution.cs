// LeetCode 0483 - Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/

public class Solution {
    public string SmallestGoodBase(string n) {
        long num = long.Parse(n);
        for (int length = (int)Math.Log(num, 2) + 1; length > 1; length--) {
            long low = 2;
            long high = num - 1;
            while (low <= high) {
                long mid = low + (high - low) / 2;
                long total = 1;
                long power = 1;
                bool ok = true;
                for (int i = 1; i < length; i++) {
                    if (power > long.MaxValue / mid) {
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
                    return mid.ToString();
                }
                if (!ok || total > num) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
        }
        return (num - 1).ToString();
    }
}

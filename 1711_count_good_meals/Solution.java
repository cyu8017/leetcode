// LeetCode 1711 - Count Good Meals
// https://leetcode.com/problems/count-good-meals/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countPairs(int[] deliciousness) {
        final long mod = 1_000_000_007L;
        Map<Integer, Long> seen = new HashMap<>();
        long ans = 0;
        for (int value : deliciousness) {
            for (int power = 0; power < 22; power++) {
                Long count = seen.get((1 << power) - value);
                if (count != null) {
                    ans += count;
                }
            }
            seen.merge(value, 1L, Long::sum);
        }
        return (int) (ans % mod);
    }
}

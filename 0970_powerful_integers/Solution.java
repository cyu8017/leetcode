// LeetCode 0970 - Powerful Integers
// https://leetcode.com/problems/powerful-integers/

import java.util.*;

class Solution {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        Set<Integer> ans = new HashSet<>();
        for (long a = 1; a < bound; a *= x) {
            for (long b = 1; a + b <= bound; b *= y) {
                ans.add((int) (a + b));
                if (y == 1) break;
            }
            if (x == 1) break;
        }
        return new ArrayList<>(ans);
    }
}

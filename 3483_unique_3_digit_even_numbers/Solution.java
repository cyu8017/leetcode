// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int totalNumbers(int[] digits) {
        Set<Integer> seen = new HashSet<>();
        int n = digits.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                for (int k = 0; k < n; k++) {
                    if (k == i || k == j) continue;
                    if (digits[i] == 0) continue;
                    if (digits[k] % 2 != 0) continue;
                    seen.add(digits[i] * 100 + digits[j] * 10 + digits[k]);
                }
            }
        }
        return seen.size();
    }
}

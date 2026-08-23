// LeetCode 1447 - Simplified Fractions
// https://leetcode.com/problems/simplified-fractions/

import java.util.*;

class Solution {
    public List<String> simplifiedFractions(int n) {
        List<String> answer = new ArrayList<>();
        for (int den = 2; den <= n; den++) {
            for (int num = 1; num < den; num++) {
                if (gcd(num, den) == 1) answer.add(num + "/" + den);
            }
        }
        return answer;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}

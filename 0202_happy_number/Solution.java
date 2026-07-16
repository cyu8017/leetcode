// LeetCode 0202 - Happy Number\n// https://leetcode.com/problems/\n\nimport java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        while (n != 1 && seen.add(n)) n = nextValue(n);
        return n == 1;
    }

    private int nextValue(int value) {
        int total = 0;
        while (value > 0) {
            int digit = value % 10;
            total += digit * digit;
            value /= 10;
        }
        return total;
    }
}

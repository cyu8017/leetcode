// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

class Solution {
    public boolean confusingNumber(int n) {
        int[] rotate = new int[10];
        for (int i = 0; i < 10; i++) {
            rotate[i] = -1;
        }
        rotate[0] = 0;
        rotate[1] = 1;
        rotate[6] = 9;
        rotate[8] = 8;
        rotate[9] = 6;
        String s = String.valueOf(n);
        StringBuilder rotated = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            int d = s.charAt(i) - '0';
            if (rotate[d] < 0) {
                return false;
            }
            rotated.append(rotate[d]);
        }
        return !rotated.toString().equals(s);
    }
}

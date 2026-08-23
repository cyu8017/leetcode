// LeetCode 1363 - Largest Multiple Of Three
// https://leetcode.com/problems/largest-multiple-of-three/

class Solution {
    public String largestMultipleOfThree(int[] digits) {
        int[] cnt = new int[10];
        int sum = 0;
        for (int d : digits) {
            cnt[d]++;
            sum += d;
        }
        int rem = sum % 3;
        if (rem != 0 && !remove(cnt, rem, 1)) remove(cnt, 3 - rem, 2);
        StringBuilder sb = new StringBuilder();
        for (int d = 9; d >= 0; d--) {
            for (int i = 0; i < cnt[d]; i++) sb.append(d);
        }
        String s = sb.toString();
        if (!s.isEmpty() && s.charAt(0) == '0') return "0";
        return s;
    }

    private boolean remove(int[] cnt, int r, int k) {
        for (int d = r; d < 10; d += 3) {
            while (cnt[d] > 0 && k > 0) {
                cnt[d]--;
                k--;
            }
            if (k == 0) return true;
        }
        return false;
    }
}

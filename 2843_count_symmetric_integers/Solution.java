// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int ans = 0;
        for (int x = low; x <= high; x++) {
            String s = Integer.toString(x);
            if (s.length() % 2 != 0) continue;
            int mid = s.length() / 2, a = 0, b = 0;
            for (int i = 0; i < mid; i++) {
                a += s.charAt(i) - '0';
                b += s.charAt(mid + i) - '0';
            }
            if (a == b) ans++;
        }
        return ans;
    }
}

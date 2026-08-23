// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

import java.util.Arrays;

class Solution {
    public boolean isDigitorialPermutation(int n) {
        int[] f = new int[10];
        f[0] = 1;
        for (int i = 1; i < 10; i++) f[i] = f[i - 1] * i;
        int x = 0, y = n;
        while (y > 0) {
            x += f[y % 10];
            y /= 10;
        }
        char[] a = String.valueOf(x).toCharArray();
        char[] b = String.valueOf(n).toCharArray();
        Arrays.sort(a);
        Arrays.sort(b);
        return new String(a).equals(new String(b));
    }
}

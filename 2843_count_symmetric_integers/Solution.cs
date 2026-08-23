// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

public class Solution {
    public int CountSymmetricIntegers(int low, int high) {
        int ans = 0;
        for (int x = low; x <= high; x++) {
            string s = x.ToString();
            if (s.Length % 2 != 0) continue;
            int mid = s.Length / 2, a = 0, b = 0;
            for (int i = 0; i < mid; i++) {
                a += s[i] - '0';
                b += s[mid + i] - '0';
            }
            if (a == b) ans++;
        }
        return ans;
    }
}

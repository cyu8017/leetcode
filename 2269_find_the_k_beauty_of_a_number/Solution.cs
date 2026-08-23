// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

public class Solution {
    public int DivisorSubstrings(int num, int k) {
        string s = num.ToString();
        int ans = 0;
        for (int i = 0; i + k <= s.Length; i++) {
            int sub = 0;
            for (int j = 0; j < k; j++) sub = sub * 10 + (s[i + j] - '0');
            if (sub != 0 && num % sub == 0) ans++;
        }
        return ans;
    }
}

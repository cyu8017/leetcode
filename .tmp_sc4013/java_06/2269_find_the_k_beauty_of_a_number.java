// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution {
    public int divisorSubstrings(int num, int k) {
        String s = Integer.toString(num);
        int ans = 0;
        for (int i = 0; i + k <= s.length(); i++) {
            int sub = 0;
            for (int j = 0; j < k; j++) sub = sub * 10 + (s.charAt(i + j) - '0');
            if (sub != 0 && num % sub == 0) ans++;
        }
        return ans;
    }
}

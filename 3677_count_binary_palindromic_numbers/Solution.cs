// LeetCode 3677 - Count Binary Palindromic Numbers
// https://leetcode.com/problems/count-binary-palindromic-numbers/

using System.Text;

public class Solution {
    public int CountBinaryPalindromes(long n) {
        if (n == 0) return 1;
        int ans = 1;
        var sb = new StringBuilder();
        {
            long x = n;
            while (x > 0) {
                sb.Append((char)('0' + (x & 1)));
                x >>= 1;
            }
            char[] arr = sb.ToString().ToCharArray();
            System.Array.Reverse(arr);
            sb.Clear();
            sb.Append(arr);
        }
        string s = sb.ToString();
        int L = s.Length;
        for (int len_ = 1; len_ < L; len_++) {
            int half = (len_ + 1) / 2;
            ans += 1 << (half - 1);
        }
        int halfLen = (L + 1) / 2;
        string prefix = s.Substring(0, halfLen);
        int start = 1 << (halfLen - 1);
        long prefVal = 0;
        foreach (char c in prefix) prefVal = (prefVal << 1) | (c - '0');
        ans += (int)prefVal - start;
        var pal = new StringBuilder(prefix);
        for (int i = halfLen - 1 - (L % 2); i >= 0; i--) pal.Append(prefix[i]);
        long pval = 0;
        foreach (char c in pal.ToString()) pval = (pval << 1) | (c - '0');
        if (pval <= n) ans++;
        return ans;
    }
}

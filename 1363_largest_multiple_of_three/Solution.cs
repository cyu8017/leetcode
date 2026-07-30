// LeetCode 1363 - Largest Multiple Of Three
// https://leetcode.com/problems/largest-multiple-of-three/

using System.Text;
public class Solution {
    public string LargestMultipleOfThree(int[] digits) {
        var cnt = new int[10]; int sum = 0;
        foreach (int d in digits) { cnt[d]++; sum += d; }
        int rem = sum % 3;
        bool Remove(int r, int k) {
            for (int d = r; d < 10; d += 3)
                while (cnt[d] > 0 && k > 0) { cnt[d]--; k--; }
            return k == 0;
        }
        if (rem != 0 && !Remove(rem, 1)) Remove(3 - rem, 2);
        var sb = new StringBuilder();
        for (int d = 9; d >= 0; d--) sb.Append(new string((char)('0' + d), cnt[d]));
        string s = sb.ToString();
        return s.Length > 0 && s[0] == '0' ? "0" : s;
    }
}

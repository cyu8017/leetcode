// LeetCode 3309 - Maximum Possible Number by Binary Concatenation
// https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

using System.Text;

public class Solution {
    string ToBin(int x) {
        if (x == 0) return "0";
        var sb = new StringBuilder();
        while (x > 0) {
            sb.Insert(0, (char)('0' + (x & 1)));
            x >>= 1;
        }
        return sb.ToString();
    }

    public int MaxGoodNumber(int[] nums) {
        string[] bs = new string[3];
        for (int i = 0; i < 3; i++) bs[i] = ToBin(nums[i]);
        int[] idx = new int[] { 0, 1, 2 };
        int ans = 0;
        void Perm(int i) {
            if (i == 3) {
                string s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]];
                int v = 0;
                foreach (char c in s) v = v * 2 + (c - '0');
                if (v > ans) ans = v;
                return;
            }
            for (int j = i; j < 3; j++) {
                int t = idx[i]; idx[i] = idx[j]; idx[j] = t;
                Perm(i + 1);
                t = idx[i]; idx[i] = idx[j]; idx[j] = t;
            }
        }
        Perm(0);
        return ans;
    }
}

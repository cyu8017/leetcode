// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

using System;
using System.Collections.Generic;
using System.Text;

public class Solution {
    static List<int> pals;
    static bool inited;

    static bool IsPalindrome(string s) {
        int m = s.Length;
        for (int i = 0; i < m / 2; i++) if (s[i] != s[m - 1 - i]) return false;
        return true;
    }

    static List<int> GetPals() {
        if (!inited) {
            pals = new List<int>();
            int N = 1 << 14;
            for (int i = 0; i < N; i++) {
                string s;
                int x = i;
                if (x == 0) s = "0";
                else {
                    var sb = new StringBuilder();
                    while (x > 0) {
                        sb.Append((char)('0' + (x & 1)));
                        x >>= 1;
                    }
                    char[] arr = sb.ToString().ToCharArray();
                    Array.Reverse(arr);
                    s = new string(arr);
                }
                if (IsPalindrome(s)) pals.Add(i);
            }
            inited = true;
        }
        return pals;
    }

    public int[] MinOperations(int[] nums) {
        var p = GetPals();
        int[] ans = new int[nums.Length];
        for (int k = 0; k < nums.Length; k++) {
            int x = nums[k];
            int it = LowerBound(p, x);
            int t = int.MaxValue;
            if (it < p.Count) t = p[it] - x;
            if (it > 0) t = Math.Min(t, x - p[it - 1]);
            ans[k] = t;
        }
        return ans;
    }

    static int LowerBound(List<int> a, int x) {
        int lo = 0, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}

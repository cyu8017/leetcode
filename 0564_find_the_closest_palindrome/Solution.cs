// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

using System.Collections.Generic;

public class Solution {
    public string NearestPalindromic(string n) {
        int length = n.Length;
        long number = long.Parse(n);
        var candidates = new List<long>();
        candidates.Add(Pow10(length - 1) - 1);
        candidates.Add(Pow10(length) + 1);

        long prefix = long.Parse(n.Substring(0, (length + 1) / 2));
        for (long half = prefix - 1; half <= prefix + 1; ++half) {
            candidates.Add(MakePalindrome(half, length));
        }

        long best = -1;
        long bestDiff = long.MaxValue;
        foreach (long candidate in candidates) {
            if (candidate == number) continue;
            long diff = System.Math.Abs(candidate - number);
            if (diff < bestDiff || (diff == bestDiff && candidate < best)) {
                best = candidate;
                bestDiff = diff;
            }
        }
        return best.ToString();
    }

    private long MakePalindrome(long half, int length) {
        string text = half.ToString();
        var pal = new System.Text.StringBuilder(text);
        if (length % 2 == 0) {
            for (int i = text.Length - 1; i >= 0; --i) pal.Append(text[i]);
        } else {
            for (int i = text.Length - 2; i >= 0; --i) pal.Append(text[i]);
        }
        return long.Parse(pal.ToString());
    }

    private long Pow10(int exp) {
        long value = 1;
        for (int i = 0; i < exp; ++i) value *= 10;
        return value;
    }
}

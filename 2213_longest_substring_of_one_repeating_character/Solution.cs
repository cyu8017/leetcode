// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

using System;

public class Solution {
    struct Seg {
        public char LChar, RChar;
        public int LLen, RLen, Best, Size;
    }

    static Seg Merge(Seg a, Seg b) {
        if (a.Size == 0) return b;
        if (b.Size == 0) return a;
        Seg res = new Seg();
        res.LChar = a.LChar; res.RChar = b.RChar;
        res.Size = a.Size + b.Size;
        res.Best = Math.Max(a.Best, b.Best);
        res.LLen = a.LLen; res.RLen = b.RLen;
        if (a.RChar == b.LChar) {
            int mid = a.RLen + b.LLen;
            res.Best = Math.Max(res.Best, mid);
            if (a.LLen == a.Size) res.LLen = a.Size + b.LLen;
            if (b.RLen == b.Size) res.RLen = b.Size + a.RLen;
        }
        return res;
    }

    Seg[] tree;
    char[] s;
    int n;

    void Build(int idx, int l, int r) {
        if (l == r) {
            tree[idx] = new Seg { LChar = s[l], RChar = s[l], LLen = 1, RLen = 1, Best = 1, Size = 1 };
            return;
        }
        int mid = (l + r) / 2;
        Build(idx * 2, l, mid);
        Build(idx * 2 + 1, mid + 1, r);
        tree[idx] = Merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    void Update(int idx, int l, int r, int pos, char ch) {
        if (l == r) {
            s[pos] = ch;
            tree[idx] = new Seg { LChar = ch, RChar = ch, LLen = 1, RLen = 1, Best = 1, Size = 1 };
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) Update(idx * 2, l, mid, pos, ch);
        else Update(idx * 2 + 1, mid + 1, r, pos, ch);
        tree[idx] = Merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    public int[] LongestRepeating(string s_, string queryCharacters, int[] queryIndices) {
        s = s_.ToCharArray();
        n = s.Length;
        tree = new Seg[4 * n + 5];
        Build(1, 0, n - 1);
        int[] ans = new int[queryIndices.Length];
        for (int i = 0; i < queryIndices.Length; i++) {
            Update(1, 0, n - 1, queryIndices[i], queryCharacters[i]);
            ans[i] = tree[1].Best;
        }
        return ans;
    }
}

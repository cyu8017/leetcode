// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

class Solution {
    private static class Seg {
        char lChar, rChar;
        int lLen, rLen, best, size;
    }

    private static Seg merge(Seg a, Seg b) {
        if (a.size == 0) return b;
        if (b.size == 0) return a;
        Seg res = new Seg();
        res.lChar = a.lChar;
        res.rChar = b.rChar;
        res.size = a.size + b.size;
        res.best = Math.max(a.best, b.best);
        res.lLen = a.lLen;
        res.rLen = b.rLen;
        if (a.rChar == b.lChar) {
            int mid = a.rLen + b.lLen;
            res.best = Math.max(res.best, mid);
            if (a.lLen == a.size) res.lLen = a.size + b.lLen;
            if (b.rLen == b.size) res.rLen = b.size + a.rLen;
        }
        return res;
    }

    private Seg[] tree;
    private char[] s;
    private int n;

    private void build(int idx, int l, int r) {
        if (l == r) {
            tree[idx] = new Seg();
            tree[idx].lChar = tree[idx].rChar = s[l];
            tree[idx].lLen = tree[idx].rLen = tree[idx].best = tree[idx].size = 1;
            return;
        }
        int mid = (l + r) / 2;
        build(idx * 2, l, mid);
        build(idx * 2 + 1, mid + 1, r);
        tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    private void update(int idx, int l, int r, int pos, char ch) {
        if (l == r) {
            s[pos] = ch;
            tree[idx] = new Seg();
            tree[idx].lChar = tree[idx].rChar = ch;
            tree[idx].lLen = tree[idx].rLen = tree[idx].best = tree[idx].size = 1;
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) update(idx * 2, l, mid, pos, ch);
        else update(idx * 2 + 1, mid + 1, r, pos, ch);
        tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
    }

    public int[] longestRepeating(String s_, String queryCharacters, int[] queryIndices) {
        s = s_.toCharArray();
        n = s.length;
        tree = new Seg[4 * n + 5];
        build(1, 0, n - 1);
        int[] ans = new int[queryIndices.length];
        for (int i = 0; i < queryIndices.length; i++) {
            update(1, 0, n - 1, queryIndices[i], queryCharacters.charAt(i));
            ans[i] = tree[1].best;
        }
        return ans;
    }
}

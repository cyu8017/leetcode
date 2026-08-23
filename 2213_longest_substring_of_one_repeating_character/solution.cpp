// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

class Solution {
    struct Seg {
        char lChar = 0, rChar = 0;
        int lLen = 0, rLen = 0, best = 0, size = 0;
    };
    static Seg merge(const Seg& a, const Seg& b) {
        if (a.size == 0) return b;
        if (b.size == 0) return a;
        Seg res;
        res.lChar = a.lChar; res.rChar = b.rChar;
        res.size = a.size + b.size;
        res.best = max(a.best, b.best);
        res.lLen = a.lLen; res.rLen = b.rLen;
        if (a.rChar == b.lChar) {
            int mid = a.rLen + b.lLen;
            res.best = max(res.best, mid);
            if (a.lLen == a.size) res.lLen = a.size + b.lLen;
            if (b.rLen == b.size) res.rLen = b.size + a.rLen;
        }
        return res;
    }
    vector<Seg> tree;
    string s;
    int n;
    void build(int idx, int l, int r) {
        if (l == r) {
            tree[idx] = {s[l], s[l], 1, 1, 1, 1};
            return;
        }
        int mid = (l + r) / 2;
        build(idx * 2, l, mid);
        build(idx * 2 + 1, mid + 1, r);
        tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
    }
    void update(int idx, int l, int r, int pos, char ch) {
        if (l == r) {
            s[pos] = ch;
            tree[idx] = {ch, ch, 1, 1, 1, 1};
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) update(idx * 2, l, mid, pos, ch);
        else update(idx * 2 + 1, mid + 1, r, pos, ch);
        tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
    }
public:
    vector<int> longestRepeating(string s_, string queryCharacters, vector<int>& queryIndices) {
        s = s_; n = s.size();
        tree.assign(4 * n + 5, {});
        build(1, 0, n - 1);
        vector<int> ans(queryIndices.size());
        for (int i = 0; i < (int)queryIndices.size(); i++) {
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i]);
            ans[i] = tree[1].best;
        }
        return ans;
    }
};

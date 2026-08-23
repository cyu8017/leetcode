// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

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
public:
    string longestSubsequenceRepeatedK(string s, int k) {
        int freq[26] = {};
        for (char c : s) freq[c - 'a']++;
        string chars;
        for (int c = 25; c >= 0; c--) if (freq[c] >= k) chars.push_back('a' + c);
        auto isSubseq = [&](const string& t) {
            int need = 0, times = 0;
            for (char c : s) {
                if (c == t[need]) {
                    need++;
                    if (need == (int)t.size()) {
                        times++;
                        if (times == k) return true;
                        need = 0;
                    }
                }
            }
            return false;
        };
        string best;
        queue<string> q;
        q.push("");
        while (!q.empty()) {
            string cur = q.front(); q.pop();
            for (char ch : chars) {
                string nxt = cur + ch;
                if (isSubseq(nxt)) {
                    if (nxt.size() > best.size() || (nxt.size() == best.size() && nxt > best)) best = nxt;
                    q.push(nxt);
                }
            }
        }
        return best;
    }
};

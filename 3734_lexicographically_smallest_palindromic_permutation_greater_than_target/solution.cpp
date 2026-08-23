// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::string lexPalindromicPermutation(std::string s, std::string target) {
        int cnt[26] = {};
        for (char c : s) cnt[c - 'a']++;
        int odd = 0, mid = -1;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] % 2 == 1) { odd++; mid = i; }
        }
        if (odd > 1) return "";
        int half[26] = {};
        for (int i = 0; i < 26; i++) half[i] = cnt[i] / 2;
        int n = (int)s.size();
        int halfLen = n / 2;
        std::string left(halfLen, ' ');
        std::function<bool(int, bool)> dfs = [&](int pos, bool greater) -> bool {
            if (pos == halfLen) {
                if (mid >= 0) {
                    if (greater) return true;
                    return char('a' + mid) > target[halfLen];
                }
                return greater;
            }
            int start = greater ? 0 : (target[pos] - 'a');
            for (int c = start; c < 26; c++) {
                if (half[c] == 0) continue;
                half[c]--;
                left[pos] = char('a' + c);
                if (dfs(pos + 1, greater || c > (target[pos] - 'a'))) return true;
                half[c]++;
            }
            return false;
        };
        if (!dfs(0, false)) return "";
        std::string res = left;
        if (mid >= 0) res.push_back(char('a' + mid));
        for (int i = halfLen - 1; i >= 0; i--) res.push_back(left[i]);
        if (res <= target) return "";
        return res;
    }
};

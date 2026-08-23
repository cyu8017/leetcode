// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

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
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> freq;
        for (auto& w : words) freq[w]++;
        int ans = 0;
        bool center = false;
        for (auto& [w, c] : freq) {
            string rev = string{w[1], w[0]};
            if (w[0] == w[1]) {
                ans += (c / 2) * 4;
                if (c % 2) center = true;
            } else if (w < rev) {
                ans += min(c, freq[rev]) * 4;
            }
        }
        if (center) ans += 2;
        return ans;
    }
};

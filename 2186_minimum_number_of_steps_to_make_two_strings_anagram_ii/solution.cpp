// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

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
    int minSteps(string s, string t) {
        int freq[26] = {};
        for (char c : s) freq[c - 'a']++;
        for (char c : t) freq[c - 'a']--;
        int ans = 0;
        for (int v : freq) ans += abs(v);
        return ans;
    }
};

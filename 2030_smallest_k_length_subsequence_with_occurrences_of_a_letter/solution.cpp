// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

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
    string smallestSubsequence(string s, int k, char letter, int repetition) {
        int n = (int)s.size(), remainLetter = 0;
        for (char c : s) if (c == letter) remainLetter++;
        string stack;
        int inStackLetter = 0;
        for (int i = 0; i < n; i++) {
            char ch = s[i];
            while (!stack.empty() && ch < stack.back() && (int)stack.size() + n - i > k) {
                char top = stack.back();
                if (top == letter) {
                    if (inStackLetter + remainLetter - 1 < repetition) break;
                    inStackLetter--;
                }
                stack.pop_back();
            }
            if ((int)stack.size() < k) {
                if (ch == letter) { stack.push_back(ch); inStackLetter++; }
                else if (k - (int)stack.size() > repetition - inStackLetter) stack.push_back(ch);
            }
            if (ch == letter) remainLetter--;
        }
        return stack;
    }
};

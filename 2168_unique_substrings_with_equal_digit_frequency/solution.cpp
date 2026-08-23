// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

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
    int equalDigitFrequency(string s) {
        int n = s.size();
        unordered_set<string> seen;
        for (int i = 0; i < n; i++) {
            int freq[10] = {}, maxf = 0, kinds = 0;
            for (int j = i; j < n; j++) {
                int d = s[j] - '0';
                if (freq[d] == 0) kinds++;
                freq[d]++;
                maxf = max(maxf, freq[d]);
                if (maxf * kinds == j - i + 1) seen.insert(s.substr(i, j - i + 1));
            }
        }
        return (int)seen.size();
    }
};

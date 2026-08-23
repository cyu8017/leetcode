// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

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
    string repeatLimitedString(string s, int repeatLimit) {
        int freq[26] = {};
        for (char c : s) freq[c - 'a']++;
        string ans;
        while (true) {
            bool placed = false;
            for (int c = 25; c >= 0; c--) {
                if (freq[c] == 0) continue;
                if (!ans.empty() && ans.back() - 'a' == c) {
                    bool found = false;
                    for (int d = c - 1; d >= 0; d--) {
                        if (freq[d] > 0) {
                            ans.push_back('a' + d);
                            freq[d]--;
                            found = placed = true;
                            break;
                        }
                    }
                    if (!found) return ans;
                    break;
                }
                int use = min(freq[c], repeatLimit);
                for (int i = 0; i < use; i++) ans.push_back('a' + c);
                freq[c] -= use;
                placed = true;
                break;
            }
            if (!placed) break;
        }
        return ans;
    }
};

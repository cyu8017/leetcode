// LeetCode 2068 - Check Whether Two Strings Are Almost Equivalent
// https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

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
    bool checkAlmostEquivalent(string word1, string word2) {
        int freq[26] = {};
        for (int i = 0; i < (int)word1.size(); i++) {
            freq[word1[i] - 'a']++;
            freq[word2[i] - 'a']--;
        }
        for (int v : freq) if (v > 3 || v < -3) return false;
        return true;
    }
};

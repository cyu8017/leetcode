// LeetCode 2062 - Count Vowel Substrings of a String
// https://leetcode.com/problems/count-vowel-substrings-of-a-string/

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
    int countVowelSubstrings(string word) {
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        int ans = 0, n = (int)word.size();
        for (int i = 0; i < n; i++) {
            unordered_set<char> seen;
            for (int j = i; j < n && isVowel(word[j]); j++) {
                seen.insert(word[j]);
                if (seen.size() == 5) ans++;
            }
        }
        return ans;
    }
};

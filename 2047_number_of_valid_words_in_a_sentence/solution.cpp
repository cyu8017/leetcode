// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

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
    int countValidWords(string sentence) {
        auto valid = [](const string& w) {
            if (w.empty()) return false;
            int hyphen = 0;
            for (int i = 0; i < (int)w.size(); i++) {
                char c = w[i];
                if (c >= '0' && c <= '9') return false;
                if (c == '-') {
                    hyphen++;
                    if (hyphen > 1 || i == 0 || i == (int)w.size() - 1) return false;
                    if (w[i - 1] < 'a' || w[i - 1] > 'z' || w[i + 1] < 'a' || w[i + 1] > 'z') return false;
                } else if (c == '!' || c == '.' || c == ',') {
                    if (i != (int)w.size() - 1) return false;
                } else if (c < 'a' || c > 'z') return false;
            }
            return true;
        };
        int ans = 0;
        stringstream ss(sentence);
        string w;
        while (ss >> w) if (valid(w)) ans++;
        return ans;
    }
};

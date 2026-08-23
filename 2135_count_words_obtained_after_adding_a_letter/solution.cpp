// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

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
    int wordCount(vector<string>& startWords, vector<string>& targetWords) {
        auto mask = [](const string& w) {
            int m = 0;
            for (char c : w) m |= 1 << (c - 'a');
            return m;
        };
        unordered_set<int> have;
        for (auto& w : startWords) have.insert(mask(w));
        int ans = 0;
        for (auto& w : targetWords) {
            int m = mask(w);
            for (int i = 0; i < (int)w.size(); i++) {
                if (have.count(m ^ (1 << (w[i] - 'a')))) { ans++; break; }
            }
        }
        return ans;
    }
};

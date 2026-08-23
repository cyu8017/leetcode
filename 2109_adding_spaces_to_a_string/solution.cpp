// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

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
    string addSpaces(string s, vector<int>& spaces) {
        string b;
        b.reserve(s.size() + spaces.size());
        int j = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            if (j < (int)spaces.size() && spaces[j] == i) { b.push_back(' '); j++; }
            b.push_back(s[i]);
        }
        return b;
    }
};

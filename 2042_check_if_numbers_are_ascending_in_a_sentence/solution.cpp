// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

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
    bool areNumbersAscending(string s) {
        int prev = -1;
        stringstream ss(s);
        string tok;
        while (ss >> tok) {
            if (tok[0] >= '0' && tok[0] <= '9') {
                int v = stoi(tok);
                if (v <= prev) return false;
                prev = v;
            }
        }
        return true;
    }
};

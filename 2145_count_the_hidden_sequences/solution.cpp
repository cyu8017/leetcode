// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

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
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        long long cur = 0, mn = 0, mx = 0;
        for (int d : differences) {
            cur += d;
            mn = min(mn, cur);
            mx = max(mx, cur);
        }
        long long res = (long long)(upper - lower) - (mx - mn) + 1;
        return res < 0 ? 0 : (int)res;
    }
};

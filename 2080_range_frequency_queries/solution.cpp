// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

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

class RangeFreqQuery {
    unordered_map<int, vector<int>> pos;
public:
    RangeFreqQuery(vector<int>& arr) {
        for (int i = 0; i < (int)arr.size(); i++) pos[arr[i]].push_back(i);
    }
    int query(int left, int right, int value) {
        auto& p = pos[value];
        auto l = lower_bound(p.begin(), p.end(), left);
        auto r = upper_bound(p.begin(), p.end(), right);
        return (int)(r - l);
    }
};

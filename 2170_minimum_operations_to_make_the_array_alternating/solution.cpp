// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

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
    int minimumOperations(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;
        auto top2 = [&](const vector<int>& idxs) {
            unordered_map<int, int> freq;
            for (int i : idxs) freq[nums[i]]++;
            int a = 0, ac = 0, b = 0, bc = 0;
            for (auto& [v, c] : freq) {
                if (c > ac) { b = a; bc = ac; a = v; ac = c; }
                else if (c > bc) { b = v; bc = c; }
            }
            return array<int,4>{a, ac, b, bc};
        };
        vector<int> even, odd;
        for (int i = 0; i < n; i++) (i % 2 == 0 ? even : odd).push_back(i);
        auto e = top2(even), o = top2(odd);
        if (e[0] != o[0]) return n - e[1] - o[1];
        return min(n - e[1] - o[3], n - e[3] - o[1]);
    }
};

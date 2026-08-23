// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

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
    int digArtifacts(int n, vector<vector<int>>& artifacts, vector<vector<int>>& dig) {
        set<pair<int,int>> dug;
        for (auto& d : dig) dug.insert({d[0], d[1]});
        int ans = 0;
        for (auto& a : artifacts) {
            bool ok = true;
            for (int r = a[0]; r <= a[2]; r++)
                for (int c = a[1]; c <= a[3]; c++)
                    if (!dug.count({r, c})) ok = false;
            if (ok) ans++;
        }
        return ans;
    }
};

// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

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
    vector<int> groupStrings(vector<string>& words) {
        unordered_map<int, int> parent, size, freq;
        function<int(int)> find = [&](int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        auto unite = [&](int a, int b) {
            int ra = find(a), rb = find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) swap(ra, rb);
            parent[rb] = ra;
            size[ra] += size[rb];
        };
        auto maskOf = [](const string& w) {
            int m = 0;
            for (char c : w) m |= 1 << (c - 'a');
            return m;
        };
        for (auto& w : words) freq[maskOf(w)]++;
        for (auto& [m, c] : freq) { parent[m] = m; size[m] = c; }
        for (auto& [m, _] : freq) {
            for (int b = 0; b < 26; b++) {
                if (m & (1 << b)) {
                    int nm = m ^ (1 << b);
                    if (freq.count(nm)) unite(m, nm);
                    for (int a = 0; a < 26; a++) {
                        if ((nm & (1 << a)) == 0) {
                            int rm = nm | (1 << a);
                            if (freq.count(rm)) unite(m, rm);
                        }
                    }
                } else {
                    int nm = m | (1 << b);
                    if (freq.count(nm)) unite(m, nm);
                }
            }
        }
        int groups = 0, maxSize = 0;
        unordered_set<int> seen;
        for (auto& [m, _] : freq) {
            int r = find(m);
            if (!seen.count(r)) {
                seen.insert(r);
                groups++;
                maxSize = max(maxSize, size[r]);
            }
        }
        return {groups, maxSize};
    }
};

// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

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
    int numberOfPaths(int n, vector<vector<int>>& corridors) {
        vector<unordered_set<int>> g(n + 1);
        for (auto& e : corridors) {
            int a = e[0], b = e[1];
            g[a].insert(b);
            g[b].insert(a);
        }
        int ans = 0;
        for (auto& e : corridors) {
            int a = e[0], b = e[1];
            for (int c : g[a]) if (g[b].count(c)) ans++;
        }
        return ans / 3;
    }
};

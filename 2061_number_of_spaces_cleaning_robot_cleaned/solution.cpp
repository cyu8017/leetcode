// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

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
    int numberOfCleanRooms(vector<vector<int>>& room) {
        int m = (int)room.size(), n = (int)room[0].size();
        int dirs[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
        set<array<int,3>> vis;
        set<pair<int,int>> cleaned{{0, 0}};
        int r = 0, c = 0, d = 0;
        while (!vis.count({r, c, d})) {
            vis.insert({r, c, d});
            int nr = r + dirs[d][0], nc = c + dirs[d][1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && room[nr][nc] == 0) {
                r = nr; c = nc;
                cleaned.insert({r, c});
            } else d = (d + 1) % 4;
        }
        return (int)cleaned.size();
    }
};

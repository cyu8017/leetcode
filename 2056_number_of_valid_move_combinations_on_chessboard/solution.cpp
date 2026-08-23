// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

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
    struct Move { int dr, dc, steps; };
public:
    int countCombinations(vector<string>& pieces, vector<vector<int>>& positions) {
        unordered_map<string, vector<pair<int,int>>> dirs = {
            {"rook", {{1,0},{-1,0},{0,1},{0,-1}}},
            {"bishop", {{1,1},{1,-1},{-1,1},{-1,-1}}},
            {"queen", {{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}}},
        };
        int n = (int)pieces.size();
        vector<vector<Move>> allMoves(n);
        for (int i = 0; i < n; i++) {
            vector<Move> ms{{0, 0, 0}};
            int r = positions[i][0], c = positions[i][1];
            for (auto [dr, dc] : dirs[pieces[i]]) {
                int nr = r + dr, nc = c + dc, step = 1;
                while (nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8) {
                    ms.push_back({dr, dc, step});
                    nr += dr; nc += dc; step++;
                }
            }
            allMoves[i] = ms;
        }
        vector<Move> chosen(n);
        auto okCombo = [&](int end) {
            int maxT = 0;
            for (int i = 0; i <= end; i++) maxT = max(maxT, chosen[i].steps);
            for (int t = 1; t <= maxT; t++) {
                map<pair<int,int>, int> pos;
                for (int i = 0; i <= end; i++) {
                    auto m = chosen[i];
                    int pr, pc;
                    if (m.steps == 0) {
                        pr = positions[i][0]; pc = positions[i][1];
                    } else {
                        int use = min(t, m.steps);
                        pr = positions[i][0] + m.dr * use;
                        pc = positions[i][1] + m.dc * use;
                    }
                    if (pos.count({pr, pc})) return false;
                    pos[{pr, pc}] = i;
                }
            }
            return true;
        };
        int ans = 0;
        function<void(int)> dfs = [&](int i) {
            if (i == n) { ans++; return; }
            for (auto& m : allMoves[i]) {
                chosen[i] = m;
                if (okCombo(i)) dfs(i + 1);
            }
        };
        dfs(0);
        return ans;
    }
};

// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

#include <queue>
#include <tuple>
#include <vector>

class Solution {
public:
    int catMouseGame(std::vector<std::vector<int>>& graph) {
        const int n = (int)graph.size();
        const int DRAW = 0, MOUSE_WIN = 1, CAT_WIN = 2;
        std::vector states(n, std::vector(n, std::vector<int>(2, DRAW)));
        std::vector outDegree(n, std::vector(n, std::vector<int>(2, 0)));
        std::queue<std::tuple<int, int, int, int>> q;

        for (int cat = 0; cat < n; cat++) {
            for (int mouse = 0; mouse < n; mouse++) {
                outDegree[cat][mouse][0] = (int)graph[mouse].size();
                int deg = 0;
                for (int x : graph[cat]) if (x != 0) deg++;
                outDegree[cat][mouse][1] = deg;
            }
        }
        for (int cat = 1; cat < n; cat++) {
            for (int move = 0; move < 2; move++) {
                states[cat][0][move] = MOUSE_WIN;
                q.emplace(cat, 0, move, MOUSE_WIN);
                states[cat][cat][move] = CAT_WIN;
                q.emplace(cat, cat, move, CAT_WIN);
            }
        }
        while (!q.empty()) {
            auto [cat, mouse, move, state] = q.front();
            q.pop();
            if (cat == 2 && mouse == 1 && move == 0) return state;
            int prevMove = move ^ 1;
            for (int prev : graph[prevMove ? cat : mouse]) {
                int prevCat = prevMove ? prev : cat;
                if (prevCat == 0) continue;
                int prevMouse = prevMove ? mouse : prev;
                if (states[prevCat][prevMouse][prevMove]) continue;
                if ((prevMove == 0 && state == MOUSE_WIN) ||
                    (prevMove == 1 && state == CAT_WIN) ||
                    outDegree[prevCat][prevMouse][prevMove] == 1) {
                    states[prevCat][prevMouse][prevMove] = state;
                    q.emplace(prevCat, prevMouse, prevMove, state);
                } else {
                    outDegree[prevCat][prevMouse][prevMove]--;
                }
            }
        }
        return states[2][1][0];
    }
};

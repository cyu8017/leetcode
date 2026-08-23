// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> survivedRobotsHealths(std::vector<int>& positions, std::vector<int>& healths, std::string directions) {
        int n = (int)positions.size();
        std::vector<int> idx(n);
        for (int i = 0; i < n; i++) idx[i] = i;
        std::sort(idx.begin(), idx.end(), [&](int a, int b) { return positions[a] < positions[b]; });
        struct Robot { int i, h; char d; };
        std::vector<Robot> stack;
        for (int i : idx) {
            Robot cur{i, healths[i], directions[i]};
            while (!stack.empty() && stack.back().d == 'R' && cur.d == 'L') {
                if (stack.back().h == cur.h) {
                    stack.pop_back();
                    cur.h = 0;
                    break;
                } else if (stack.back().h > cur.h) {
                    stack.back().h--;
                    cur.h = 0;
                    break;
                } else {
                    cur.h--;
                    stack.pop_back();
                }
            }
            if (cur.h > 0) stack.push_back(cur);
        }
        std::unordered_map<int, int> alive;
        for (auto& r : stack) alive[r.i] = r.h;
        std::vector<int> ans;
        for (int i = 0; i < n; i++) {
            if (alive.count(i)) ans.push_back(alive[i]);
        }
        return ans;
    }
};

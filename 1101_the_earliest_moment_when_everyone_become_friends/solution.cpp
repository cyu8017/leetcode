// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int earliestAcq(std::vector<std::vector<int>>& logs, int n) {
        std::vector<int> parent(n);
        std::iota(parent.begin(), parent.end(), 0);

        auto find = [&](int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };

        auto unite = [&](int a, int b) {
            int ra = find(a);
            int rb = find(b);
            if (ra == rb) {
                return false;
            }
            parent[rb] = ra;
            return true;
        };

        std::sort(logs.begin(), logs.end());
        int components = n;
        for (const auto& log : logs) {
            if (unite(log[1], log[2])) {
                --components;
                if (components == 1) {
                    return log[0];
                }
            }
        }
        return -1;
    }
};

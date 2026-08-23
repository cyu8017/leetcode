// LeetCode 0403 - Frog Jump
// https://leetcode.com/problems/frog-jump/

#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool canCross(vector<int>& stones) {
        unordered_map<int, unordered_set<int>> jumps;
        unordered_set<int> stoneSet(stones.begin(), stones.end());

        for (int stone : stones) {
            jumps[stone];
        }
        jumps[0].insert(0);

        for (int stone : stones) {
            for (int jump : jumps[stone]) {
                for (int nextJump : {jump - 1, jump, jump + 1}) {
                    if (nextJump > 0 && stoneSet.count(stone + nextJump)) {
                        jumps[stone + nextJump].insert(nextJump);
                    }
                }
            }
        }

        return !jumps[stones.back()].empty();
    }
};

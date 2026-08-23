// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int shortestSequence(std::vector<int>& rolls, int k) {
        std::unordered_set<int> seen;
        int ans = 1;
        for (int r : rolls) {
            seen.insert(r);
            if ((int)seen.size() == k) {
                ans++;
                seen.clear();
            }
        }
        return ans;
    }
};

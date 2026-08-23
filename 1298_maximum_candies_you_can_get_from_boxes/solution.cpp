// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

#include <queue>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int maxCandies(std::vector<int>& status, std::vector<int>& candies, std::vector<std::vector<int>>& keys,
                   std::vector<std::vector<int>>& containedBoxes, std::vector<int>& initialBoxes) {
        std::unordered_set<int> owned(initialBoxes.begin(), initialBoxes.end());
        std::unordered_set<int> opened;
        std::queue<int> q;
        for (int box : initialBoxes) {
            if (status[box]) {
                q.push(box);
            }
        }
        int total = 0;
        while (!q.empty()) {
            int box = q.front();
            q.pop();
            if (opened.count(box) || !status[box]) {
                continue;
            }
            opened.insert(box);
            total += candies[box];
            for (int key : keys[box]) {
                status[key] = 1;
                if (owned.count(key) && !opened.count(key)) {
                    q.push(key);
                }
            }
            for (int child : containedBoxes[box]) {
                owned.insert(child);
                if (status[child] && !opened.count(child)) {
                    q.push(child);
                }
            }
        }
        return total;
    }
};

// LeetCode 0406 - Queue Reconstruction by Height
// https://leetcode.com/problems/queue-reconstruction-by-height/

#include <algorithm>
#include <vector>

class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](const vector<int>& left, const vector<int>& right) {
            if (left[0] != right[0]) {
                return left[0] > right[0];
            }
            return left[1] < right[1];
        });

        vector<vector<int>> queue;
        for (const vector<int>& person : people) {
            queue.insert(queue.begin() + person[1], person);
        }

        return queue;
    }
};

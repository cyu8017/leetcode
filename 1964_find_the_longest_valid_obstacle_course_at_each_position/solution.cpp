// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> longestObstacleCourseAtEachPosition(std::vector<int>& obstacles) {
        std::vector<int> tails, ans;
        for (int x : obstacles) {
            auto it = std::upper_bound(tails.begin(), tails.end(), x);
            int i = (int)(it - tails.begin());
            if (it == tails.end()) tails.push_back(x);
            else *it = x;
            ans.push_back(i + 1);
        }
        return ans;
    }
};

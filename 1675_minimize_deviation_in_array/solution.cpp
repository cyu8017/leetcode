// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

#include <algorithm>
#include <climits>
#include <queue>
#include <vector>

class Solution {
public:
    int minimumDeviation(std::vector<int>& nums) {
        std::priority_queue<int> pq;
        int mn = INT_MAX;
        for (int x : nums) {
            if (x % 2) {
                x *= 2;
            }
            mn = std::min(mn, x);
            pq.push(x);
        }
        int ans = INT_MAX;
        while (true) {
            int x = pq.top();
            pq.pop();
            ans = std::min(ans, x - mn);
            if (x % 2) {
                return ans;
            }
            x /= 2;
            mn = std::min(mn, x);
            pq.push(x);
        }
    }
};

// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

#include <queue>
#include <vector>

class Solution {
public:
    int minRefuelStops(int target, int startFuel, std::vector<std::vector<int>>& stations) {
        std::priority_queue<int> pq;
        stations.push_back({target, 0});
        int ans = 0, prev = 0;
        long long fuel = startFuel;
        for (auto& st : stations) {
            int pos = st[0], gas = st[1];
            fuel -= pos - prev;
            while (!pq.empty() && fuel < 0) {
                fuel += pq.top();
                pq.pop();
                ++ans;
            }
            if (fuel < 0) {
                return -1;
            }
            pq.push(gas);
            prev = pos;
        }
        return ans;
    }
};

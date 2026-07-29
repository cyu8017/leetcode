// LeetCode 1184 - Distance Between Bus Stops
// https://leetcode.com/problems/distance-between-bus-stops/

#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int distanceBetweenBusStops(std::vector<int>& distance, int start, int destination) {
        if (start > destination) std::swap(start, destination);
        int clockwise = std::accumulate(distance.begin() + start, distance.begin() + destination, 0);
        int total = std::accumulate(distance.begin(), distance.end(), 0);
        return std::min(clockwise, total - clockwise);
    }
};

// LeetCode 1942 - The Number of the Smallest Unoccupied Chair
#include <algorithm>
#include <queue>
#include <vector>

class Solution {
public:
    int smallestChair(std::vector<std::vector<int>>& times, int targetFriend) {
        int n = (int)times.size();
        std::vector<int> order(n);
        for (int i = 0; i < n; i++) order[i] = i;
        std::sort(order.begin(), order.end(), [&](int a, int b) { return times[a][0] < times[b][0]; });
        std::priority_queue<int, std::vector<int>, std::greater<>> free;
        int nextChair = 0;
        using P = std::pair<int, int>;
        std::priority_queue<P, std::vector<P>, std::greater<>> leaving;
        for (int i : order) {
            int arr = times[i][0], leave = times[i][1];
            while (!leaving.empty() && leaving.top().first <= arr) {
                free.push(leaving.top().second);
                leaving.pop();
            }
            int chair;
            if (!free.empty()) { chair = free.top(); free.pop(); }
            else chair = nextChair++;
            if (i == targetFriend) return chair;
            leaving.emplace(leave, chair);
        }
        return -1;
    }
};

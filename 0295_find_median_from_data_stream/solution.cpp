// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

#include <queue>
#include <vector>

class MedianFinder {
    std::priority_queue<int> small;
    std::priority_queue<int, std::vector<int>, std::greater<int>> large;

public:
    MedianFinder() = default;

    void addNum(int num) {
        small.push(num);
        large.push(small.top());
        small.pop();
        if (large.size() > small.size()) {
            small.push(large.top());
            large.pop();
        }
    }

    double findMedian() {
        if (small.size() > large.size()) {
            return static_cast<double>(small.top());
        }
        return (static_cast<double>(small.top()) + large.top()) / 2.0;
    }
};

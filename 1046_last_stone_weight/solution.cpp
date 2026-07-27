// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/

#include <queue>
#include <vector>

class Solution {
public:
    int lastStoneWeight(std::vector<int>& stones) {
        std::priority_queue<int> heap(stones.begin(), stones.end());
        while (heap.size() > 1) {
            int a = heap.top();
            heap.pop();
            int b = heap.top();
            heap.pop();
            if (a != b) heap.push(a - b);
        }
        return heap.empty() ? 0 : heap.top();
    }
};


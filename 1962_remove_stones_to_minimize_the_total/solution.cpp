// LeetCode 1962 - Remove Stones to Minimize the Total
#include <queue>
#include <vector>

class Solution {
public:
    int minStoneSum(std::vector<int>& piles, int k) {
        std::priority_queue<int> heap(piles.begin(), piles.end());
        for (int i = 0; i < k; i++) {
            int x = heap.top(); heap.pop();
            heap.push(x - x / 2);
        }
        int sum = 0;
        while (!heap.empty()) { sum += heap.top(); heap.pop(); }
        return sum;
    }
};

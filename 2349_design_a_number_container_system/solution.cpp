// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

#include <queue>
#include <unordered_map>
#include <vector>

class NumberContainers {
public:
    NumberContainers() {}

    void change(int index, int number) {
        idx[index] = number;
        heap[number].push(index);
    }

    int find(int number) {
        auto it = heap.find(number);
        if (it == heap.end()) return -1;
        auto& h = it->second;
        while (!h.empty()) {
            int i = h.top();
            if (idx[i] == number) return i;
            h.pop();
        }
        return -1;
    }

private:
    std::unordered_map<int, int> idx;
    std::unordered_map<int, std::priority_queue<int, std::vector<int>, std::greater<int>>> heap;
};

// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

#include <queue>
#include <unordered_set>

class SmallestInfiniteSet {
public:
    SmallestInfiniteSet() : next(1) {}

    int popSmallest() {
        if (!heap.empty()) {
            int x = heap.top();
            heap.pop();
            added.erase(x);
            return x;
        }
        return next++;
    }

    void addBack(int num) {
        if (num < next && !added.count(num)) {
            added.insert(num);
            heap.push(num);
        }
    }

private:
    int next;
    std::unordered_set<int> added;
    std::priority_queue<int, std::vector<int>, std::greater<int>> heap;
};

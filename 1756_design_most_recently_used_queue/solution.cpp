// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

#include <vector>

class MRUQueue {
public:
    MRUQueue(int n) {
        q.reserve(n);
        for (int i = 1; i <= n; i++) {
            q.push_back(i);
        }
    }

    int fetch(int k) {
        int val = q[k - 1];
        q.erase(q.begin() + (k - 1));
        q.push_back(val);
        return val;
    }

private:
    std::vector<int> q;
};

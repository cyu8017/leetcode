#include <numeric>
#include <queue>
#include <vector>

class Solution {
public:
    bool isPossible(std::vector<int>& target) {
        if (target.size() == 1) return target[0] == 1;
        long long total = std::accumulate(target.begin(), target.end(), 0LL);
        std::priority_queue<long long> h(target.begin(), target.end());
        while (true) {
            long long x = h.top(); h.pop();
            long long rest = total - x;
            if (x == 1 || rest == 1) return true;
            if (rest == 0 || x <= rest) return false;
            long long prev = x % rest;
            if (prev == 0) return false;
            total = rest + prev;
            h.push(prev);
        }
    }
};

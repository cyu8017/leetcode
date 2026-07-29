// LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    long long numberOfWeeks(std::vector<int>& milestones) {
        long long total = std::accumulate(milestones.begin(), milestones.end(), 0LL);
        long long mx = *std::max_element(milestones.begin(), milestones.end());
        long long rest = total - mx;
        if (mx > rest + 1) return 2 * rest + 1;
        return total;
    }
};

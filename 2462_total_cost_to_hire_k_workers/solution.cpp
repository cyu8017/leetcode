// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    long long totalCost(std::vector<int>& costs, int k, int candidates) {
        using P = std::pair<int, int>;
        auto cmp = [](const P& a, const P& b) {
            if (a.first != b.first) return a.first > b.first;
            return a.second > b.second;
        };
        std::priority_queue<P, std::vector<P>, decltype(cmp)> leftH(cmp), rightH(cmp);
        int n = (int)costs.size();
        int l = 0, r = n - 1;
        while (l <= r && (int)leftH.size() < candidates) {
            leftH.push({costs[l], l});
            l++;
        }
        while (r >= l && (int)rightH.size() < candidates) {
            rightH.push({costs[r], r});
            r--;
        }
        long long ans = 0;
        for (int t = 0; t < k; t++) {
            bool useLeft = false;
            if (!leftH.empty() && !rightH.empty()) {
                if (leftH.top().first < rightH.top().first ||
                    (leftH.top().first == rightH.top().first &&
                     leftH.top().second <= rightH.top().second)) {
                    useLeft = true;
                }
            } else if (!leftH.empty()) {
                useLeft = true;
            }
            if (useLeft) {
                ans += leftH.top().first;
                leftH.pop();
                if (l <= r) {
                    leftH.push({costs[l], l});
                    l++;
                }
            } else {
                ans += rightH.top().first;
                rightH.pop();
                if (l <= r) {
                    rightH.push({costs[r], r});
                    r--;
                }
            }
        }
        return ans;
    }
};

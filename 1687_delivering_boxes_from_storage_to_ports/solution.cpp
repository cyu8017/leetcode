// LeetCode 1687 - Delivering Boxes from Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

#include <deque>
#include <vector>

class Solution {
public:
    int boxDelivering(std::vector<std::vector<int>>& boxes, int portsCount, int maxBoxes, int maxWeight) {
        (void)portsCount;
        int n = static_cast<int>(boxes.size());
        std::vector<long long> w(n + 1, 0);
        std::vector<int> changes(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            w[i] = w[i - 1] + boxes[i - 1][1];
            changes[i] = changes[i - 1] + (i > 1 && boxes[i - 1][0] != boxes[i - 2][0] ? 1 : 0);
        }
        std::vector<int> dp(n + 1, 0);
        std::deque<int> q;
        q.push_back(0);
        for (int i = 1; i <= n; ++i) {
            while (!q.empty() && (i - q.front() > maxBoxes || w[i] - w[q.front()] > maxWeight)) {
                q.pop_front();
            }
            int j = q.front();
            dp[i] = dp[j] + changes[i] - changes[j + 1] + 2;
            if (i < n) {
                int val = dp[i] - changes[i + 1];
                while (!q.empty() && dp[q.back()] - changes[q.back() + 1] >= val) {
                    q.pop_back();
                }
                q.push_back(i);
            }
        }
        return dp[n];
    }
};

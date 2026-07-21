// LeetCode 1889 - Minimum Space Wasted From Packaging
// https://leetcode.com/problems/minimum-space-wasted-from-packaging/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minWastedSpace(std::vector<int>& packages, std::vector<std::vector<int>>& boxes) {
        std::sort(packages.begin(), packages.end());
        int n = static_cast<int>(packages.size());
        std::vector<long long> prefix(n);
        prefix[0] = packages[0];
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + packages[i];
        }

        long long answer = LLONG_MAX;
        for (auto& supplier : boxes) {
            std::sort(supplier.begin(), supplier.end());
            int start = 0;
            long long wasted = 0;
            for (int box : supplier) {
                auto it = std::upper_bound(packages.begin() + start, packages.end(), box);
                int end = static_cast<int>(it - packages.begin());
                if (end == start) continue;
                long long packageSum = prefix[end - 1] - (start ? prefix[start - 1] : 0);
                wasted += 1LL * box * (end - start) - packageSum;
                start = end;
            }
            if (start == n) {
                answer = std::min(answer, wasted);
            }
        }
        return answer == LLONG_MAX ? -1 : static_cast<int>(answer % 1000000007LL);
    }
};

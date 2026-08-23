// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

#include <algorithm>
#include <queue>
#include <vector>

class Solution {
    struct SparseTableRMQ {
        int n, maxLog;
        std::vector<std::vector<int>> fMax, fMin;
        std::vector<int> lg;

        explicit SparseTableRMQ(const std::vector<int>& data) {
            n = (int)data.size();
            maxLog = 0;
            while ((1 << maxLog) <= n) maxLog++;
            maxLog++;
            fMax.assign(n, std::vector<int>(maxLog));
            fMin.assign(n, std::vector<int>(maxLog));
            lg.assign(n + 1, 0);
            for (int i = 2; i <= n; i++) lg[i] = lg[i >> 1] + 1;
            for (int i = 0; i < n; i++) {
                fMax[i][0] = data[i];
                fMin[i][0] = data[i];
            }
            for (int j = 1; j < maxLog; j++) {
                for (int i = 0; i <= n - (1 << j); i++) {
                    fMax[i][j] = std::max(fMax[i][j - 1], fMax[i + (1 << (j - 1))][j - 1]);
                    fMin[i][j] = std::min(fMin[i][j - 1], fMin[i + (1 << (j - 1))][j - 1]);
                }
            }
        }

        int queryMax(int l, int r) {
            int k = lg[r - l + 1];
            return std::max(fMax[l][k], fMax[r - (1 << k) + 1][k]);
        }

        int queryMin(int l, int r) {
            int k = lg[r - l + 1];
            return std::min(fMin[l][k], fMin[r - (1 << k) + 1][k]);
        }
    };

public:
    long long maxTotalValue(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        SparseTableRMQ st(nums);
        using Item = std::tuple<long long, int, int>;
        std::priority_queue<Item> pq;
        for (int l = 0; l < n; l++) {
            long long val = (long long)st.queryMax(l, n - 1) - st.queryMin(l, n - 1);
            pq.emplace(val, l, n - 1);
        }
        long long ans = 0;
        for (int i = 0; i < k; i++) {
            auto [val, l, r] = pq.top();
            pq.pop();
            ans += val;
            if (r > l) {
                long long nextVal = (long long)st.queryMax(l, r - 1) - st.queryMin(l, r - 1);
                pq.emplace(nextVal, l, r - 1);
            }
        }
        return ans;
    }
};

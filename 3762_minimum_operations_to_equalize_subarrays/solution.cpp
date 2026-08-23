// LeetCode 3762 - Minimum Operations to Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

#include <algorithm>
#include <functional>
#include <vector>

class Solution {
    struct Node {
        int left = 0, right = 0, count = 0;
        long long sum = 0;
    };

public:
    std::vector<long long> minOperations(std::vector<int>& nums, int k, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> quotient(n), remainder(n), values(n);
        for (int i = 0; i < n; i++) {
            quotient[i] = nums[i] / k;
            remainder[i] = nums[i] % k;
            values[i] = quotient[i];
        }
        std::sort(values.begin(), values.end());
        values.erase(std::unique(values.begin(), values.end()), values.end());
        std::vector<Node> nodes(1);
        std::function<int(int, int, int, int, int)> update = [&](int previous, int lo, int hi, int position, int value) -> int {
            int current = (int)nodes.size();
            nodes.push_back(nodes[previous]);
            nodes[current].count++;
            nodes[current].sum += value;
            if (lo < hi) {
                int mid = (lo + hi) / 2;
                if (position <= mid) nodes[current].left = update(nodes[previous].left, lo, mid, position, value);
                else nodes[current].right = update(nodes[previous].right, mid + 1, hi, position, value);
            }
            return current;
        };
        std::vector<int> roots(n + 1);
        int umax = (int)values.size() - 1;
        for (int i = 0; i < n; i++) {
            int position = (int)(std::lower_bound(values.begin(), values.end(), quotient[i]) - values.begin());
            roots[i + 1] = update(roots[i], 0, umax, position, quotient[i]);
        }
        std::function<int(int, int, int, int, int)> kth = [&](int rightRoot, int leftRoot, int lo, int hi, int rank) -> int {
            if (lo == hi) return lo;
            int leftCount = nodes[nodes[rightRoot].left].count - nodes[nodes[leftRoot].left].count;
            int mid = (lo + hi) / 2;
            if (rank <= leftCount) return kth(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, rank);
            return kth(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, rank - leftCount);
        };
        std::function<std::pair<int, long long>(int, int, int, int, int)> prefixStats =
            [&](int rightRoot, int leftRoot, int lo, int hi, int end) -> std::pair<int, long long> {
            if (end < lo) return {0, 0};
            if (hi <= end) return {nodes[rightRoot].count - nodes[leftRoot].count,
                                   nodes[rightRoot].sum - nodes[leftRoot].sum};
            int mid = (lo + hi) / 2;
            auto [count, sum] = prefixStats(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, end);
            if (end > mid) {
                auto [c2, s2] = prefixStats(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, end);
                count += c2;
                sum += s2;
            }
            return {count, sum};
        };
        std::vector<int> logv(n + 1);
        for (int i = 2; i <= n; i++) logv[i] = logv[i / 2] + 1;
        int levels = logv[n] + 1;
        std::vector<std::vector<int>> minTable(levels), maxTable(levels);
        minTable[0] = remainder;
        maxTable[0] = remainder;
        for (int level = 1; level < levels; level++) {
            int length = n - (1 << level) + 1;
            minTable[level].resize(length);
            maxTable[level].resize(length);
            int half = 1 << (level - 1);
            for (int i = 0; i < length; i++) {
                minTable[level][i] = std::min(minTable[level - 1][i], minTable[level - 1][i + half]);
                maxTable[level][i] = std::max(maxTable[level - 1][i], maxTable[level - 1][i + half]);
            }
        }
        std::vector<long long> answer(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int left = queries[qi][0], right = queries[qi][1];
            int length = right - left + 1;
            int level = logv[length];
            int offset = right - (1 << level) + 1;
            int minR = std::min(minTable[level][left], minTable[level][offset]);
            int maxR = std::max(maxTable[level][left], maxTable[level][offset]);
            if (minR != maxR) {
                answer[qi] = -1;
                continue;
            }
            int medianIndex = kth(roots[right + 1], roots[left], 0, umax, (length + 1) / 2);
            int median = values[medianIndex];
            auto [leftCount, leftSum] = prefixStats(roots[right + 1], roots[left], 0, umax, medianIndex);
            long long totalSum = nodes[roots[right + 1]].sum - nodes[roots[left]].sum;
            answer[qi] = 1LL * median * leftCount - leftSum + (totalSum - leftSum) - 1LL * median * (length - leftCount);
        }
        return answer;
    }
};

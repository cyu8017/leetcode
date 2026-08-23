// LeetCode 3962 - Maximum Subarray Sum After at Most K Swaps
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxSubarraySum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<int> unique = nums;
        std::sort(unique.begin(), unique.end());
        unique.erase(std::unique(unique.begin(), unique.end()), unique.end());
        std::vector<int> rank(n);
        std::vector<int> globalCount(unique.size() + 1, 0);
        std::vector<long long> globalSum(unique.size() + 1, 0);
        auto add = [&](std::vector<int>& count, std::vector<long long>& sum, int index, int delta) {
            long long value = unique[index - 1];
            for (; index < (int)count.size(); index += index & -index) {
                count[index] += delta;
                sum[index] += (long long)delta * value;
            }
        };
        for (int i = 0; i < n; i++) {
            rank[i] = (int)(std::lower_bound(unique.begin(), unique.end(), nums[i]) - unique.begin()) + 1;
            add(globalCount, globalSum, rank[i], 1);
        }
        auto queryCount = [](std::vector<int>& bit, int index) {
            int result = 0;
            for (; index > 0; index -= index & -index) result += bit[index];
            return result;
        };
        auto querySum = [](std::vector<long long>& bit, int index) {
            long long result = 0;
            for (; index > 0; index -= index & -index) result += bit[index];
            return result;
        };
        auto kth = [](std::vector<int>& bit, int order) {
            int index = 0, step = 1;
            while ((step << 1) < (int)bit.size()) step <<= 1;
            for (; step > 0; step >>= 1) {
                int next = index + step;
                if (next < (int)bit.size() && bit[next] < order) {
                    index = next;
                    order -= bit[next];
                }
            }
            return index + 1;
        };
        auto sumSmallest = [&](std::vector<int>& count, std::vector<long long>& sum, int amount) {
            if (amount <= 0) return 0LL;
            int index = kth(count, amount);
            int countBefore = queryCount(count, index - 1);
            long long sumBefore = querySum(sum, index - 1);
            return sumBefore + (long long)(amount - countBefore) * unique[index - 1];
        };
        long long answer = -(1LL << 60);
        for (int left = 0; left < n; left++) {
            std::vector<int> insideCount(unique.size() + 1, 0);
            std::vector<long long> insideSum(unique.size() + 1, 0);
            std::vector<int> outsideCount = globalCount;
            std::vector<long long> outsideSum = globalSum;
            long long subarraySum = 0;
            for (int right = left; right < n; right++) {
                add(outsideCount, outsideSum, rank[right], -1);
                add(insideCount, insideSum, rank[right], 1);
                subarraySum += nums[right];
                int insideSize = right - left + 1;
                int outsideSize = n - insideSize;
                int limit = std::min({k, insideSize, outsideSize});
                int low = 0, high = limit;
                while (low < high) {
                    int mid = (low + high + 1) / 2;
                    int insideValue = unique[kth(insideCount, mid) - 1];
                    int outsideOrder = outsideSize - mid + 1;
                    int outsideValue = unique[kth(outsideCount, outsideOrder) - 1];
                    if (outsideValue > insideValue) low = mid;
                    else high = mid - 1;
                }
                int swaps = low;
                long long gain = 0;
                if (swaps > 0) {
                    long long smallInside = sumSmallest(insideCount, insideSum, swaps);
                    long long totalOutside = querySum(outsideSum, (int)unique.size());
                    long long largeOutside = totalOutside - sumSmallest(outsideCount, outsideSum, outsideSize - swaps);
                    gain = largeOutside - smallInside;
                }
                answer = std::max(answer, subarraySum + gain);
            }
        }
        return answer;
    }
};

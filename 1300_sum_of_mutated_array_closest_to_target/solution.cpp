#include <algorithm>
#include <climits>
#include <numeric>
#include <vector>

class Solution {
public:
    int findBestValue(std::vector<int>& arr, int target) {
        int lo = 0, hi = *std::max_element(arr.begin(), arr.end());
        auto mutatedSum = [&](int value) {
            long long sum = 0;
            for (int x : arr) sum += std::min(x, value);
            return sum;
        };
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (mutatedSum(mid) < target) lo = mid + 1;
            else hi = mid;
        }
        long long before = mutatedSum(lo - 1);
        long long after = mutatedSum(lo);
        return target - before <= after - target ? lo - 1 : lo;
    }
};

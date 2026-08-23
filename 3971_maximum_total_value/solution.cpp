// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

#include <vector>

class Solution {
public:
    int maximumTotalValue(std::vector<int>& value, std::vector<int>& decay, long long m) {
        const long long mod = 1000000007;
        auto countAtLeast = [&](long long threshold) {
            long long count = 0;
            for (int i = 0; i < (int)value.size(); i++) {
                if (value[i] >= threshold) {
                    count += (value[i] - threshold) / decay[i] + 1;
                }
            }
            return count;
        };
        if (countAtLeast(1) <= m) {
            long long sum = 0;
            for (int i = 0; i < (int)value.size(); i++) {
                long long terms = (value[i] - 1LL) / decay[i] + 1;
                sum = (sum + terms * value[i] - (long long)decay[i] * terms * (terms - 1) / 2) % mod;
            }
            return (int)sum;
        }
        long long high = 0;
        for (int v : value) if (v > high) high = v;
        long long low = 1;
        while (low < high) {
            long long mid = (low + high + 1) / 2;
            if (countAtLeast(mid) >= m) low = mid;
            else high = mid - 1;
        }
        long long threshold = low;
        long long count = 0, sum = 0;
        for (int i = 0; i < (int)value.size(); i++) {
            if (value[i] < threshold) continue;
            long long terms = (value[i] - threshold) / decay[i] + 1;
            count += terms;
            sum = (sum + (terms * value[i] - (long long)decay[i] * terms * (terms - 1) / 2) % mod) % mod;
        }
        sum = (sum - ((count - m) % mod) * (threshold % mod)) % mod;
        if (sum < 0) sum += mod;
        return (int)sum;
    }
};

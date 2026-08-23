// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

#include <cmath>
#include <vector>

class Solution {
    static constexpr int M = 100010;
    static std::vector<bool>& primes() {
        static std::vector<bool> p;
        if (p.empty()) {
            p.assign(M, true);
            p[0] = p[1] = false;
            for (int i = 2; i < M; i++)
                if (p[i])
                    for (int j = i + i; j < M; j += i) p[j] = false;
        }
        return p;
    }

public:
    long long splitArray(std::vector<int>& nums) {
        auto& pr = primes();
        long long ans = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (pr[i]) ans += nums[i];
            else ans -= nums[i];
        }
        return std::llabs(ans);
    }
};

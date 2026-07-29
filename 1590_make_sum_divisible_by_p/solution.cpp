// LeetCode 1590 - Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minSubarray(std::vector<int>& nums, int p) {
        long long total = 0;
        for (int x : nums) {
            total += x;
        }
        const int target = static_cast<int>(total % p);
        if (target == 0) {
            return 0;
        }
        std::unordered_map<int, int> seen{{0, -1}};
        long long prefix = 0;
        int answer = static_cast<int>(nums.size());
        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            prefix = (prefix + nums[i]) % p;
            const int need = static_cast<int>((prefix - target + p) % p);
            auto it = seen.find(need);
            if (it != seen.end()) {
                answer = std::min(answer, i - it->second);
            }
            seen[static_cast<int>(prefix)] = i;
        }
        return answer < static_cast<int>(nums.size()) ? answer : -1;
    }
};

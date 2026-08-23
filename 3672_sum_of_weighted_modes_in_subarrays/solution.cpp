// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
public:
    long long modeWeight(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> cnt;
        // pair: {freq, -val} so higher freq first, then smaller val
        using P = std::pair<int, int>;
        std::priority_queue<P> pq;

        for (int i = 0; i < k; i++) {
            int x = nums[i];
            cnt[x]++;
            pq.push({cnt[x], -x});
        }

        auto getMode = [&]() -> long long {
            while (true) {
                auto [freq, negVal] = pq.top();
                int val = -negVal;
                if (cnt[val] == freq) return 1LL * freq * val;
                pq.pop();
            }
        };

        long long ans = getMode();
        for (int i = k; i < (int)nums.size(); i++) {
            int x = nums[i], y = nums[i - k];
            cnt[x]++;
            cnt[y]--;
            pq.push({cnt[x], -x});
            pq.push({cnt[y], -y});
            ans += getMode();
        }
        return ans;
    }
};

// LeetCode 3020 - Find the Maximum Number of Elements in Subset
// https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maximumLength(std::vector<int>& nums) {
        std::unordered_map<long long, int> cnt;
        for (int x : nums) cnt[x]++;
        int ans = cnt[1] - ((cnt[1] % 2) ^ 1);
        cnt.erase(1);
        for (auto it = cnt.begin(); it != cnt.end(); ++it) {
            long long x = it->first;
            int t = 0;
            while (cnt[x] > 1) {
                x = x * x;
                t += 2;
            }
            if (cnt[x] > 0) t += 1;
            else t -= 1;
            ans = std::max(ans, t);
        }
        return ans;
    }
};

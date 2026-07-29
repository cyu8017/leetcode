#include <algorithm>
#include <vector>

class Solution {
public:
    int numSubseq(std::vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        const int mod = 1000000007;
        int n = (int)nums.size();
        std::vector<int> powers(n + 1, 1);
        for (int i = 1; i <= n; ++i) powers[i] = powers[i - 1] * 2 % mod;
        int left = 0, right = n - 1, ans = 0;
        while (left <= right) {
            if (nums[left] + nums[right] <= target) {
                ans = (ans + powers[right - left]) % mod;
                ++left;
            } else --right;
        }
        return ans;
    }
};

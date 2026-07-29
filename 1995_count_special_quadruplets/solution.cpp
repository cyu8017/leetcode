// LeetCode 1995 - Count Special Quadruplets
#include <vector>

class Solution {
public:
    int countQuadruplets(std::vector<int>& nums) {
        int n = (int)nums.size(), ans = 0;
        for (int a = 0; a < n; a++) {
            for (int b = a + 1; b < n; b++) {
                for (int c = b + 1; c < n; c++) {
                    int s = nums[a] + nums[b] + nums[c];
                    for (int d = c + 1; d < n; d++) if (nums[d] == s) ans++;
                }
            }
        }
        return ans;
    }
};

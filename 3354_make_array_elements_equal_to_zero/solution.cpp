// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

#include <vector>

class Solution {
public:
    int countValidSelections(std::vector<int>& nums) {
        int n = (int)nums.size();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) continue;
            for (int dir : {-1, 1}) {
                std::vector<int> a = nums;
                int cur = i, d = dir;
                while (cur >= 0 && cur < n) {
                    if (a[cur] == 0) cur += d;
                    else {
                        a[cur]--;
                        d = -d;
                        cur += d;
                    }
                }
                bool ok = true;
                for (int v : a) if (v != 0) { ok = false; break; }
                if (ok) ans++;
            }
        }
        return ans;
    }
};

// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    long long minimumMoves(std::vector<int>& nums, int k, int maxChanges) {
        int n = (int)nums.size();
        std::vector<int> cnt(n + 1), s(n + 1);
        for (int i = 1; i <= n; i++) {
            cnt[i] = cnt[i - 1] + nums[i - 1];
            s[i] = s[i - 1] + i * nums[i - 1];
        }
        long long ans = LLONG_MAX;
        for (int i = 1; i <= n; i++) {
            long long t = 0;
            int need = k - nums[i - 1];
            for (int j : {i - 1, i + 1}) {
                if (need > 0 && 1 <= j && j <= n && nums[j - 1] == 1) {
                    need--;
                    t++;
                }
            }
            int c = std::min(need, maxChanges);
            need -= c;
            t += c * 2;
            if (need <= 0) {
                ans = std::min(ans, t);
                continue;
            }
            int l = 2, r = std::max(i - 1, n - i);
            while (l <= r) {
                int mid = (l + r) >> 1;
                int l1 = std::max(1, i - mid), r1 = std::max(0, i - 2);
                int l2 = std::min(n + 1, i + 2), r2 = std::min(n, i + mid);
                int c1 = cnt[r1] - cnt[l1 - 1];
                int c2 = cnt[r2] - cnt[l2 - 1];
                if (c1 + c2 >= need) {
                    long long t1 = (long long)c1 * i - (s[r1] - s[l1 - 1]);
                    long long t2 = s[r2] - s[l2 - 1] - (long long)c2 * i;
                    ans = std::min(ans, t + t1 + t2);
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
        }
        return ans;
    }
};

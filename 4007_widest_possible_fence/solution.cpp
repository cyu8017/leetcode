// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maximumWidth(std::vector<int>& planks) {
        std::unordered_map<int, int> cnt;
        for (int x : planks) cnt[x]++;

        std::unordered_map<int, int> t;
        int ans = 0;

        for (auto& [x, v1] : cnt) {
            t[x] += v1;
            ans = std::max(ans, t[x]);

            t[x * 2] += v1 / 2;
            ans = std::max(ans, t[x * 2]);

            for (auto& [y, v2] : cnt) {
                if (y > x) {
                    int key = x + y;
                    t[key] += std::min(v1, v2);
                    ans = std::max(ans, t[key]);
                }
            }
        }
        return ans;
    }
};

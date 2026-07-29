// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int kEmptySlots(std::vector<int>& bulbs, int k) {
        const int n = static_cast<int>(bulbs.size());
        std::vector<int> days(n);
        for (int day = 1; day <= n; ++day) {
            days[bulbs[day - 1] - 1] = day;
        }

        int ans = INT_MAX;
        int i = 0;
        while (i < n - k - 1) {
            const int left = i;
            const int right = i + k + 1;
            int j = left + 1;
            while (j < right && days[j] > days[left] && days[j] > days[right]) {
                ++j;
            }
            if (j == right) {
                ans = std::min(ans, std::max(days[left], days[right]));
                ++i;
            } else {
                i = j;
            }
        }
        return ans == INT_MAX ? -1 : ans;
    }
};

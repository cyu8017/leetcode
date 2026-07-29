// LeetCode 1552 - Magnetic Force Between Two Balls
// https://leetcode.com/problems/magnetic-force-between-two-balls/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxDistance(std::vector<int>& position, int m) {
        std::sort(position.begin(), position.end());
        int lo = 1;
        int hi = (position.back() - position.front()) / (m - 1);
        while (lo <= hi) {
            const int mid = lo + (hi - lo) / 2;
            int count = 1;
            int last = position[0];
            for (std::size_t i = 1; i < position.size(); ++i) {
                if (position[i] - last >= mid) {
                    ++count;
                    last = position[i];
                }
            }
            if (count >= m) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return hi;
    }
};

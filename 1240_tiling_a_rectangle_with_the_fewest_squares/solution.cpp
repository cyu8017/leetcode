// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

#include <algorithm>
#include <vector>

class Solution {
public:
    int tilingRectangle(int n, int m) {
        if (n > m) {
            std::swap(n, m);
        }
        std::vector<int> heights(m, 0);
        int best = n * m;
        auto search = [&](auto&& self, int used) -> void {
            if (used >= best) {
                return;
            }
            int low = *std::min_element(heights.begin(), heights.end());
            if (low == n) {
                best = used;
                return;
            }
            int left = 0;
            while (heights[left] != low) {
                ++left;
            }
            int right = left;
            while (right < m && heights[right] == low) {
                ++right;
            }
            int maxSize = std::min(n - low, right - left);
            for (int size = maxSize; size >= 1; --size) {
                for (int i = left; i < left + size; ++i) {
                    heights[i] = low + size;
                }
                self(self, used + 1);
                for (int i = left; i < left + size; ++i) {
                    heights[i] = low;
                }
            }
        };
        search(search, 0);
        return best;
    }
};

#include <algorithm>
#include <vector>

class Solution {
public:
    int minTaps(int n, std::vector<int>& ranges) {
        std::vector<int> farthest(n + 1, 0);
        for (int center = 0; center < (int)ranges.size(); ++center) {
            int left = std::max(0, center - ranges[center]);
            int right = std::min(n, center + ranges[center]);
            farthest[left] = std::max(farthest[left], right);
        }
        int taps = 0, end = 0, reach = 0;
        for (int position = 0; position < n; ++position) {
            reach = std::max(reach, farthest[position]);
            if (position == end) {
                if (reach <= position) return -1;
                ++taps;
                end = reach;
            }
        }
        return taps;
    }
};

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxArea(int h, int w, std::vector<int>& horizontalCuts, std::vector<int>& verticalCuts) {
        horizontalCuts.push_back(0); horizontalCuts.push_back(h);
        verticalCuts.push_back(0); verticalCuts.push_back(w);
        std::sort(horizontalCuts.begin(), horizontalCuts.end());
        std::sort(verticalCuts.begin(), verticalCuts.end());
        long long maxH = 0, maxV = 0;
        for (size_t i = 1; i < horizontalCuts.size(); ++i)
            maxH = std::max(maxH, (long long)horizontalCuts[i] - horizontalCuts[i - 1]);
        for (size_t i = 1; i < verticalCuts.size(); ++i)
            maxV = std::max(maxV, (long long)verticalCuts[i] - verticalCuts[i - 1]);
        return (int)(maxH * maxV % 1000000007);
    }
};

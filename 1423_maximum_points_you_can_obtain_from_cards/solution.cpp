#include <algorithm>
#include <numeric>
#include <vector>

class Solution {
public:
    int maxScore(std::vector<int>& cardPoints, int k) {
        int n = (int)cardPoints.size();
        if (k == n) return std::accumulate(cardPoints.begin(), cardPoints.end(), 0);
        int window = n - k;
        int current = 0;
        for (int i = 0; i < window; ++i) current += cardPoints[i];
        int smallest = current;
        for (int i = window; i < n; ++i) {
            current += cardPoints[i] - cardPoints[i - window];
            smallest = std::min(smallest, current);
        }
        return std::accumulate(cardPoints.begin(), cardPoints.end(), 0) - smallest;
    }
};

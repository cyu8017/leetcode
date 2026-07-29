#include <vector>

class Solution {
public:
    int countNegatives(std::vector<std::vector<int>>& grid) {
        int answer = 0;
        for (auto& row : grid) {
            int lo = 0, hi = (int)row.size();
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (row[mid] < 0) hi = mid;
                else lo = mid + 1;
            }
            answer += (int)row.size() - lo;
        }
        return answer;
    }
};

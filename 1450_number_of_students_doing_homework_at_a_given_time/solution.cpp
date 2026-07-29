#include <vector>

class Solution {
public:
    int busyStudent(std::vector<int>& startTime, std::vector<int>& endTime, int queryTime) {
        int ans = 0;
        for (size_t i = 0; i < startTime.size(); ++i)
            ans += startTime[i] <= queryTime && queryTime <= endTime[i];
        return ans;
    }
};

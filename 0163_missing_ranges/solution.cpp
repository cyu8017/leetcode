// LeetCode 0163 - Missing Ranges
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<vector<int>> result;
        long long prev = (long long)lower - 1;
        for (int i = 0; i <= (int)nums.size(); ++i) {
            long long current = i == nums.size() ? (long long)upper + 1 : nums[i];
            if (current - prev >= 2) result.push_back({(int)(prev + 1), (int)(current - 1)});
            prev = current;
        }
        return result;
    }
};
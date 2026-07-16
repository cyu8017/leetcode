// LeetCode 0164 - Maximum Gap
#include <algorithm>
#include <climits>
#include <vector>
using namespace std;
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.size() < 2) return 0;
        int low = *min_element(nums.begin(), nums.end());
        int high = *max_element(nums.begin(), nums.end());
        if (low == high) return 0;
        int size = max(1, (high - low) / ((int)nums.size() - 1));
        int count = (high - low) / size + 1;
        vector<int> mins(count, INT_MAX), maxs(count, INT_MIN);
        vector<bool> used(count);
        for (int n : nums) {
            int i = (n - low) / size;
            mins[i] = min(mins[i], n); maxs[i] = max(maxs[i], n); used[i] = true;
        }
        int best = 0, previous = low;
        for (int i = 0; i < count; ++i) if (used[i]) {
            best = max(best, mins[i] - previous); previous = maxs[i];
        }
        return best;
    }
};
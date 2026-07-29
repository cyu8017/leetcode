#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minSumOfLengths(std::vector<int>& arr, int target) {
        const int inf = 1e9;
        int left = 0, total = 0, best = inf, ans = inf;
        std::vector<int> shortest(arr.size(), inf);
        for (int right = 0; right < (int)arr.size(); ++right) {
            total += arr[right];
            while (total > target) total -= arr[left++];
            if (total == target) {
                int length = right - left + 1;
                if (left) ans = std::min(ans, length + shortest[left - 1]);
                best = std::min(best, length);
            }
            shortest[right] = best;
        }
        return ans == inf ? -1 : ans;
    }
};

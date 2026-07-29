#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    int findTheDistanceValue(std::vector<int>& arr1, std::vector<int>& arr2, int d) {
        std::sort(arr2.begin(), arr2.end());
        int ans = 0;
        for (int x : arr1) {
            auto it = std::lower_bound(arr2.begin(), arr2.end(), x);
            bool bad = false;
            if (it != arr2.end() && std::abs(*it - x) <= d) bad = true;
            if (it != arr2.begin() && std::abs(*(it - 1) - x) <= d) bad = true;
            if (!bad) ++ans;
        }
        return ans;
    }
};

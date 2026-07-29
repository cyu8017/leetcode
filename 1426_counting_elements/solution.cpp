#include <unordered_set>
#include <vector>

class Solution {
public:
    int countElements(std::vector<int>& arr) {
        std::unordered_set<int> values(arr.begin(), arr.end());
        int ans = 0;
        for (int value : arr) ans += values.count(value + 1);
        return ans;
    }
};

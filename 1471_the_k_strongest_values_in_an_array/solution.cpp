#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<int> getStrongest(std::vector<int>& arr, int k) {
        std::sort(arr.begin(), arr.end());
        int median = arr[(arr.size() - 1) / 2];
        std::sort(arr.begin(), arr.end(), [&](int a, int b) {
            int da = std::abs(a - median), db = std::abs(b - median);
            return da != db ? da > db : a > b;
        });
        arr.resize(k);
        return arr;
    }
};

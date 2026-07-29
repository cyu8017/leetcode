#include <unordered_map>
#include <vector>

class Solution {
public:
    bool canArrange(std::vector<int>& arr, int k) {
        std::unordered_map<int, int> count;
        for (int x : arr) {
            int r = ((x % k) + k) % k;
            ++count[r];
        }
        if (count[0] % 2) return false;
        for (int r = 1; r < k; ++r)
            if (count[r] != count[k - r]) return false;
        return true;
    }
};

#include <unordered_set>
#include <vector>

class Solution {
public:
    bool checkIfExist(std::vector<int>& arr) {
        std::unordered_set<int> seen;
        for (int value : arr) {
            if (seen.count(2 * value) || (value % 2 == 0 && seen.count(value / 2))) return true;
            seen.insert(value);
        }
        return false;
    }
};

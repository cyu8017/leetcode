// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

#include <algorithm>
#include <vector>

class Skiplist {
public:
    Skiplist() = default;

    bool search(int target) {
        return std::binary_search(values.begin(), values.end(), target);
    }

    void add(int num) {
        values.insert(std::upper_bound(values.begin(), values.end(), num), num);
    }

    bool erase(int num) {
        auto it = std::lower_bound(values.begin(), values.end(), num);
        if (it == values.end() || *it != num) {
            return false;
        }
        values.erase(it);
        return true;
    }

private:
    std::vector<int> values;
};

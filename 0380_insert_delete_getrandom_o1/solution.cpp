// LeetCode 0380 - Insert Delete GetRandom O(1)
// https://leetcode.com/problems/insert-delete-getrandom-o1/

#include <cstdlib>
#include <unordered_map>
#include <vector>

class RandomizedSet {
    std::vector<int> values_;
    std::unordered_map<int, int> indexByValue_;

public:
    RandomizedSet() {}

    bool insert(int val) {
        if (indexByValue_.count(val)) {
            return false;
        }
        indexByValue_[val] = static_cast<int>(values_.size());
        values_.push_back(val);
        return true;
    }

    bool remove(int val) {
        if (!indexByValue_.count(val)) {
            return false;
        }

        int index = indexByValue_[val];
        int lastValue = values_.back();
        values_[index] = lastValue;
        indexByValue_[lastValue] = index;
        values_.pop_back();
        indexByValue_.erase(val);
        return true;
    }

    int getRandom() {
        return values_[std::rand() % values_.size()];
    }
};

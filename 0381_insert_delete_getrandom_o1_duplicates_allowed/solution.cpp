// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

#include <unordered_map>
#include <unordered_set>
#include <vector>

class RandomizedCollection {
    std::vector<int> values_;
    std::unordered_map<int, std::unordered_set<int>> indicesByValue_;

public:
    RandomizedCollection() {}

    bool insert(int val) {
        if (!indicesByValue_.count(val)) {
            indicesByValue_[val] = {};
        }
        indicesByValue_[val].insert(static_cast<int>(values_.size()));
        values_.push_back(val);
        return indicesByValue_[val].size() == 1;
    }

    bool remove(int val) {
        if (!indicesByValue_.count(val) || indicesByValue_[val].empty()) {
            return false;
        }

        int index = *indicesByValue_[val].begin();
        int lastIndex = static_cast<int>(values_.size()) - 1;
        int lastValue = values_[lastIndex];
        values_[index] = lastValue;
        indicesByValue_[lastValue].erase(lastIndex);
        indicesByValue_[lastValue].insert(index);
        values_.pop_back();
        indicesByValue_[val].erase(index);
        if (indicesByValue_[val].empty()) {
            indicesByValue_.erase(val);
        }
        return true;
    }

    int getRandom() {
        return values_.back();
    }
};

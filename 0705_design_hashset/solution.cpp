// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

#include <unordered_set>

class MyHashSet {
public:
    MyHashSet() = default;

    void add(int key) { data_.insert(key); }

    void remove(int key) { data_.erase(key); }

    bool contains(int key) { return data_.count(key) > 0; }

private:
    std::unordered_set<int> data_;
};

// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

#include <unordered_map>

class MyHashMap {
public:
    MyHashMap() = default;

    void put(int key, int value) { data_[key] = value; }

    int get(int key) {
        auto it = data_.find(key);
        return it == data_.end() ? -1 : it->second;
    }

    void remove(int key) { data_.erase(key); }

private:
    std::unordered_map<int, int> data_;
};

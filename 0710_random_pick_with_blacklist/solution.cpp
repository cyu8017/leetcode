// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

#include <cstdlib>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    Solution(int n, std::vector<int>& blacklist) {
        size_ = n - static_cast<int>(blacklist.size());
        std::unordered_set<int> black(blacklist.begin(), blacklist.end());
        int white = size_;
        for (int b : blacklist) {
            if (b < size_) {
                while (black.count(white)) {
                    ++white;
                }
                mapping_[b] = white++;
            }
        }
    }

    int pick() {
        int index = std::rand() % size_;
        auto it = mapping_.find(index);
        return it == mapping_.end() ? index : it->second;
    }

private:
    int size_;
    std::unordered_map<int, int> mapping_;
};

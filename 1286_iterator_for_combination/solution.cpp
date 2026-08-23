// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

#include <string>
#include <vector>

class CombinationIterator {
public:
    CombinationIterator(std::string characters, int combinationLength) {
        std::string current;
        auto dfs = [&](auto&& self, int start) -> void {
            if (static_cast<int>(current.size()) == combinationLength) {
                items.push_back(current);
                return;
            }
            for (int i = start; i < static_cast<int>(characters.size()); ++i) {
                current.push_back(characters[i]);
                self(self, i + 1);
                current.pop_back();
            }
        };
        dfs(dfs, 0);
        index = 0;
    }

    std::string next() {
        return items[index++];
    }

    bool hasNext() {
        return index < static_cast<int>(items.size());
    }

private:
    std::vector<std::string> items;
    int index;
};

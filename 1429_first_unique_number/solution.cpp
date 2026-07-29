#include <list>
#include <unordered_map>
#include <vector>

class FirstUnique {
    std::unordered_map<int, int> counts;
    std::list<int> unique;
    std::unordered_map<int, std::list<int>::iterator> pos;
public:
    FirstUnique(std::vector<int>& nums) {
        for (int value : nums) add(value);
    }

    int showFirstUnique() {
        return unique.empty() ? -1 : unique.front();
    }

    void add(int value) {
        ++counts[value];
        if (counts[value] == 1) {
            unique.push_back(value);
            pos[value] = std::prev(unique.end());
        } else if (pos.count(value)) {
            unique.erase(pos[value]);
            pos.erase(value);
        }
    }
};

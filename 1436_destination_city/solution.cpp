#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::string destCity(std::vector<std::vector<std::string>>& paths) {
        std::unordered_set<std::string> starts;
        for (auto& p : paths) starts.insert(p[0]);
        for (auto& p : paths)
            if (!starts.count(p[1])) return p[1];
        return "";
    }
};

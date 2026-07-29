#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<std::string> getFolderNames(std::vector<std::string>& names) {
        std::unordered_map<std::string, int> used;
        std::vector<std::string> ans;
        for (auto& name : names) {
            std::string candidate;
            if (!used.count(name)) candidate = name;
            else {
                int k = used[name];
                while (used.count(name + "(" + std::to_string(k) + ")")) ++k;
                candidate = name + "(" + std::to_string(k) + ")";
                used[name] = k + 1;
            }
            used[candidate] = 1;
            ans.push_back(candidate);
        }
        return ans;
    }
};

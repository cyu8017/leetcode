// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

#include <vector>
#include <string>
#include <map>
#include <set>
#include <sstream>

class Solution {
public:
    // JS array-of-objects-to-matrix stand-in
    std::vector<std::vector<std::string>> jsonToMatrix(std::vector<std::map<std::string, std::string>>& arr) {
        std::set<std::string> keys;
        for (auto& obj : arr) for (auto& [k, _] : obj) keys.insert(k);
        std::vector<std::vector<std::string>> mat;
        mat.push_back(std::vector<std::string>(keys.begin(), keys.end()));
        for (auto& obj : arr) {
            std::vector<std::string> row;
            for (auto& k : keys) {
                auto it = obj.find(k);
                row.push_back(it == obj.end() ? "" : it->second);
            }
            mat.push_back(row);
        }
        return mat;
    }
};

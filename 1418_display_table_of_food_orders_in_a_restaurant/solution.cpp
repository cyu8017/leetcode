#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> displayTable(std::vector<std::vector<std::string>>& orders) {
        std::set<std::string> foodSet;
        std::set<int> tableSet;
        std::map<std::pair<int, std::string>, int> counts;
        for (auto& o : orders) {
            int table = std::stoi(o[1]);
            foodSet.insert(o[2]);
            tableSet.insert(table);
            ++counts[{table, o[2]}];
        }
        std::vector<std::string> foods(foodSet.begin(), foodSet.end());
        std::vector<std::vector<std::string>> answer;
        answer.push_back({"Table"});
        answer[0].insert(answer[0].end(), foods.begin(), foods.end());
        for (int table : tableSet) {
            std::vector<std::string> row{std::to_string(table)};
            for (auto& food : foods) row.push_back(std::to_string(counts[{table, food}]));
            answer.push_back(row);
        }
        return answer;
    }
};

// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

#include <string>
#include <unordered_map>
#include <vector>

class SQL {
public:
    SQL(std::vector<std::string>& names, std::vector<int>& columns) {
        for (auto& name : names) {
            tables[name] = {};
            nextID[name] = 1;
        }
    }

    bool ins(std::string name, std::vector<std::string> row) {
        if (!tables.count(name)) return false;
        int id = nextID[name]++;
        std::vector<std::string> full;
        full.push_back(std::to_string(id));
        full.insert(full.end(), row.begin(), row.end());
        tables[name].push_back(std::move(full));
        return true;
    }

    void rmv(std::string name, int rowId) {
        auto& rows = tables[name];
        for (auto it = rows.begin(); it != rows.end(); ++it) {
            if (std::stoi((*it)[0]) == rowId) {
                rows.erase(it);
                return;
            }
        }
    }

    std::string sel(std::string name, int rowId, int columnId) {
        for (auto& r : tables[name]) {
            if (std::stoi(r[0]) == rowId) {
                if (columnId < 1 || columnId >= (int)r.size()) return "<null>";
                return r[columnId];
            }
        }
        return "<null>";
    }

    std::vector<std::string> exp(std::string name) {
        std::vector<std::string> ans;
        for (auto& r : tables[name]) {
            std::string s = r[0];
            for (int j = 1; j < (int)r.size(); j++) s += "," + r[j];
            ans.push_back(s);
        }
        return ans;
    }

private:
    std::unordered_map<std::string, std::vector<std::vector<std::string>>> tables;
    std::unordered_map<std::string, int> nextID;
};

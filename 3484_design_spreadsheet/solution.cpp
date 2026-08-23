// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

#include <string>
#include <unordered_map>

class Spreadsheet {
    std::unordered_map<std::string, int> cells;
public:
    Spreadsheet(int rows) {}

    void setCell(std::string cell, int value) { cells[cell] = value; }

    void resetCell(std::string cell) { cells.erase(cell); }

    int getValue(std::string formula) {
        if (!formula.empty() && formula[0] == '=') formula = formula.substr(1);
        int sum = 0;
        size_t start = 0;
        while (start < formula.size()) {
            size_t plus = formula.find('+', start);
            std::string p = formula.substr(start, plus == std::string::npos ? std::string::npos : plus - start);
            bool isNum = !p.empty() && (isdigit(p[0]) || (p[0] == '-' && p.size() > 1));
            if (isNum) {
                for (size_t i = 1; i < p.size(); i++) if (!isdigit(p[i])) { isNum = false; break; }
            }
            if (isNum) sum += std::stoi(p);
            else sum += cells[p];
            if (plus == std::string::npos) break;
            start = plus + 1;
        }
        return sum;
    }
};

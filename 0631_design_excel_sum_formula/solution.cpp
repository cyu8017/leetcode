// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

#include <map>
#include <string>
#include <utility>
#include <vector>

class Excel {
    int height_;
    int width_;
    std::vector<std::vector<int>> values_;
    std::map<std::pair<int, int>, std::vector<std::pair<int, int>>> formulas_;

    std::pair<int, int> parse(const std::string& cell) {
        return {std::stoi(cell.substr(1)), cell[0] - 'A'};
    }

    int eval(int row, int col) {
        const auto key = std::make_pair(row, col);
        if (formulas_.count(key)) {
            int total = 0;
            for (const auto& [r, c] : formulas_[key]) {
                total += eval(r, c);
            }
            return total;
        }
        return values_[row][col];
    }

public:
    Excel(int height, char width)
        : height_(height),
          width_(width - 'A' + 1),
          values_(height + 1, std::vector<int>(width - 'A' + 1, 0)) {}

    void set(int row, char column, int val) {
        const int col = column - 'A';
        formulas_.erase({row, col});
        values_[row][col] = val;
    }

    int get(int row, char column) { return eval(row, column - 'A'); }

    int sum(int row, char column, std::vector<std::string> numbers) {
        const int col = column - 'A';
        std::vector<std::pair<int, int>> cells;
        for (const std::string& token : numbers) {
            const auto colon = token.find(':');
            if (colon != std::string::npos) {
                auto [r1, c1] = parse(token.substr(0, colon));
                auto [r2, c2] = parse(token.substr(colon + 1));
                for (int r = r1; r <= r2; ++r) {
                    for (int c = c1; c <= c2; ++c) {
                        cells.emplace_back(r, c);
                    }
                }
            } else {
                cells.push_back(parse(token));
            }
        }
        formulas_[{row, col}] = cells;
        return eval(row, col);
    }
};

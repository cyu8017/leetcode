#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool isSolvable(std::vector<std::string>& words, std::string result) {
        int maxWord = 0;
        for (auto& w : words) maxWord = std::max(maxWord, (int)w.size());
        if (maxWord > (int)result.size()) return false;
        std::string all;
        for (auto& w : words) all += w;
        all += result;
        std::unordered_set<char> uniq(all.begin(), all.end());
        if (uniq.size() > 10) return false;
        std::unordered_set<char> leading;
        for (auto& w : words) if (w.size() > 1) leading.insert(w[0]);
        if (result.size() > 1) leading.insert(result[0]);
        std::unordered_map<char, int> value;
        std::vector<bool> used(10, false);
        int width = (int)result.size();
        auto solve = [&](auto&& self, int column, int row, int total) -> bool {
            if (column == width) return total == 0;
            if (row < (int)words.size()) {
                if (column >= (int)words[row].size()) return self(self, column, row + 1, total);
                char ch = words[row][words[row].size() - 1 - column];
                if (value.count(ch)) return self(self, column, row + 1, total + value[ch]);
                for (int digit = 0; digit < 10; ++digit) {
                    if (!used[digit] && (digit || !leading.count(ch))) {
                        value[ch] = digit; used[digit] = true;
                        if (self(self, column, row + 1, total + digit)) return true;
                        used[digit] = false; value.erase(ch);
                    }
                }
                return false;
            }
            char ch = result[result.size() - 1 - column];
            int digit = total % 10;
            int carry = total / 10;
            if (value.count(ch)) return value[ch] == digit && self(self, column + 1, 0, carry);
            if (used[digit] || (digit == 0 && leading.count(ch))) return false;
            value[ch] = digit; used[digit] = true;
            bool ok = self(self, column + 1, 0, carry);
            used[digit] = false; value.erase(ch);
            return ok;
        };
        return solve(solve, 0, 0, 0);
    }
};

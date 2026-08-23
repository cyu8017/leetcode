// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

#include <string>
#include <sstream>
#include <vector>
#include <iomanip>

class Solution {
public:
    std::string discountPrices(std::string sentence, int discount) {
        std::istringstream iss(sentence);
        std::vector<std::string> parts;
        std::string p;
        while (iss >> p) parts.push_back(p);
        for (auto& part : parts) {
            if (part.size() >= 2 && part[0] == '$') {
                bool ok = true;
                for (size_t j = 1; j < part.size(); ++j)
                    if (part[j] < '0' || part[j] > '9') { ok = false; break; }
                if (ok) {
                    long long val = std::stoll(part.substr(1));
                    double price = val * (100.0 - discount) / 100.0;
                    std::ostringstream oss;
                    oss << '$' << std::fixed << std::setprecision(2) << price;
                    part = oss.str();
                }
            }
        }
        std::string out;
        for (size_t i = 0; i < parts.size(); ++i) {
            if (i) out += ' ';
            out += parts[i];
        }
        return out;
    }
};

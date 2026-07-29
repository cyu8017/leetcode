// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

#include <cmath>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<std::string> invalidTransactions(std::vector<std::string>& transactions) {
        struct Tx { std::string name, city, raw; int time, amount; };
        std::vector<Tx> parsed;
        for (const auto& t : transactions) {
            std::stringstream ss(t);
            std::string name, timeStr, amountStr, city;
            std::getline(ss, name, ',');
            std::getline(ss, timeStr, ',');
            std::getline(ss, amountStr, ',');
            std::getline(ss, city, ',');
            parsed.push_back({name, city, t, std::stoi(timeStr), std::stoi(amountStr)});
        }
        std::unordered_set<std::string> invalid;
        for (int i = 0; i < static_cast<int>(parsed.size()); ++i) {
            if (parsed[i].amount > 1000) invalid.insert(parsed[i].raw);
            for (int j = 0; j < static_cast<int>(parsed.size()); ++j) {
                if (i != j && parsed[i].name == parsed[j].name && parsed[i].city != parsed[j].city &&
                    std::abs(parsed[i].time - parsed[j].time) <= 60) {
                    invalid.insert(parsed[i].raw);
                    invalid.insert(parsed[j].raw);
                }
            }
        }
        return std::vector<std::string>(invalid.begin(), invalid.end());
    }
};

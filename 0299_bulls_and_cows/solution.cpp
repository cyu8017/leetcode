// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

#include <string>
#include <unordered_map>

class Solution {
public:
    std::string getHint(std::string secret, std::string guess) {
        int bulls = 0;
        std::unordered_map<char, int> secretCounts;
        std::unordered_map<char, int> guessCounts;

        for (size_t index = 0; index < secret.size(); index++) {
            if (secret[index] == guess[index]) {
                bulls++;
            } else {
                secretCounts[secret[index]]++;
                guessCounts[guess[index]]++;
            }
        }

        int cows = 0;
        for (const auto& entry : guessCounts) {
            auto iterator = secretCounts.find(entry.first);
            if (iterator != secretCounts.end()) {
                cows += std::min(entry.second, iterator->second);
            }
        }

        return std::to_string(bulls) + "A" + std::to_string(cows) + "B";
    }
};

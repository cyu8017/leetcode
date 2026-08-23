// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

#include <string>
#include <vector>

class Solution {
public:
    std::string numberToWords(int num) {
        if (num == 0) {
            return "Zero";
        }

        std::vector<std::string> parts;
        int chunkIndex = 0;
        while (num > 0) {
            int chunk = num % 1000;
            if (chunk != 0) {
                std::string chunkWords = convertChunk(chunk);
                if (!thousands[chunkIndex].empty()) {
                    chunkWords += " " + thousands[chunkIndex];
                }
                parts.push_back(chunkWords);
            }
            num /= 1000;
            chunkIndex++;
        }

        std::string result;
        for (int i = static_cast<int>(parts.size()) - 1; i >= 0; i--) {
            if (!result.empty()) {
                result += " ";
            }
            result += parts[i];
        }
        return result;
    }

private:
    const std::vector<std::string> ones = {
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen"
    };
    const std::vector<std::string> tens = {
        "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    };
    const std::vector<std::string> thousands = {"", "Thousand", "Million", "Billion"};

    std::string convertChunk(int value) {
        if (value == 0) {
            return "";
        }
        if (value < 20) {
            return ones[value];
        }
        if (value < 100) {
            std::string tensPart = tens[value / 10];
            std::string onesPart = ones[value % 10];
            return onesPart.empty() ? tensPart : tensPart + " " + onesPart;
        }
        std::string hundreds = ones[value / 100];
        std::string remainder = convertChunk(value % 100);
        return remainder.empty() ? hundreds + " Hundred" : hundreds + " Hundred " + remainder;
    }
};

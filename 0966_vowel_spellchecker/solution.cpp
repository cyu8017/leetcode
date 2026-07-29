// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

#include <cctype>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<std::string> spellchecker(std::vector<std::string>& wordlist, std::vector<std::string>& queries) {
        auto lower = [](std::string w) {
            for (char& c : w) c = (char)std::tolower(static_cast<unsigned char>(c));
            return w;
        };
        auto devowel = [&](std::string w) {
            w = lower(w);
            for (char& c : w) {
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') c = '*';
            }
            return w;
        };
        std::unordered_set<std::string> exact(wordlist.begin(), wordlist.end());
        std::unordered_map<std::string, std::string> lowerMap, vowelMap;
        for (const auto& w : wordlist) {
            std::string low = lower(w);
            if (!lowerMap.count(low)) lowerMap[low] = w;
            std::string dv = devowel(w);
            if (!vowelMap.count(dv)) vowelMap[dv] = w;
        }
        std::vector<std::string> ans;
        for (const auto& q : queries) {
            if (exact.count(q)) ans.push_back(q);
            else if (lowerMap.count(lower(q))) ans.push_back(lowerMap[lower(q)]);
            else if (vowelMap.count(devowel(q))) ans.push_back(vowelMap[devowel(q)]);
            else ans.push_back("");
        }
        return ans;
    }
};

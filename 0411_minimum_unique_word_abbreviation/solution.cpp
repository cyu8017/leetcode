// LeetCode 0411 - Minimum Unique Word Abbreviation
// https://leetcode.com/problems/minimum-unique-word-abbreviation/

#include <cctype>
#include <functional>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string minAbbreviation(string target, vector<string>& dictionary) {
        vector<string> words;
        for (const string& word : dictionary) {
            if (word.size() == target.size()) {
                words.push_back(word);
            }
        }

        int bestLen = (int)target.size() + 1;
        string result = target;

        auto matches = [](const string& word, const string& abbr) -> bool {
            int index = 0;
            int pointer = 0;
            while (index < (int)word.size() && pointer < (int)abbr.size()) {
                if (isdigit(abbr[pointer])) {
                    if (abbr[pointer] == '0') {
                        return false;
                    }
                    int number = 0;
                    while (pointer < (int)abbr.size() && isdigit(abbr[pointer])) {
                        number = number * 10 + (abbr[pointer] - '0');
                        ++pointer;
                    }
                    index += number;
                } else {
                    if (index >= (int)word.size() || word[index] != abbr[pointer]) {
                        return false;
                    }
                    ++index;
                    ++pointer;
                }
            }
            return index == (int)word.size() && pointer == (int)abbr.size();
        };

        auto valid = [&](const string& abbr) -> bool {
            if (!matches(target, abbr)) {
                return false;
            }
            for (const string& word : words) {
                if (matches(word, abbr)) {
                    return false;
                }
            }
            return true;
        };

        function<void(int, vector<string>, int)> dfs = [&](int index, vector<string> parts, int skip) {
            if (index == (int)target.size()) {
                string abbr;
                for (const string& part : parts) {
                    abbr += part;
                }
                if (skip) {
                    abbr += to_string(skip);
                }
                if (valid(abbr)) {
                    if ((int)abbr.size() < bestLen ||
                        ((int)abbr.size() == bestLen && abbr < result)) {
                        bestLen = (int)abbr.size();
                        result = abbr;
                    }
                }
                return;
            }

            dfs(index + 1, parts, skip + 1);

            vector<string> newParts = parts;
            if (skip) {
                newParts.push_back(to_string(skip));
            }
            newParts.push_back(string(1, target[index]));
            dfs(index + 1, newParts, 0);
        };

        dfs(0, {}, 0);
        return result;
    }
};

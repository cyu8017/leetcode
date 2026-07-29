// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

#include <string>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int uniqueMorseRepresentations(std::vector<std::string>& words) {
        static const char* codes[] = {
            ".-",   "-...", "-.-.", "-..",  ".",   "..-.", "--.",  "....",
            "..",   ".---", "-.-",  ".-..", "--",  "-.",   "---",  ".--.",
            "--.-", ".-.",  "...",  "-",    "..-", "...-", ".--",  "-..-",
            "-.--", "--.."};
        std::unordered_set<std::string> seen;
        for (const auto& word : words) {
            std::string code;
            for (char ch : word) {
                code += codes[ch - 'a'];
            }
            seen.insert(code);
        }
        return static_cast<int>(seen.size());
    }
};

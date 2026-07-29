#include <sstream>
#include <string>

class Solution {
public:
    int isPrefixOfWord(std::string sentence, std::string searchWord) {
        std::istringstream iss(sentence);
        std::string w;
        int i = 1;
        while (iss >> w) {
            if (w.compare(0, searchWord.size(), searchWord) == 0) return i;
            ++i;
        }
        return -1;
    }
};

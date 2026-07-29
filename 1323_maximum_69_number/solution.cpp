#include <string>

class Solution {
public:
    int maximum69Number(int num) {
        std::string s = std::to_string(num);
        for (char& ch : s) {
            if (ch == '6') { ch = '9'; break; }
        }
        return std::stoi(s);
    }
};

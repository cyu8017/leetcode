#include <string>

class Solution {
public:
    int maxDiff(int num) {
        std::string s = std::to_string(num);
        std::string high = s;
        for (char ch : s) {
            if (ch != '9') {
                for (char& c : high) if (c == ch) c = '9';
                break;
            }
        }
        std::string low = s;
        if (s[0] != '1') {
            char ch = s[0];
            for (char& c : low) if (c == ch) c = '1';
        } else {
            for (size_t i = 1; i < s.size(); ++i) {
                if (s[i] != '0' && s[i] != '1') {
                    char ch = s[i];
                    for (char& c : low) if (c == ch) c = '0';
                    break;
                }
            }
        }
        return std::stoi(high) - std::stoi(low);
    }
};

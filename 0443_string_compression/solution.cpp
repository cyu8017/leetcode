// LeetCode 0443 - String Compression
// https://leetcode.com/problems/string-compression/

#include <string>
#include <vector>

class Solution {
public:
    int compress(std::vector<char>& chars) {
        int write = 0;
        int read = 0;
        while (read < static_cast<int>(chars.size())) {
            char ch = chars[read];
            int count = 0;
            while (read < static_cast<int>(chars.size()) && chars[read] == ch) {
                ++read;
                ++count;
            }
            chars[write++] = ch;
            if (count > 1) {
                for (char digit : std::to_string(count)) {
                    chars[write++] = digit;
                }
            }
        }
        return write;
    }
};

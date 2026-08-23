// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

#include <string>
#include <vector>

class Codec {
public:
    std::string encode(std::vector<std::string>& strs) {
        std::string encoded;
        for (const std::string& text : strs) {
            encoded += std::to_string(text.size());
            encoded.push_back('#');
            encoded += text;
        }
        return encoded;
    }

    std::vector<std::string> decode(std::string encoded) {
        std::vector<std::string> result;
        size_t index = 0;
        while (index < encoded.size()) {
            size_t delimiter = encoded.find('#', index);
            int length = std::stoi(encoded.substr(index, delimiter - index));
            size_t start = delimiter + 1;
            result.push_back(encoded.substr(start, length));
            index = start + length;
        }
        return result;
    }
};

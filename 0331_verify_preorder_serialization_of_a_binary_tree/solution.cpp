// LeetCode 0331 - Verify Preorder Serialization of a Binary Tree
// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

#include <string>

class Solution {
public:
    bool isValidSerialization(const std::string& preorder) {
        int slots = 1;
        size_t start = 0;
        while (start <= preorder.size()) {
            size_t end = preorder.find(',', start);
            std::string node = preorder.substr(start, end - start);
            slots -= 1;
            if (slots < 0) {
                return false;
            }
            if (node != "#") {
                slots += 2;
            }
            if (end == std::string::npos) {
                break;
            }
            start = end + 1;
        }
        return slots == 0;
    }
};

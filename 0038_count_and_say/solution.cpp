// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

#include <string>

class Solution {
public:
    std::string countAndSay(int n) {
        std::string term = "1";

        for (int i = 1; i < n; i++) {
            std::string nextTerm;
            int index = 0;
            while (index < static_cast<int>(term.size())) {
                int count = 1;
                while (index + count < static_cast<int>(term.size()) && term[index + count] == term[index]) {
                    count++;
                }
                nextTerm.push_back(static_cast<char>('0' + count));
                nextTerm.push_back(term[index]);
                index += count;
            }
            term = nextTerm;
        }

        return term;
    }
};

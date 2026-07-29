// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

#include <string>

class Solution {
public:
    std::string strWithout3a3b(int a, int b) {
        std::string ans;
        while (a || b) {
            bool writeA;
            if (ans.size() >= 2 && ans[ans.size() - 1] == ans[ans.size() - 2])
                writeA = ans.back() == 'b';
            else
                writeA = a >= b;
            if (writeA) {
                ans.push_back('a');
                a--;
            } else {
                ans.push_back('b');
                b--;
            }
        }
        return ans;
    }
};

// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> twoEditWords(std::vector<std::string>& queries, std::vector<std::string>& dictionary) {
        std::vector<std::string> ans;
        for (auto& q : queries) {
            bool ok = false;
            for (auto& d : dictionary) {
                int diff = 0;
                for (int i = 0; i < (int)q.size(); i++) {
                    if (q[i] != d[i]) {
                        if (++diff > 2) break;
                    }
                }
                if (diff <= 2) {
                    ok = true;
                    break;
                }
            }
            if (ok) ans.push_back(q);
        }
        return ans;
    }
};

// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

#include <queue>
#include <string>
#include <unordered_set>

class Solution {
public:
    std::string findLexSmallestString(std::string s, int a, int b) {
        std::unordered_set<std::string> seen{s};
        std::queue<std::string> q;
        q.push(s);
        std::string ans = s;
        while (!q.empty()) {
            std::string cur = q.front();
            q.pop();
            ans = std::min(ans, cur);
            std::string add = cur;
            for (int i = 1; i < static_cast<int>(add.size()); i += 2) {
                add[i] = static_cast<char>('0' + (add[i] - '0' + a) % 10);
            }
            std::string rot = cur.substr(cur.size() - b) + cur.substr(0, cur.size() - b);
            for (const auto& nxt : {add, rot}) {
                if (!seen.count(nxt)) {
                    seen.insert(nxt);
                    q.push(nxt);
                }
            }
        }
        return ans;
    }
};

// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

#include <string>
#include <unordered_map>

class Solution {
public:
    std::string mergeCharacters(std::string s, int k) {
        std::unordered_map<char, int> last;
        std::string ans;
        for (char c : s) {
            int cur = (int)ans.size();
            auto it = last.find(c);
            if (it != last.end() && cur - it->second <= k) continue;
            ans.push_back(c);
            last[c] = cur;
        }
        return ans;
    }
};

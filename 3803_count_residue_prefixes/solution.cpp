// LeetCode 3803 - Count Residue Prefixes
// https://leetcode.com/problems/count-residue-prefixes/

#include <string>
#include <unordered_set>

class Solution {
public:
    int residuePrefixes(std::string s) {
        std::unordered_set<char> st;
        int ans = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            st.insert(s[i]);
            if ((int)st.size() == (i + 1) % 3) ans++;
        }
        return ans;
    }
};

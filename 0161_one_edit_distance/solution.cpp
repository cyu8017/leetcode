// LeetCode 0161 - One Edit Distance
#include <string>
using namespace std;
class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        if (s.size() > t.size()) swap(s, t);
        if (t.size() - s.size() > 1 || s == t) return false;
        size_t i = 0;
        while (i < s.size() && s[i] == t[i]) ++i;
        return s.size() == t.size() ? s.substr(i + 1) == t.substr(i + 1)
                                    : s.substr(i) == t.substr(i + 1);
    }
};
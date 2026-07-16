// LeetCode 0205 - Isomorphic Strings
#include <string>
#include <vector>
class Solution { public: bool isIsomorphic(std::string s, std::string t) { std::vector<int> mapS(256, -1), mapT(256, -1); for (size_t i = 0; i < s.size(); ++i) { unsigned char a = s[i], b = t[i]; if ((mapS[a] != -1 && mapS[a] != b) || (mapT[b] != -1 && mapT[b] != a)) return false; mapS[a] = b; mapT[b] = a; } return true; } };

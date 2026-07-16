// LeetCode 0131 - Palindrome Partitioning
#include <string>
#include <vector>
using namespace std;

class Solution {
    vector<vector<string>> result;
    vector<string> path;
    bool palindrome(const string& s, int left, int right) {
        while (left < right) if (s[left++] != s[right--]) return false;
        return true;
    }
    void dfs(const string& s, int start) {
        if (start == s.size()) { result.push_back(path); return; }
        for (int end = start; end < s.size(); ++end) {
            if (palindrome(s, start, end)) {
                path.push_back(s.substr(start, end - start + 1));
                dfs(s, end + 1);
                path.pop_back();
            }
        }
    }
public:
    vector<vector<string>> partition(string s) {
        dfs(s, 0);
        return result;
    }
};
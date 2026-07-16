// LeetCode 0140 - Word Break II
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
class Solution {
    unordered_set<string> words;
    unordered_map<int, vector<string>> memo;
    vector<string> dfs(const string& s, int start) {
        if (memo.count(start)) return memo[start];
        vector<string> result;
        if (start == s.size()) result.push_back("");
        for (int end = start + 1; end <= s.size(); ++end) {
            string word = s.substr(start, end - start);
            if (!words.count(word)) continue;
            for (const string& tail : dfs(s, end)) result.push_back(tail.empty() ? word : word + " " + tail);
        }
        return memo[start] = result;
    }
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        words = {wordDict.begin(), wordDict.end()}; memo.clear(); return dfs(s, 0);
    }
};
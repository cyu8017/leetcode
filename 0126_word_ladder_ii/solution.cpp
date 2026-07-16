// LeetCode 0126 - Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/

#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <algorithm>
class Solution {
    std::vector<std::vector<std::string>> result;
    void build(const std::string& word, const std::string& begin, std::unordered_map<std::string, std::vector<std::string>>& parents, std::vector<std::string>& path) {
        if (word == begin) { result.emplace_back(path.rbegin(), path.rend()); return; }
        for (const std::string& parent : parents[word]) { path.push_back(parent); build(parent, begin, parents, path); path.pop_back(); }
    }
public:
    std::vector<std::vector<std::string>> findLadders(std::string beginWord, std::string endWord, std::vector<std::string>& wordList) {
        std::unordered_set<std::string> words(wordList.begin(), wordList.end());
        if (!words.count(endWord)) return {};
        std::unordered_map<std::string, std::vector<std::string>> parents;
        std::queue<std::string> queue; queue.push(beginWord);
        std::unordered_set<std::string> seen{beginWord}; bool found = false;
        while (!queue.empty() && !found) {
            int count = queue.size(); std::unordered_set<std::string> level;
            while (count--) { std::string current = queue.front(); queue.pop();
                std::string next = current;
                for (int i = 0; i < (int)next.size(); ++i) { char saved = next[i];
                    for (char c = 'a'; c <= 'z'; ++c) { next[i] = c;
                        if (!words.count(next) || seen.count(next)) continue;
                        if (level.insert(next).second) queue.push(next);
                        parents[next].push_back(current);
                    } next[i] = saved;
                }
            }
            seen.insert(level.begin(), level.end());
            found = level.count(endWord);
        }
        if (!found) return {};
        std::vector<std::string> path{endWord}; build(endWord, beginWord, parents, path);
        std::sort(result.begin(), result.end());
        return result;
    }
};
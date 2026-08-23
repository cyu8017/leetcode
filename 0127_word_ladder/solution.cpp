// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

#include <string>
#include <vector>
#include <unordered_set>
#include <queue>
class Solution { public: int ladderLength(std::string beginWord, std::string endWord, std::vector<std::string>& wordList) {
    std::unordered_set<std::string> words(wordList.begin(), wordList.end()), seen{beginWord};
    if (!words.count(endWord)) return 0;
    std::queue<std::pair<std::string, int>> queue; queue.push({beginWord, 1});
    while (!queue.empty()) { auto [word, steps] = queue.front(); queue.pop();
        if (word == endWord) return steps;
        for (int i = 0; i < (int)word.size(); ++i) { char saved = word[i];
            for (char c = 'a'; c <= 'z'; ++c) { word[i] = c; if (words.count(word) && seen.insert(word).second) queue.push({word, steps + 1}); }
            word[i] = saved;
        }
    } return 0;
} };
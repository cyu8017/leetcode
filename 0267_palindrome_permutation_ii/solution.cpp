// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

#include <algorithm>
#include <functional>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> generatePalindromes(string s) {
        unordered_map<char, int> counts;
        for (char ch : s) {
            counts[ch]++;
        }

        string middle = "";
        vector<char> oddChars;
        for (const auto& entry : counts) {
            if (entry.second % 2 != 0) {
                oddChars.push_back(entry.first);
            }
        }
        if (oddChars.size() > 1) {
            return {};
        }
        if (oddChars.size() == 1) {
            middle = string(1, oddChars[0]);
        }

        vector<char> keys;
        keys.reserve(counts.size());
        for (const auto& entry : counts) {
            keys.push_back(entry.first);
        }
        sort(keys.begin(), keys.end());

        vector<char> half;
        for (char ch : keys) {
            for (int i = 0; i < counts[ch] / 2; i++) {
                half.push_back(ch);
            }
        }

        vector<string> result;
        vector<bool> used(half.size(), false);
        vector<char> path;

        function<void()> backtrack = [&]() {
            if (path.size() == half.size()) {
                string prefix(path.begin(), path.end());
                string reversed = prefix;
                reverse(reversed.begin(), reversed.end());
                result.push_back(prefix + middle + reversed);
                return;
            }
            for (size_t index = 0; index < half.size(); index++) {
                if (used[index]) {
                    continue;
                }
                if (index > 0 && half[index] == half[index - 1] && !used[index - 1]) {
                    continue;
                }
                used[index] = true;
                path.push_back(half[index]);
                backtrack();
                path.pop_back();
                used[index] = false;
            }
        };

        backtrack();
        return result;
    }
};

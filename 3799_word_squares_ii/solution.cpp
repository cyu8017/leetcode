// LeetCode 3799 - Word Squares Ii
// https://leetcode.com/problems/word-squares-ii/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> wordSquares(std::vector<std::string>& words) {
        std::sort(words.begin(), words.end());
        int n = (int)words.size();
        std::vector<std::vector<std::string>> ans;
        for (int i = 0; i < n; i++) {
            const std::string& top = words[i];
            for (int j = 0; j < n; j++) {
                if (j == i) continue;
                const std::string& left = words[j];
                for (int k = 0; k < n; k++) {
                    if (k == j || k == i) continue;
                    const std::string& right = words[k];
                    for (int h = 0; h < n; h++) {
                        if (h == k || h == j || h == i) continue;
                        const std::string& bottom = words[h];
                        if (top[0] == left[0] && top[3] == right[0] &&
                            bottom[0] == left[3] && bottom[3] == right[3]) {
                            ans.push_back({top, left, right, bottom});
                        }
                    }
                }
            }
        }
        return ans;
    }
};

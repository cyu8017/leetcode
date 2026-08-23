// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::vector<std::string>> suggestedProducts(std::vector<std::string>& products,
                                                            std::string searchWord) {
        std::sort(products.begin(), products.end());
        std::vector<std::vector<std::string>> answer;
        std::string prefix;
        for (char ch : searchWord) {
            prefix.push_back(ch);
            auto it = std::lower_bound(products.begin(), products.end(), prefix);
            std::vector<std::string> suggestions;
            for (int i = 0; i < 3 && it + i != products.end(); ++i) {
                const std::string& p = *(it + i);
                if (p.compare(0, prefix.size(), prefix) == 0) {
                    suggestions.push_back(p);
                }
            }
            answer.push_back(suggestions);
        }
        return answer;
    }
};

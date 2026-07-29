// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

#include <unordered_map>
#include <vector>

class Solution {
public:
    int totalFruit(std::vector<int>& fruits) {
        std::unordered_map<int, int> count;
        int left = 0, ans = 0;
        for (int right = 0; right < (int)fruits.size(); right++) {
            count[fruits[right]]++;
            while ((int)count.size() > 2) {
                if (--count[fruits[left]] == 0) count.erase(fruits[left]);
                left++;
            }
            ans = std::max(ans, right - left + 1);
        }
        return ans;
    }
};

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
        int maximum = *std::max_element(candies.begin(), candies.end());
        std::vector<bool> answer;
        for (int value : candies) answer.push_back(value + extraCandies >= maximum);
        return answer;
    }
};

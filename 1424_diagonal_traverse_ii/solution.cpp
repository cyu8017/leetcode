#include <map>
#include <vector>

class Solution {
public:
    std::vector<int> findDiagonalOrder(std::vector<std::vector<int>>& nums) {
        std::map<int, std::vector<int>> diagonals;
        for (int row = 0; row < (int)nums.size(); ++row)
            for (int col = 0; col < (int)nums[row].size(); ++col)
                diagonals[row + col].push_back(nums[row][col]);
        std::vector<int> answer;
        for (auto& [_, vals] : diagonals)
            for (auto it = vals.rbegin(); it != vals.rend(); ++it)
                answer.push_back(*it);
        return answer;
    }
};

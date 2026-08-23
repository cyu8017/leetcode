// LeetCode 2545 - Sort the Students by Their Kth Score
// https://leetcode.com/problems/sort-the-students-by-their-kth-score/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> sortTheStudents(std::vector<std::vector<int>>& score, int k) {
        std::sort(score.begin(), score.end(), [k](const auto& a, const auto& b) {
            return a[k] > b[k];
        });
        return score;
    }
};

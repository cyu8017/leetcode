// LeetCode 0119 - Pascal's Triangle II
#include <vector>
class Solution { public: std::vector<int> getRow(int rowIndex) {
    std::vector<int> row(rowIndex + 1, 1);
    for (int i = 2; i <= rowIndex; ++i)
        for (int j = i - 1; j; --j) row[j] += row[j - 1];
    return row;
} };
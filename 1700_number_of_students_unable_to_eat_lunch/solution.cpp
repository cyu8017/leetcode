// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

#include <vector>

class Solution {
public:
    int countStudents(std::vector<int>& students, std::vector<int>& sandwiches) {
        int c[2] = {0, 0};
        for (int x : students) c[x]++;
        for (int i = 0; i < (int)sandwiches.size(); i++) {
            if (c[sandwiches[i]] == 0) return (int)students.size() - i;
            c[sandwiches[i]]--;
        }
        return 0;
    }
};

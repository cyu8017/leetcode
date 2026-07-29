// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

int countStudents(int* students, int studentsSize, int* sandwiches, int sandwichesSize) {
    int c[2] = {0, 0};
    for (int i = 0; i < studentsSize; i++) c[students[i]]++;
    for (int i = 0; i < sandwichesSize; i++) {
        if (c[sandwiches[i]] == 0) return studentsSize - i;
        c[sandwiches[i]]--;
    }
    return 0;
}

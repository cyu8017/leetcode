// LeetCode 1450 - Number of Students Doing Homework at a Given Time
// https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

int busyStudent(int* startTime, int startTimeSize, int* endTime, int endTimeSize, int queryTime) {
    (void)endTimeSize;
    int ans = 0;
    for (int i = 0; i < startTimeSize; i++)
        if (startTime[i] <= queryTime && queryTime <= endTime[i]) ans++;
    return ans;
}

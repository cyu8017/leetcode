// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

int numberOfEmployeesWhoMetTarget(int* hours, int hoursSize, int target) {
    int ans = 0;
    for (int i = 0; i < hoursSize; i++) {
        if (hours[i] >= target) ans++;
    }
    return ans;
}

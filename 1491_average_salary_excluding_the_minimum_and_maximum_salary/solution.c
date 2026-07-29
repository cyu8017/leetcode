// LeetCode 1491 - Average Salary Excluding the Minimum and Maximum Salary
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

double average(int* salary, int salarySize) {
    int mn = salary[0], mx = salary[0], sum = 0;
    for (int i = 0; i < salarySize; i++) {
        sum += salary[i];
        if (salary[i] < mn) mn = salary[i];
        if (salary[i] > mx) mx = salary[i];
    }
    return (double)(sum - mn - mx) / (salarySize - 2);
}

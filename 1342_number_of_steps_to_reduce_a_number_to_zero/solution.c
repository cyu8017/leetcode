// LeetCode 1342 - Number of Steps to Reduce a Number to Zero
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

int numberOfSteps(int num) {
    int steps = 0;
    while (num) {
        num = (num % 2 == 0) ? num / 2 : num - 1;
        steps++;
    }
    return steps;
}

// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

int reachNumber(int target) {
    if (target < 0) target = -target;
    int steps = 0;
    long long sum = 0;
    while (sum < target || (sum - target) % 2 != 0) {
        steps++;
        sum += steps;
    }
    return steps;
}

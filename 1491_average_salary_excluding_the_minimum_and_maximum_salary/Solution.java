// LeetCode 1491 - Average Salary Excluding The Minimum And Maximum Salary
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution {
    public double average(int[] salary) {
        int sum = 0, min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int x : salary) {
            sum += x;
            min = Math.min(min, x);
            max = Math.max(max, x);
        }
        return (sum - min - max) / (double) (salary.length - 2);
    }
}

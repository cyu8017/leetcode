// LeetCode 1491 - Average Salary Excluding The Minimum And Maximum Salary
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

using System.Linq;
public class Solution {
    public double Average(int[] salary) {
        return (salary.Sum() - salary.Min() - salary.Max()) / (double)(salary.Length - 2);
    }
}

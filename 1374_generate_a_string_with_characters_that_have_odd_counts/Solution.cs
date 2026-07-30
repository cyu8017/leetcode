// LeetCode 1374 - Generate A String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

public class Solution {
    public string GenerateTheString(int n) {
        return n % 2 == 1 ? new string('a', n) : new string('a', n - 1) + "b";
    }
}

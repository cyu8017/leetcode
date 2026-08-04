// LeetCode 1374 - Generate A String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-String-with-characters-that-have-odd-counts/

class Solution {
    public String generateTheString(int n) {
        return n % 2 == 1 ? new String('a', n) : new String('a', n - 1) + "b";
    }
}

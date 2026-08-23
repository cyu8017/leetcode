// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

public class Solution {
    public int FirstUniqueEven(int[] nums) {
        var cnt = new int[101];
        foreach (int x in nums) cnt[x]++;
        foreach (int x in nums) {
            if (x % 2 == 0 && cnt[x] == 1) return x;
        }
        return -1;
    }
}

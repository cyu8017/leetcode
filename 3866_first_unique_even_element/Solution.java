// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

class Solution {
    public int firstUniqueEven(int[] nums) {
        var cnt = new int[101];
        for (int x : nums) cnt[x]++;
        for (int x : nums) {
            if (x % 2 == 0 && cnt[x] == 1) return x;
        }
        return -1;
    }
}

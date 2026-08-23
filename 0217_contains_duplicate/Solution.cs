// LeetCode 0217 - Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        var seen = new HashSet<int>();
        foreach (int num in nums) {
            if (!seen.Add(num)) {
                return true;
            }
        }
        return false;
    }
}

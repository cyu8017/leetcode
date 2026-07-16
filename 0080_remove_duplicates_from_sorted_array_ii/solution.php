// LeetCode 0080 - Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums) {
        if (count($nums) <= 2) {
            return count($nums);
        }

        $write = 2;
        for ($i = 2; $i < count($nums); $i++) {
            if ($nums[$i] !== $nums[$write - 2]) {
                $nums[$write] = $nums[$i];
                $write++;
            }
        }

        return $write;
    }
}

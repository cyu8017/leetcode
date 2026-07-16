// LeetCode 0026 - Remove Duplicates from Sorted Array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums) {
        if (count($nums) === 0) {
            return 0;
        }

        $write = 1;
        for ($read = 1; $read < count($nums); $read++) {
            if ($nums[$read] !== $nums[$write - 1]) {
                $nums[$write] = $nums[$read];
                $write++;
            }
        }

        return $write;
    }
}

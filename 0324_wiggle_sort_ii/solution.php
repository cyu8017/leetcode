// LeetCode 0324 - Wiggle Sort II
// https://leetcode.com/problems/wiggle-sort-ii/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function wiggleSort(&$nums) {
        $sortedNums = $nums;
        sort($sortedNums);
        $left = intdiv(count($nums) - 1, 2);
        $right = count($nums) - 1;
        foreach (array_keys($nums) as $index) {
            if ($index % 2 === 0) {
                $nums[$index] = $sortedNums[$left];
                $left--;
            } else {
                $nums[$index] = $sortedNums[$right];
                $right--;
            }
        }
        return $nums;
    }
}

// LeetCode 0280 - Wiggle Sort
// https://leetcode.com/problems/wiggle-sort/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function wiggleSort($nums) {
        $count = count($nums);
        for ($index = 1; $index < $count; $index++) {
            if ($index % 2 === 1 && $nums[$index] < $nums[$index - 1]) {
                $tmp = $nums[$index];
                $nums[$index] = $nums[$index - 1];
                $nums[$index - 1] = $tmp;
            } elseif ($index % 2 === 0 && $nums[$index] > $nums[$index - 1]) {
                $tmp = $nums[$index];
                $nums[$index] = $nums[$index - 1];
                $nums[$index - 1] = $tmp;
            }
        }
        return $nums;
    }
}

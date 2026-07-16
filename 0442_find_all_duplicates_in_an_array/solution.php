// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution {
    /**
     * @param int[] $nums
     * @return int[]
     */
    function findDuplicates($nums) {
        return $this->find_duplicates($nums);
    }

    /**
     * @param int[] $nums
     * @return int[]
     */
    function find_duplicates($nums) {
        $result = [];
        foreach ($nums as $number) {
            $index = abs($number) - 1;
            if ($nums[$index] < 0) {
                $result[] = abs($number);
            } else {
                $nums[$index] = -$nums[$index];
            }
        }
        return $result;
    }
}

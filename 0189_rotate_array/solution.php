// LeetCode 0189 - Rotate Array
// https://leetcode.com/problems/rotate-array/

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return NULL
     */
    function rotate(&$nums, $k) {
        $n = count($nums);
        $k %= $n;

        $this->reverseRange($nums, 0, $n - 1);
        $this->reverseRange($nums, 0, $k - 1);
        $this->reverseRange($nums, $k, $n - 1);
    }

    private function reverseRange(&$nums, $left, $right) {
        while ($left < $right) {
            [$nums[$left], $nums[$right]] = [$nums[$right], $nums[$left]];
            $left++;
            $right--;
        }
    }
}
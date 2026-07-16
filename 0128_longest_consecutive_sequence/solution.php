// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestConsecutive($nums) {
        $values = array_fill_keys($nums, true);
        $best = 0;
        foreach ($values as $number => $_) {
            $number = (int) $number;
            if (isset($values[$number - 1])) {
                continue;
            }
            $length = 1;
            while (isset($values[$number + $length])) {
                $length++;
            }
            $best = max($best, $length);
        }
        return $best;
    }
}
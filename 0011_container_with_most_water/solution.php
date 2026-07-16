// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

class Solution {
    /**
     * @param Integer[] $height
     * @return Integer
     */
    function maxArea($height) {
        $left = 0;
        $right = count($height) - 1;
        $best = 0;

        while ($left < $right) {
            $width = $right - $left;
            $best = max($best, min($height[$left], $height[$right]) * $width);
            if ($height[$left] < $height[$right]) {
                $left++;
            } else {
                $right--;
            }
        }

        return $best;
    }
}

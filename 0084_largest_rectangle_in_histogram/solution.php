// LeetCode 0084 - Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution {
    /**
     * @param Integer[] $heights
     * @return Integer
     */
    function largestRectangleArea($heights) {
        $stack = [];
        $maxArea = 0;
        $extended = array_merge($heights, [0]);
        $n = count($extended);

        for ($i = 0; $i < $n; $i++) {
            $height = $extended[$i];
            while (!empty($stack) && $extended[end($stack)] > $height) {
                $h = $extended[array_pop($stack)];
                $width = empty($stack) ? $i : $i - end($stack) - 1;
                $maxArea = max($maxArea, $h * $width);
            }
            $stack[] = $i;
        }

        return $maxArea;
    }
}

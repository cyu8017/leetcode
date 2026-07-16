// LeetCode 0085 - Maximal Rectangle
// https://leetcode.com/problems/maximal-rectangle/

class Solution {
    /**
     * @param String[][] $matrix
     * @return Integer
     */
    function maximalRectangle($matrix) {
        if ($matrix === null || count($matrix) === 0) {
            return 0;
        }

        $cols = count($matrix[0]);
        $heights = array_fill(0, $cols, 0);
        $maxArea = 0;

        foreach ($matrix as $row) {
            for ($j = 0; $j < $cols; $j++) {
                $heights[$j] = $row[$j] === '1' ? $heights[$j] + 1 : 0;
            }
            $maxArea = max($maxArea, $this->largestHistogram($heights));
        }

        return $maxArea;
    }

    private function largestHistogram($heights) {
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

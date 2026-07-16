// LeetCode 0356 - Line Reflection
// https://leetcode.com/problems/line-reflection/

class Solution {
    /**
     * @param Integer[][] $points
     * @return Boolean
     */
    function isReflected($points) {
        return $this->is_reflected($points);
    }

    /**
     * @param Integer[][] $points
     * @return Boolean
     */
    function is_reflected($points) {
        $pointSet = [];
        $minX = PHP_INT_MAX;
        $maxX = PHP_INT_MIN;

        foreach ($points as $point) {
            $x = $point[0];
            $y = $point[1];
            $pointSet[$x . ',' . $y] = true;
            $minX = min($minX, $x);
            $maxX = max($maxX, $x);
        }

        $target = $minX + $maxX;
        foreach ($points as $point) {
            $x = $point[0];
            $y = $point[1];
            if (!array_key_exists(($target - $x) . ',' . $y, $pointSet)) {
                return false;
            }
        }

        return true;
    }
}

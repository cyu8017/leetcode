// LeetCode 0469 - Convex Polygon
// https://leetcode.com/problems/convex-polygon/

class Solution {
    /**
     * @param int[][] $points
     * @return bool
     */
    function isConvex($points) {
        return $this->is_convex($points);
    }

    /**
     * @param int[][] $points
     * @return bool
     */
    function is_convex($points) {
        $direction = 0;
        $count = count($points);

        for ($index = 0; $index < $count; $index++) {
            $x1 = $points[($index + 1) % $count][0] - $points[$index][0];
            $y1 = $points[($index + 1) % $count][1] - $points[$index][1];
            $x2 = $points[($index + 2) % $count][0] - $points[($index + 1) % $count][0];
            $y2 = $points[($index + 2) % $count][1] - $points[($index + 1) % $count][1];
            $cross = $x1 * $y2 - $y1 * $x2;
            if ($cross === 0) {
                continue;
            }

            $current = $cross > 0 ? 1 : -1;
            if ($direction !== 0 && $direction !== $current) {
                return false;
            }
            if ($direction === 0) {
                $direction = $current;
            }
        }

        return true;
    }
}

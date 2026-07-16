// LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution {
    /**
     * @param int[][] $points
     * @return int
     */
    function findMinArrowShots($points) {
        return $this->find_min_arrow_shots($points);
    }

    /**
     * @param int[][] $points
     * @return int
     */
    function find_min_arrow_shots($points) {
        if (count($points) === 0) {
            return 0;
        }

        usort($points, fn($left, $right) => $left[1] <=> $right[1]);
        $arrows = 1;
        $end = $points[0][1];
        for ($index = 1; $index < count($points); $index++) {
            [$start, $finish] = $points[$index];
            if ($start > $end) {
                $arrows++;
                $end = $finish;
            }
        }
        return $arrows;
    }
}

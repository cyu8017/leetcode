// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

class Solution {
    /**
     * @param int[][] $points
     * @return int
     */
    function numberOfBoomerangs($points) {
        return $this->number_of_boomerangs($points);
    }

    /**
     * @param int[][] $points
     * @return int
     */
    function number_of_boomerangs($points) {
        $total = 0;
        foreach ($points as $anchor) {
            $distances = [];
            foreach ($points as $other) {
                $dx = $anchor[0] - $other[0];
                $dy = $anchor[1] - $other[1];
                $distance = $dx * $dx + $dy * $dy;
                $distances[$distance] = ($distances[$distance] ?? 0) + 1;
            }
            foreach ($distances as $count) {
                $total += $count * ($count - 1);
            }
        }
        return $total;
    }
}

// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution {
    /**
     * @param int[] $nums
     * @return int
     */
    function minMoves($nums) {
        return $this->min_moves($nums);
    }

    /**
     * @param int[] $nums
     * @return int
     */
    function min_moves($nums) {
        $minimum = min($nums);
        $total = 0;
        foreach ($nums as $value) {
            $total += $value - $minimum;
        }
        return $total;
    }
}

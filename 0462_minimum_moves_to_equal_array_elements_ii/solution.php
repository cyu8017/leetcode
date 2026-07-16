// LeetCode 0462 - Minimum Moves to Equal Array Elements II
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution {
    /**
     * @param int[] $nums
     * @return int
     */
    function minMoves2($nums) {
        return $this->min_moves2($nums);
    }

    /**
     * @param int[] $nums
     * @return int
     */
    function min_moves2($nums) {
        sort($nums);
        $median = $nums[intdiv(count($nums), 2)];
        $total = 0;
        foreach ($nums as $value) {
            $total += abs($value - $median);
        }
        return $total;
    }
}

// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

class Solution {
    /**
     * @param int[][] $intervals
     * @return int
     */
    function eraseOverlapIntervals($intervals) {
        return $this->erase_overlap_intervals($intervals);
    }

    /**
     * @param int[][] $intervals
     * @return int
     */
    function erase_overlap_intervals($intervals) {
        usort($intervals, fn($left, $right) => $left[1] <=> $right[1]);
        $removed = 0;
        $end = PHP_INT_MIN;
        foreach ($intervals as [$start, $finish]) {
            if ($start < $end) {
                $removed++;
            } else {
                $end = $finish;
            }
        }
        return $removed;
    }
}

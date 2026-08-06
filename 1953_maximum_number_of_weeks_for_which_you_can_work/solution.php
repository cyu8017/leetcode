<?php
class Solution {
    /**
     * @param Integer[] $milestones
     * @return Integer
     */
    function numberOfWeeks($milestones) {
        $total = array_sum($milestones);
        $mx = max($milestones);
        $rest = $total - $mx;
        if ($mx > $rest + 1) {
            return 2 * $rest + 1;
        }
        return $total;
    }
}

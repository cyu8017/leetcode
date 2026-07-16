// LeetCode 0390 - Elimination Game
// https://leetcode.com/problems/elimination-game/

class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function lastRemaining($n) {
        return $this->last_remaining($n);
    }

    /**
     * @param Integer $n
     * @return Integer
     */
    function last_remaining($n) {
        $left = 1;
        $right = $n;
        $step = 1;
        $remaining = $n;
        $fromLeft = true;

        while ($left < $right) {
            if ($fromLeft || $remaining % 2 === 1) {
                $left += $step;
            }
            $right -= $step;
            $step *= 2;
            $remaining = intdiv($remaining, 2);
            $fromLeft = !$fromLeft;
        }

        return $left;
    }
}

// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

class Solution {
    /**
     * @param String $currentState
     * @return Boolean
     */
    function canWin($currentState) {
        $memo = [];

        $canWinState = function ($state) use (&$canWinState, &$memo) {
            if (array_key_exists($state, $memo)) {
                return $memo[$state];
            }
            $length = strlen($state);
            for ($index = 0; $index < $length - 1; $index++) {
                if (substr($state, $index, 2) === "++") {
                    $nextState = substr($state, 0, $index) . "--" . substr($state, $index + 2);
                    if (!$canWinState($nextState)) {
                        $memo[$state] = true;
                        return true;
                    }
                }
            }
            $memo[$state] = false;
            return false;
        };

        return $canWinState($currentState);
    }
}

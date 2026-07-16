// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

class Solution {
    /**
     * @param Integer[][] $costs
     * @return Integer
     */
    function minCost($costs) {
        if (count($costs) === 0) {
            return 0;
        }
        $previous = $costs[0];
        for ($row = 1; $row < count($costs); $row++) {
            $previous = [
                $costs[$row][0] + min($previous[1], $previous[2]),
                $costs[$row][1] + min($previous[0], $previous[2]),
                $costs[$row][2] + min($previous[0], $previous[1]),
            ];
        }
        return min($previous);
    }
}

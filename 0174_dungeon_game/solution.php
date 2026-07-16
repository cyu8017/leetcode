// LeetCode 0174 - Dungeon Game
// https://leetcode.com/problems/dungeon-game/

class Solution {
    function calculateMinimumHP(array $dungeon): int {
        $rows = count($dungeon);
        $cols = count($dungeon[0]);
        $infinity = PHP_INT_MAX;
        $dp = array_fill(0, $rows + 1, array_fill(0, $cols + 1, $infinity));
        $dp[$rows][$cols - 1] = 1;
        $dp[$rows - 1][$cols] = 1;

        for ($row = $rows - 1; $row >= 0; $row--) {
            for ($col = $cols - 1; $col >= 0; $col--) {
                $need = min($dp[$row + 1][$col], $dp[$row][$col + 1]) - $dungeon[$row][$col];
                $dp[$row][$col] = max(1, $need);
            }
        }
        return $dp[0][0];
    }
}
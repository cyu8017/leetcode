// LeetCode 0419 - Battleships in a Board
// https://leetcode.com/problems/battleships-in-a-board/

class Solution {
    /**
     * @param String[][] $board
     * @return Integer
     */
    function countBattleships($board) {
        return $this->count_battleships($board);
    }

    /**
     * @param String[][] $board
     * @return Integer
     */
    function count_battleships($board) {
        $count = 0;
        foreach ($board as $row => $rowValues) {
            foreach ($rowValues as $col => $cell) {
                if ($cell !== "X") {
                    continue;
                }
                if ($row > 0 && $board[$row - 1][$col] === "X") {
                    continue;
                }
                if ($col > 0 && $board[$row][$col - 1] === "X") {
                    continue;
                }
                $count++;
            }
        }
        return $count;
    }
}

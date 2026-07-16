// LeetCode 0055 - Jump Game
// https://leetcode.com/problems/jump-game/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canJump($nums) {
        $farthest = 0;

        foreach ($nums as $i => $jump) {
            if ($i > $farthest) {
                return false;
            }
            $farthest = max($farthest, $i + $jump);
        }

        return true;
    }
}

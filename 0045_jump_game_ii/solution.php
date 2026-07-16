// LeetCode 0045 - Jump Game II
// https://leetcode.com/problems/jump-game-ii/

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function jump($nums) {
        $jumps = 0;
        $currentEnd = 0;
        $farthest = 0;
        $n = count($nums);

        for ($i = 0; $i < $n - 1; $i++) {
            $farthest = max($farthest, $i + $nums[$i]);
            if ($i === $currentEnd) {
                $jumps++;
                $currentEnd = $farthest;
            }
        }

        return $jumps;
    }
}

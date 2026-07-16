// LeetCode 0062 - Unique Paths
// https://leetcode.com/problems/unique-paths/

class Solution {
    /**
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function uniquePaths($m, $n) {
        $row = array_fill(0, $n, 1);

        for ($r = 1; $r < $m; $r++) {
            for ($col = 1; $col < $n; $col++) {
                $row[$col] += $row[$col - 1];
            }
        }

        return $row[$n - 1];
    }
}

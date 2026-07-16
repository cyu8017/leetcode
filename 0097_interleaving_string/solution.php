// LeetCode 0097 - Interleaving String
// https://leetcode.com/problems/interleaving-string/

class Solution {
    /**
     * @param String $s1
     * @param String $s2
     * @param String $s3
     * @return Boolean
     */
    function isInterleave($s1, $s2, $s3) {
        if (strlen($s1) + strlen($s2) !== strlen($s3)) {
            return false;
        }

        $m = strlen($s1);
        $n = strlen($s2);
        $dp = array_fill(0, $n + 1, false);
        $dp[0] = true;

        for ($j = 1; $j <= $n; $j++) {
            $dp[$j] = $dp[$j - 1] && $s2[$j - 1] === $s3[$j - 1];
        }

        for ($i = 1; $i <= $m; $i++) {
            $dp[0] = $dp[0] && $s1[$i - 1] === $s3[$i - 1];
            for ($j = 1; $j <= $n; $j++) {
                $dp[$j] = ($dp[$j] && $s1[$i - 1] === $s3[$i + $j - 1])
                    || ($dp[$j - 1] && $s2[$j - 1] === $s3[$i + $j - 1]);
            }
        }

        return $dp[$n];
    }
}

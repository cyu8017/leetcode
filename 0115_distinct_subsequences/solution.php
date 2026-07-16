class Solution {
    function numDistinct($s, $t) {
        $dp = array_fill(0, strlen($t) + 1, 0);
        $dp[0] = 1;
        for ($i = 0; $i < strlen($s); $i++) {
            for ($j = strlen($t) - 1; $j >= 0; $j--) {
                if ($s[$i] === $t[$j]) {
                    $dp[$j + 1] += $dp[$j];
                }
            }
        }
        return $dp[strlen($t)];
    }
}
// LeetCode 0091 - Decode Ways
// https://leetcode.com/problems/decode-ways/

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function numDecodings($s) {
        if ($s === null || $s === '' || $s[0] === '0') {
            return 0;
        }

        $prev2 = 1;
        $prev1 = 1;

        for ($i = 1; $i < strlen($s); $i++) {
            $current = 0;
            if ($s[$i] !== '0') {
                $current += $prev1;
            }
            $two = intval(substr($s, $i - 1, 2));
            if ($two >= 10 && $two <= 26) {
                $current += $prev2;
            }
            $prev2 = $prev1;
            $prev1 = $current;
        }

        return $prev1;
    }
}

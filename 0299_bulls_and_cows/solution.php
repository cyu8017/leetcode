// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

class Solution {
    /**
     * @param String $secret
     * @param String $guess
     * @return String
     */
    function getHint($secret, $guess) {
        $bulls = 0;
        $secretCounts = [];
        $guessCounts = [];
        $length = strlen($secret);
        for ($index = 0; $index < $length; $index++) {
            $secretDigit = $secret[$index];
            $guessDigit = $guess[$index];
            if ($secretDigit === $guessDigit) {
                $bulls++;
            } else {
                $secretCounts[$secretDigit] = ($secretCounts[$secretDigit] ?? 0) + 1;
                $guessCounts[$guessDigit] = ($guessCounts[$guessDigit] ?? 0) + 1;
            }
        }
        $cows = 0;
        foreach ($guessCounts as $digit => $count) {
            $cows += min($count, $secretCounts[$digit] ?? 0);
        }
        return "{$bulls}A{$cows}B";
    }
}

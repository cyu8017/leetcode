// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

class Solution {
    /**
     * @param String $pattern
     * @param String $s
     * @return Boolean
     */
    function wordPatternMatch($pattern, $s) {
        $charToWord = [];
        $wordToChar = [];

        $backtrack = function ($patternIndex, $stringIndex) use (
            &$backtrack,
            $pattern,
            $s,
            &$charToWord,
            &$wordToChar
        ) {
            if ($patternIndex === strlen($pattern)) {
                return $stringIndex === strlen($s);
            }
            $char = $pattern[$patternIndex];
            if (array_key_exists($char, $charToWord)) {
                $word = $charToWord[$char];
                if (substr($s, $stringIndex, strlen($word)) !== $word) {
                    return false;
                }
                return $backtrack($patternIndex + 1, $stringIndex + strlen($word));
            }
            for ($end = $stringIndex + 1; $end <= strlen($s); $end++) {
                $word = substr($s, $stringIndex, $end - $stringIndex);
                if (array_key_exists($word, $wordToChar)) {
                    continue;
                }
                $charToWord[$char] = $word;
                $wordToChar[$word] = $char;
                if ($backtrack($patternIndex + 1, $end)) {
                    return true;
                }
                unset($charToWord[$char], $wordToChar[$word]);
            }
            return false;
        };

        return $backtrack(0, 0);
    }
}

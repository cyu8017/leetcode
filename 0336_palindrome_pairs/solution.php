// LeetCode 0336 - Palindrome Pairs
// https://leetcode.com/problems/palindrome-pairs/

class Solution {
    /**
     * @param String[] $words
     * @return Integer[][]
     */
    function palindromePairs($words) {
        return $this->palindrome_pairs($words);
    }

    /**
     * @param String[] $words
     * @return Integer[][]
     */
    function palindrome_pairs($words) {
        $wordMap = [];
        foreach ($words as $index => $word) {
            $wordMap[$word] = $index;
        }
        $result = [];

        foreach ($words as $index => $word) {
            $length = strlen($word);
            for ($split = 0; $split <= $length; $split++) {
                $left = substr($word, 0, $split);
                $right = substr($word, $split);
                if ($left === strrev($left)) {
                    $reversedRight = strrev($right);
                    if (array_key_exists($reversedRight, $wordMap) && $wordMap[$reversedRight] !== $index) {
                        $result[$wordMap[$reversedRight] . "," . $index] = [$wordMap[$reversedRight], $index];
                    }
                }
                if ($right === strrev($right)) {
                    $reversedLeft = strrev($left);
                    if (array_key_exists($reversedLeft, $wordMap) && $wordMap[$reversedLeft] !== $index) {
                        $result[$index . "," . $wordMap[$reversedLeft]] = [$index, $wordMap[$reversedLeft]];
                    }
                }
            }
        }

        $pairs = array_values($result);
        usort($pairs, function ($left, $right) {
            if ($left[0] !== $right[0]) {
                return $left[0] <=> $right[0];
            }
            return $left[1] <=> $right[1];
        });
        return $pairs;
    }
}

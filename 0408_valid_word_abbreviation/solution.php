// LeetCode 0408 - Valid Word Abbreviation
// https://leetcode.com/problems/valid-word-abbreviation/

class Solution {
    /**
     * @param String $word
     * @param String $abbr
     * @return Boolean
     */
    function validWordAbbreviation($word, $abbr) {
        return $this->valid_word_abbreviation($word, $abbr);
    }

    /**
     * @param String $word
     * @param String $abbr
     * @return Boolean
     */
    function valid_word_abbreviation($word, $abbr) {
        $i = 0;
        $j = 0;
        $wordLength = strlen($word);
        $abbrLength = strlen($abbr);

        while ($i < $wordLength && $j < $abbrLength) {
            if (ctype_digit($abbr[$j])) {
                if ($abbr[$j] === "0") {
                    return false;
                }
                $number = 0;
                while ($j < $abbrLength && ctype_digit($abbr[$j])) {
                    $number = $number * 10 + (int)$abbr[$j];
                    $j++;
                }
                $i += $number;
            } else {
                if ($word[$i] !== $abbr[$j]) {
                    return false;
                }
                $i++;
                $j++;
            }
        }

        return $i === $wordLength && $j === $abbrLength;
    }
}

// LeetCode 0418 - Sentence Screen Fitting
// https://leetcode.com/problems/sentence-screen-fitting/

class Solution {
    /**
     * @param String[] $sentence
     * @param Integer $rows
     * @param Integer $cols
     * @return Integer
     */
    function wordsTyping($sentence, $rows, $cols) {
        return $this->words_typing($sentence, $rows, $cols);
    }

    /**
     * @param String[] $sentence
     * @param Integer $rows
     * @param Integer $cols
     * @return Integer
     */
    function words_typing($sentence, $rows, $cols) {
        $count = 0;
        $index = 0;
        $total = count($sentence);

        for ($row = 0; $row < $rows; $row++) {
            $col = 0;
            while (true) {
                $word = $sentence[$index];
                $needed = strlen($word) + ($col > 0 ? 1 : 0);
                if ($col + $needed > $cols) {
                    break;
                }
                if ($col > 0) {
                    $col++;
                }
                $col += strlen($word);
                $index = ($index + 1) % $total;
                if ($index === 0) {
                    $count++;
                }
            }
        }

        return $count;
    }
}

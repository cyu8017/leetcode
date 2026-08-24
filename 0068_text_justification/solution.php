<?php
// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

class Solution {
    /**
     * @param String[] $words
     * @param Integer $maxWidth
     * @return String[]
     */
    function fullJustify($words, $maxWidth) {
        $result = [];
        $i = 0;
        $n = count($words);

        while ($i < $n) {
            $lineWords = [];
            $lineLen = 0;

            while ($i < $n) {
                $word = $words[$i];
                $extra = empty($lineWords) ? 0 : 1;
                if ($lineLen + strlen($word) + $extra > $maxWidth) {
                    break;
                }
                $lineWords[] = $word;
                $lineLen += strlen($word) + $extra;
                $i++;
            }

            if ($i === $n || count($lineWords) === 1) {
                $line = implode(' ', $lineWords);
                $line .= str_repeat(' ', $maxWidth - strlen($line));
                $result[] = $line;
            } else {
                $totalChars = 0;
                foreach ($lineWords as $word) {
                    $totalChars += strlen($word);
                }
                $totalSpaces = $maxWidth - $totalChars;
                $gaps = count($lineWords) - 1;
                $space = intdiv($totalSpaces, $gaps);
                $remainder = $totalSpaces % $gaps;
                $line = '';
                for ($j = 0; $j < count($lineWords) - 1; $j++) {
                    $line .= $lineWords[$j];
                    $line .= str_repeat(' ', $space + ($j < $remainder ? 1 : 0));
                }
                $line .= $lineWords[count($lineWords) - 1];
                $result[] = $line;
            }
        }

        return $result;
    }
}

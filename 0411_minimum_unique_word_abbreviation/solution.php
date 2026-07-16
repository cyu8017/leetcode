// LeetCode 0411 - Minimum Unique Word Abbreviation
// https://leetcode.com/problems/minimum-unique-word-abbreviation/

class Solution {
    /** @var string */
    private $target;

    /** @var string[] */
    private $words;

    /** @var int */
    private $bestLen;

    /** @var string */
    private $result;

    /**
     * @param String $target
     * @param String[] $dictionary
     * @return String
     */
    function minAbbreviation($target, $dictionary) {
        return $this->min_abbreviation($target, $dictionary);
    }

    /**
     * @param String $target
     * @param String[] $dictionary
     * @return String
     */
    function min_abbreviation($target, $dictionary) {
        $this->target = $target;
        $this->words = array_values(array_filter(
            $dictionary,
            fn($word) => strlen($word) === strlen($target)
        ));
        $this->bestLen = strlen($target) + 1;
        $this->result = $target;
        $this->dfs(0, [], 0);
        return $this->result;
    }

    /**
     * @param string $word
     * @param string $abbr
     * @return bool
     */
    private function matches($word, $abbr) {
        $index = 0;
        $pointer = 0;
        $wordLength = strlen($word);
        $abbrLength = strlen($abbr);

        while ($index < $wordLength && $pointer < $abbrLength) {
            if (ctype_digit($abbr[$pointer])) {
                if ($abbr[$pointer] === "0") {
                    return false;
                }
                $number = 0;
                while ($pointer < $abbrLength && ctype_digit($abbr[$pointer])) {
                    $number = $number * 10 + (int)$abbr[$pointer];
                    $pointer++;
                }
                $index += $number;
            } else {
                if ($word[$index] !== $abbr[$pointer]) {
                    return false;
                }
                $index++;
                $pointer++;
            }
        }

        return $index === $wordLength && $pointer === $abbrLength;
    }

    /**
     * @param string $abbr
     * @return bool
     */
    private function isValid($abbr) {
        if (!$this->matches($this->target, $abbr)) {
            return false;
        }
        foreach ($this->words as $word) {
            if ($this->matches($word, $abbr)) {
                return false;
            }
        }
        return true;
    }

    /**
     * @param int $index
     * @param string[] $parts
     * @param int $skip
     * @return void
     */
    private function dfs($index, $parts, $skip) {
        if ($index === strlen($this->target)) {
            $abbr = implode("", $parts) . ($skip ? (string)$skip : "");
            if (
                $this->isValid($abbr) &&
                (strlen($abbr) < $this->bestLen || (strlen($abbr) === $this->bestLen && $abbr < $this->result))
            ) {
                $this->bestLen = strlen($abbr);
                $this->result = $abbr;
            }
            return;
        }

        $this->dfs($index + 1, $parts, $skip + 1);

        $newParts = $parts;
        if ($skip) {
            $newParts[] = (string)$skip;
        }
        $newParts[] = $this->target[$index];
        $this->dfs($index + 1, $newParts, 0);
    }
}

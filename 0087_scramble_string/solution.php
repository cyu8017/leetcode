// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

class Solution {
    private $memo = [];

    /**
     * @param String $s1
     * @param String $s2
     * @return Boolean
     */
    function isScramble($s1, $s2) {
        $key = $s1 . '#' . $s2;
        if (array_key_exists($key, $this->memo)) {
            return $this->memo[$key];
        }
        if ($s1 === $s2) {
            return $this->memo[$key] = true;
        }
        $a = str_split($s1);
        $b = str_split($s2);
        sort($a);
        sort($b);
        if ($a !== $b) {
            return $this->memo[$key] = false;
        }

        $n = strlen($s1);
        for ($i = 1; $i < $n; $i++) {
            if ($this->isScramble(substr($s1, 0, $i), substr($s2, 0, $i))
                && $this->isScramble(substr($s1, $i), substr($s2, $i))) {
                return $this->memo[$key] = true;
            }
            if ($this->isScramble(substr($s1, 0, $i), substr($s2, $n - $i))
                && $this->isScramble(substr($s1, $i), substr($s2, 0, $n - $i))) {
                return $this->memo[$key] = true;
            }
        }
        return $this->memo[$key] = false;
    }
}

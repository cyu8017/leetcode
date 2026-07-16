// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

class ValidWordAbbr {
    /** @var array<string, array<string, bool>> */
    private $groups;

    /**
     * @param String[] $dictionary
     */
    function __construct($dictionary) {
        $this->groups = [];
        foreach ($dictionary as $word) {
            $key = self::abbreviate($word);
            if (!isset($this->groups[$key])) {
                $this->groups[$key] = [];
            }
            $this->groups[$key][$word] = true;
        }
    }

    /**
     * @param String $word
     * @return Boolean
     */
    function isUnique($word) {
        $key = self::abbreviate($word);
        if (!isset($this->groups[$key])) {
            return true;
        }
        $words = array_keys($this->groups[$key]);
        return count($words) === 1 && isset($this->groups[$key][$word]);
    }

    /**
     * @param String $word
     * @return String
     */
    private static function abbreviate($word) {
        $length = strlen($word);
        if ($length <= 2) {
            return $word;
        }
        return $word[0] . ($length - 2) . $word[$length - 1];
    }
}

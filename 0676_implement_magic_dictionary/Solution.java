// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/

class MagicDictionary {
    private String[] words = new String[0];

    public MagicDictionary() {}

    public void buildDict(String[] dictionary) {
        words = dictionary;
    }

    public boolean search(String searchWord) {
        for (String word : words) {
            if (word.length() != searchWord.length()) {
                continue;
            }
            int diff = 0;
            for (int i = 0; i < word.length(); ++i) {
                if (word.charAt(i) != searchWord.charAt(i)) {
                    ++diff;
                }
            }
            if (diff == 1) {
                return true;
            }
        }
        return false;
    }
}

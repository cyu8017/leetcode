// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int i = 0;

        while (i < words.length) {
            List<String> lineWords = new ArrayList<>();
            int lineLen = 0;

            while (i < words.length) {
                String word = words[i];
                int extra = lineWords.isEmpty() ? 0 : 1;
                if (lineLen + word.length() + extra > maxWidth) {
                    break;
                }
                lineWords.add(word);
                lineLen += word.length() + extra;
                i++;
            }

            if (i == words.length || lineWords.size() == 1) {
                StringBuilder line = new StringBuilder();
                for (int j = 0; j < lineWords.size(); j++) {
                    if (j > 0) {
                        line.append(' ');
                    }
                    line.append(lineWords.get(j));
                }
                while (line.length() < maxWidth) {
                    line.append(' ');
                }
                result.add(line.toString());
            } else {
                int totalChars = 0;
                for (String word : lineWords) {
                    totalChars += word.length();
                }
                int totalSpaces = maxWidth - totalChars;
                int gaps = lineWords.size() - 1;
                int space = totalSpaces / gaps;
                int remainder = totalSpaces % gaps;
                StringBuilder line = new StringBuilder();
                for (int j = 0; j < lineWords.size() - 1; j++) {
                    line.append(lineWords.get(j));
                    for (int k = 0; k < space + (j < remainder ? 1 : 0); k++) {
                        line.append(' ');
                    }
                }
                line.append(lineWords.get(lineWords.size() - 1));
                result.add(line.toString());
            }
        }

        return result;
    }
}

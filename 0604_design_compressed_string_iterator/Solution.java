// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

import java.util.ArrayList;
import java.util.List;

class StringIterator {
    private final List<Character> chars = new ArrayList<>();
    private final List<Integer> counts = new ArrayList<>();
    private int index = 0;

    public StringIterator(String compressedString) {
        int n = compressedString.length();
        int i = 0;
        while (i < n) {
            char ch = compressedString.charAt(i++);
            int j = i;
            while (j < n && compressedString.charAt(j) >= '0' && compressedString.charAt(j) <= '9') {
                ++j;
            }
            chars.add(ch);
            counts.add(Integer.parseInt(compressedString.substring(i, j)));
            i = j;
        }
    }

    public char next() {
        if (!hasNext()) {
            return ' ';
        }
        char ch = chars.get(index);
        counts.set(index, counts.get(index) - 1);
        if (counts.get(index) == 0) {
            ++index;
        }
        return ch;
    }

    public boolean hasNext() {
        return index < chars.size();
    }
}

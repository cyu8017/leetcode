// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

import java.util.ArrayList;
import java.util.List;

class TextEditor {
    private List<Character> left = new ArrayList<>();
    private List<Character> right = new ArrayList<>();

    private String suffix() {
        int start = Math.max(0, left.size() - 10);
        StringBuilder sb = new StringBuilder();
        for (int i = start; i < left.size(); i++) sb.append(left.get(i));
        return sb.toString();
    }

    public TextEditor() {}

    public void addText(String text) {
        for (char c : text.toCharArray()) left.add(c);
    }

    public int deleteText(int k) {
        int deleted = 0;
        while (k > 0 && !left.isEmpty()) {
            left.remove(left.size() - 1);
            k--;
            deleted++;
        }
        return deleted;
    }

    public String cursorLeft(int k) {
        while (k > 0 && !left.isEmpty()) {
            right.add(left.remove(left.size() - 1));
            k--;
        }
        return suffix();
    }

    public String cursorRight(int k) {
        while (k > 0 && !right.isEmpty()) {
            left.add(right.remove(right.size() - 1));
            k--;
        }
        return suffix();
    }
}

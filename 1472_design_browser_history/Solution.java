// LeetCode 1472 - Design Browser History
// https://leetcode.com/problems/design-browser-history/

import java.util.*;

class BrowserHistory {
    List<String> history = new ArrayList<>(); int index;
    public BrowserHistory(String homepage) { history.add(homepage); index = 0; }
    public void visit(String url) {
        history.RemoveRange(index + 1, history.size() - index - 1);
        history.add(url); index++;
    }
    public String back(int steps) { index = Math.max(0, index - steps); return history[index]; }
    public String forward(int steps) {
        index = Math.min(history.size() - 1, index + steps); return history[index];
    }
}

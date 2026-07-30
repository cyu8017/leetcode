// LeetCode 1472 - Design Browser History
// https://leetcode.com/problems/design-browser-history/

using System.Collections.Generic;
public class BrowserHistory {
    List<string> history = new List<string>(); int index;
    public BrowserHistory(string homepage) { history.Add(homepage); index = 0; }
    public void Visit(string url) {
        history.RemoveRange(index + 1, history.Count - index - 1);
        history.Add(url); index++;
    }
    public string Back(int steps) { index = System.Math.Max(0, index - steps); return history[index]; }
    public string Forward(int steps) {
        index = System.Math.Min(history.Count - 1, index + steps); return history[index];
    }
}

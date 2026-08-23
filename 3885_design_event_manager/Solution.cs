// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

using System.Collections.Generic;

public class EventManager {
    SortedSet<(int, int)> sl = new SortedSet<(int, int)>();
    Dictionary<int, int> d = new Dictionary<int, int>();

    public EventManager(int[][] events) {
        foreach (var e in events) {
            int eventId = e[0], priority = e[1];
            sl.Add((-priority, eventId));
            d[eventId] = priority;
        }
    }

    public void UpdatePriority(int eventId, int newPriority) {
        int old = d[eventId];
        sl.Remove((-old, eventId));
        sl.Add((-newPriority, eventId));
        d[eventId] = newPriority;
    }

    public int PollHighest() {
        if (sl.Count == 0) return -1;
        var top = default((int, int));
        foreach (var x in sl) { top = x; break; }
        int eventId = top.Item2;
        sl.Remove(top);
        d.Remove(eventId);
        return eventId;
    }
}

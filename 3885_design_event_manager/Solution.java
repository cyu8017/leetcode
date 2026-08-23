// LeetCode 3885 - Design Event Manager
// https://leetcode.com/problems/design-event-manager/

import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

class EventManager {
    TreeSet<long[]> sl = new TreeSet<>((a, b) -> {
        if (a[0] != b[0]) return Long.compare(a[0], b[0]);
        return Long.compare(a[1], b[1]);
    });
    Map<Integer, Integer> d = new HashMap<>();

    public EventManager(int[][] events) {
        for (int[] e : events) {
            int eventId = e[0], priority = e[1];
            sl.add(new long[] { -priority, eventId });
            d.put(eventId, priority);
        }
    }

    public void updatePriority(int eventId, int newPriority) {
        int old = d.get(eventId);
        sl.remove(new long[] { -old, eventId });
        sl.add(new long[] { -newPriority, eventId });
        d.put(eventId, newPriority);
    }

    public int pollHighest() {
        if (sl.isEmpty()) return -1;
        long[] top = sl.first();
        int eventId = (int) top[1];
        sl.remove(top);
        d.remove(eventId);
        return eventId;
    }
}

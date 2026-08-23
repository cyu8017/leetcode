// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

import java.util.*;
import java.util.function.Consumer;

// JS EventEmitter stand-in
class EventEmitter {
    private final Map<String, List<Consumer<int[]>>> handlers = new HashMap<>();

    public EventEmitter() {}

    public Runnable subscribe(String eventName, Consumer<int[]> callback) {
        handlers.computeIfAbsent(eventName, k -> new ArrayList<>()).add(callback);
        int[] idx = new int[] {handlers.get(eventName).size() - 1};
        return () -> {
            List<Consumer<int[]>> v = handlers.get(eventName);
            if (v != null && idx[0] >= 0 && idx[0] < v.size()) {
                v.remove(idx[0]);
                idx[0] = -1;
            }
        };
    }

    public int[] emit(String eventName, int[] args) {
        List<Integer> res = new ArrayList<>();
        List<Consumer<int[]>> list = handlers.get(eventName);
        if (list != null) {
            for (Consumer<int[]> cb : new ArrayList<>(list)) {
                cb.accept(args);
                res.add(0);
            }
        }
        int[] out = new int[res.size()];
        for (int i = 0; i < res.size(); i++) out[i] = res.get(i);
        return out;
    }
}

class Solution {
    public EventEmitter createEmitter() {
        return new EventEmitter();
    }
}

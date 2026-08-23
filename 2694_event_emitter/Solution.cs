// LeetCode 2694 - Event Emitter
// https://leetcode.com/problems/event-emitter/

// JS EventEmitter stand-in
using System;
using System.Collections.Generic;

public class EventEmitter {
    Dictionary<string, List<Action<int[]>>> handlers = new Dictionary<string, List<Action<int[]>>>();

    public EventEmitter() {}

    public Action Subscribe(string eventName, Action<int[]> callback) {
        if (!handlers.ContainsKey(eventName)) handlers[eventName] = new List<Action<int[]>>();
        handlers[eventName].Add(callback);
        int idx = handlers[eventName].Count - 1;
        return () => {
            if (handlers.TryGetValue(eventName, out var v) && idx >= 0 && idx < v.Count) {
                v.RemoveAt(idx);
                idx = -1;
            }
        };
    }

    public int[] Emit(string eventName, int[] args) {
        var res = new List<int>();
        if (handlers.TryGetValue(eventName, out var list)) {
            foreach (var cb in list) {
                cb(args);
                res.Add(0);
            }
        }
        return res.ToArray();
    }
}

public class Solution {
    public EventEmitter CreateEmitter() => new EventEmitter();
}

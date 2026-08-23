// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] CountMentions(int numberOfUsers, IList<IList<string>> events) {
        var list = new List<IList<string>>(events);
        list.Sort((a, b) => {
            int ti = int.Parse(a[1]), tj = int.Parse(b[1]);
            if (ti != tj) return ti.CompareTo(tj);
            return string.CompareOrdinal(b[0], a[0]);
        });
        bool[] online = new bool[numberOfUsers];
        for (int i = 0; i < numberOfUsers; i++) online[i] = true;
        int[] offlineUntil = new int[numberOfUsers];
        int[] ans = new int[numberOfUsers];
        foreach (var e in list) {
            int t = int.Parse(e[1]);
            for (int i = 0; i < numberOfUsers; i++) {
                if (!online[i] && offlineUntil[i] <= t) online[i] = true;
            }
            if (e[0] == "OFFLINE") {
                int id = int.Parse(e[2]);
                online[id] = false;
                offlineUntil[id] = t + 60;
            } else {
                string msg = e[2];
                if (msg == "ALL") {
                    for (int i = 0; i < numberOfUsers; i++) ans[i]++;
                } else if (msg == "HERE") {
                    for (int i = 0; i < numberOfUsers; i++) if (online[i]) ans[i]++;
                } else {
                    foreach (string part in msg.Split(' ', StringSplitOptions.RemoveEmptyEntries)) {
                        int id = int.Parse(part.Substring(2));
                        ans[id]++;
                    }
                }
            }
        }
        return ans;
    }
}

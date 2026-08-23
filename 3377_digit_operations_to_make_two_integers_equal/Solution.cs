// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

using System.Collections.Generic;

public class Solution {
    bool[] Sieve(int n) {
        bool[] isP = new bool[n];
        for (int i = 2; i < n; i++) isP[i] = true;
        for (int i = 2; i * i < n; i++) {
            if (isP[i]) {
                for (int j = i * i; j < n; j += i) isP[j] = false;
            }
        }
        return isP;
    }

    public int MinOperations(int n, int m) {
        var isPrime = Sieve(100000);
        if (isPrime[n]) return -1;
        int[] dist = new int[100000];
        for (int i = 0; i < 100000; i++) dist[i] = -1;
        var pq = new PriorityQueue<(int cost, int val), int>();
        pq.Enqueue((n, n), n);
        dist[n] = n;
        while (pq.Count > 0) {
            var cur = pq.Dequeue();
            int cost = cur.cost, val = cur.val;
            if (cost != dist[val]) continue;
            if (val == m) return cost;
            char[] s = val.ToString().ToCharArray();
            for (int i = 0; i < s.Length; i++) {
                char orig = s[i];
                foreach (int d in new int[] { -1, 1 }) {
                    int nd = (orig - '0') + d;
                    if (nd < 0 || nd > 9) continue;
                    if (i == 0 && nd == 0 && s.Length > 1) continue;
                    s[i] = (char)('0' + nd);
                    int nv = int.Parse(new string(s));
                    s[i] = orig;
                    if (isPrime[nv]) continue;
                    int nc = cost + nv;
                    if (dist[nv] == -1 || nc < dist[nv]) {
                        dist[nv] = nc;
                        pq.Enqueue((nc, nv), nc);
                    }
                }
            }
        }
        return -1;
    }
}

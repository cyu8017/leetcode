// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    private boolean[] sieve(int n) {
        boolean[] isP = new boolean[n];
        for (int i = 2; i < n; i++) isP[i] = true;
        for (int i = 2; i * i < n; i++) {
            if (isP[i]) {
                for (int j = i * i; j < n; j += i) isP[j] = false;
            }
        }
        return isP;
    }

    public int minOperations(int n, int m) {
        boolean[] isPrime = sieve(100000);
        if (isPrime[n]) return -1;
        int[] dist = new int[100000];
        Arrays.fill(dist, -1);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        pq.offer(new int[] {n, n});
        dist[n] = n;
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int cost = cur[0], val = cur[1];
            if (cost != dist[val]) continue;
            if (val == m) return cost;
            char[] s = String.valueOf(val).toCharArray();
            for (int i = 0; i < s.length; i++) {
                char orig = s[i];
                for (int d : new int[] {-1, 1}) {
                    int nd = (orig - '0') + d;
                    if (nd < 0 || nd > 9) continue;
                    if (i == 0 && nd == 0 && s.length > 1) continue;
                    s[i] = (char) ('0' + nd);
                    int nv = Integer.parseInt(new String(s));
                    s[i] = orig;
                    if (isPrime[nv]) continue;
                    int nc = cost + nv;
                    if (dist[nv] == -1 || nc < dist[nv]) {
                        dist[nv] = nc;
                        pq.offer(new int[] {nc, nv});
                    }
                }
            }
        }
        return -1;
    }
}

// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

public class Solution {
    public int[] GroupStrings(string[] words) {
        var parent = new Dictionary<int, int>();
        var size = new Dictionary<int, int>();
        var freq = new Dictionary<int, int>();
        int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }
        void Unite(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra == rb) return;
            if (size[ra] < size[rb]) { int t = ra; ra = rb; rb = t; }
            parent[rb] = ra;
            size[ra] += size[rb];
        }
        int MaskOf(string w) {
            int m = 0;
            foreach (char c in w) m |= 1 << (c - 'a');
            return m;
        }
        foreach (string w in words) {
            int m = MaskOf(w);
            if (!freq.ContainsKey(m)) freq[m] = 0;
            freq[m]++;
        }
        foreach (var kv in freq) { parent[kv.Key] = kv.Key; size[kv.Key] = kv.Value; }
        foreach (int m in freq.Keys.ToList()) {
            for (int b = 0; b < 26; b++) {
                if ((m & (1 << b)) != 0) {
                    int nm = m ^ (1 << b);
                    if (freq.ContainsKey(nm)) Unite(m, nm);
                    for (int a = 0; a < 26; a++) {
                        if ((nm & (1 << a)) == 0) {
                            int rm = nm | (1 << a);
                            if (freq.ContainsKey(rm)) Unite(m, rm);
                        }
                    }
                } else {
                    int nm = m | (1 << b);
                    if (freq.ContainsKey(nm)) Unite(m, nm);
                }
            }
        }
        int groups = 0, maxSize = 0;
        var seen = new HashSet<int>();
        foreach (int m in freq.Keys) {
            int r = Find(m);
            if (!seen.Contains(r)) {
                seen.Add(r);
                groups++;
                maxSize = Math.Max(maxSize, size[r]);
            }
        }
        return new[] { groups, maxSize };
    }
}

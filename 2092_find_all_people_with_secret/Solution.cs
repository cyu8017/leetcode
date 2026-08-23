// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

public class Solution {
    public IList<int> FindAllPeople(int n, int[][] meetings, int firstPerson) {
        Array.Sort(meetings, (a, b) => a[2].CompareTo(b[2]));
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        int Find(int x) {
            return parent[x] == x ? x : parent[x] = Find(parent[x]);
        }
        void Unite(int a, int b) {
            a = Find(a); b = Find(b);
            if (a != b) parent[a] = b;
        }

        bool[] know = new bool[n];
        know[0] = know[firstPerson] = true;
        Unite(0, firstPerson);
        for (int i = 0; i < meetings.Length; ) {
            int j = i;
            while (j < meetings.Length && meetings[j][2] == meetings[i][2]) j++;
            for (int k = i; k < j; k++) Unite(meetings[k][0], meetings[k][1]);
            int root0 = Find(0);
            var reset = new List<int>();
            for (int k = i; k < j; k++) {
                int a = meetings[k][0], b = meetings[k][1];
                if (Find(a) != root0) { reset.Add(a); reset.Add(b); }
                else { know[a] = know[b] = true; }
            }
            foreach (int x in reset) parent[x] = x;
            i = j;
        }
        var ans = new List<int>();
        for (int i = 0; i < n; i++) if (Find(i) == Find(0) || know[i]) ans.Add(i);
        return ans;
    }
}

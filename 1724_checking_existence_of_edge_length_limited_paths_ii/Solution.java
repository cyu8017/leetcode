// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class DistanceLimitedPathsExist {
    private final int[] weights;
    private final int[][] versions;

    public DistanceLimitedPathsExist(int n, int[][] edgeList) {
        int[][] edges = new int[edgeList.length][3];
        for (int i = 0; i < edgeList.length; i++) {
            edges[i][0] = edgeList[i][2];
            edges[i][1] = edgeList[i][0];
            edges[i][2] = edgeList[i][1];
        }
        Arrays.sort(edges, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            if (a[1] != b[1]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[2], b[2]);
        });
        int[] parent = new int[n];
        int[] size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        List<Integer> weightList = new ArrayList<>();
        List<int[]> versionList = new ArrayList<>();
        int i = 0;
        while (i < edges.length) {
            int weight = edges[i][0];
            while (i < edges.length && edges[i][0] == weight) {
                union(parent, size, edges[i][1], edges[i][2]);
                i++;
            }
            weightList.add(weight);
            versionList.add(parent.clone());
        }
        weights = new int[weightList.size()];
        for (int j = 0; j < weights.length; j++) {
            weights[j] = weightList.get(j);
        }
        versions = versionList.toArray(new int[0][]);
    }

    public boolean query(int p, int q, int limit) {
        int lo = 0;
        int hi = weights.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (weights[mid] < limit) lo = mid + 1;
            else hi = mid;
        }
        int idx = lo - 1;
        if (idx < 0) return p == q;
        int[] parent = versions[idx];
        return find(parent, p) == find(parent, q);
    }

    private static int find(int[] parent, int x) {
        while (parent[x] != x) {
            x = parent[x];
        }
        return x;
    }

    private static void union(int[] parent, int[] size, int a, int b) {
        int ra = findCompress(parent, a);
        int rb = findCompress(parent, b);
        if (ra == rb) return;
        if (size[ra] < size[rb]) {
            int tmp = ra;
            ra = rb;
            rb = tmp;
        }
        parent[rb] = ra;
        size[ra] += size[rb];
    }

    private static int findCompress(int[] parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
}

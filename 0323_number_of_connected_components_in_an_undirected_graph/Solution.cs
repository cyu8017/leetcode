// LeetCode 0323 - Number of Connected Components in an Undirected Graph

// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/



public class Solution {

    public int CountComponents(int n, int[][] edges) {

        int[] parent = new int[n];

        int[] rank = new int[n];

        for (int index = 0; index < n; index++) {

            parent[index] = index;

        }



        int components = n;

        foreach (int[] edge in edges) {

            int left = edge[0];

            int right = edge[1];

            int rootLeft = Find(parent, left);

            int rootRight = Find(parent, right);

            if (rootLeft == rootRight) {

                continue;

            }

            if (rank[rootLeft] < rank[rootRight]) {

                (rootLeft, rootRight) = (rootRight, rootLeft);

            }

            parent[rootRight] = rootLeft;

            if (rank[rootLeft] == rank[rootRight]) {

                rank[rootLeft]++;

            }

            components--;

        }

        return components;

    }



    private int Find(int[] parent, int node) {

        if (parent[node] != node) {

            parent[node] = Find(parent, parent[node]);

        }

        return parent[node];

    }

}


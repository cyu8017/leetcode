// LeetCode 0323 - Number of Connected Components in an Undirected Graph

// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/



class Solution {

    public int countComponents(int n, int[][] edges) {

        int[] parent = new int[n];

        int[] rank = new int[n];

        for (int index = 0; index < n; index++) {

            parent[index] = index;

        }



        int components = n;

        for (int[] edge : edges) {

            int left = edge[0];

            int right = edge[1];

            int rootLeft = find(parent, left);

            int rootRight = find(parent, right);

            if (rootLeft == rootRight) {

                continue;

            }

            if (rank[rootLeft] < rank[rootRight]) {

                int temp = rootLeft;

                rootLeft = rootRight;

                rootRight = temp;

            }

            parent[rootRight] = rootLeft;

            if (rank[rootLeft] == rank[rootRight]) {

                rank[rootLeft]++;

            }

            components--;

        }

        return components;

    }



    private int find(int[] parent, int node) {

        if (parent[node] != node) {

            parent[node] = find(parent, parent[node]);

        }

        return parent[node];

    }

}


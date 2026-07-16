// LeetCode 0399 - Evaluate Division

// https://leetcode.com/problems/evaluate-division/



import java.util.ArrayList;

import java.util.HashMap;

import java.util.HashSet;

import java.util.List;

import java.util.Map;

import java.util.Set;



class Solution {

    public double[] calcEquation(

            List<List<String>> equations,

            double[] values,

            List<List<String>> queries) {

        Map<String, Map<String, Double>> graph = new HashMap<>();



        for (int index = 0; index < equations.size(); index++) {

            String dividend = equations.get(index).get(0);

            String divisor = equations.get(index).get(1);

            double value = values[index];

            graph.computeIfAbsent(dividend, ignored -> new HashMap<>()).put(divisor, value);

            graph.computeIfAbsent(divisor, ignored -> new HashMap<>()).put(dividend, 1.0 / value);

        }



        double[] results = new double[queries.size()];

        for (int index = 0; index < queries.size(); index++) {

            results[index] = dfs(

                    queries.get(index).get(0),

                    queries.get(index).get(1),

                    graph,

                    new HashSet<>());

        }



        return results;

    }



    private double dfs(

            String start,

            String end,

            Map<String, Map<String, Double>> graph,

            Set<String> visited) {

        if (!graph.containsKey(start) || !graph.containsKey(end)) {

            return -1.0;

        }

        if (start.equals(end)) {

            return 1.0;

        }



        visited.add(start);

        for (Map.Entry<String, Double> entry : graph.get(start).entrySet()) {

            if (visited.contains(entry.getKey())) {

                continue;

            }

            double result = dfs(entry.getKey(), end, graph, visited);

            if (result != -1.0) {

                return entry.getValue() * result;

            }

        }



        return -1.0;

    }

}

// LeetCode 0399 - Evaluate Division

// https://leetcode.com/problems/evaluate-division/



using System.Collections.Generic;



public class Solution {

    public double[] CalcEquation(

        IList<IList<string>> equations,

        double[] values,

        IList<IList<string>> queries) {

        Dictionary<string, Dictionary<string, double>> graph = new();



        for (int index = 0; index < equations.Count; index++) {

            string dividend = equations[index][0];

            string divisor = equations[index][1];

            double value = values[index];

            if (!graph.ContainsKey(dividend)) {

                graph[dividend] = new Dictionary<string, double>();

            }

            if (!graph.ContainsKey(divisor)) {

                graph[divisor] = new Dictionary<string, double>();

            }

            graph[dividend][divisor] = value;

            graph[divisor][dividend] = 1.0 / value;

        }



        double[] results = new double[queries.Count];

        for (int index = 0; index < queries.Count; index++) {

            results[index] = Dfs(

                queries[index][0],

                queries[index][1],

                graph,

                new HashSet<string>());

        }



        return results;

    }



    private static double Dfs(

        string start,

        string end,

        Dictionary<string, Dictionary<string, double>> graph,

        HashSet<string> visited) {

        if (!graph.ContainsKey(start) || !graph.ContainsKey(end)) {

            return -1.0;

        }

        if (start == end) {

            return 1.0;

        }



        visited.Add(start);

        foreach (KeyValuePair<string, double> entry in graph[start]) {

            if (visited.Contains(entry.Key)) {

                continue;

            }

            double result = Dfs(entry.Key, end, graph, visited);

            if (result != -1.0) {

                return entry.Value * result;

            }

        }



        return -1.0;

    }

}

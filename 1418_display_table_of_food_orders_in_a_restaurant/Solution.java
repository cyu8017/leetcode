// LeetCode 1418 - Display Table Of Food Orders In A Restaurant
// https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

import java.util.*;

class Solution {
    public List<List<String>> displayTable(List<List<String>> orders) {
        TreeSet<String> foods = new TreeSet<>();
        TreeSet<Integer> tables = new TreeSet<>();
        Map<String, Integer> counts = new HashMap<>();
        for (List<String> order : orders) {
            int table = Integer.parseInt(order.get(1));
            String food = order.get(2);
            foods.add(food);
            tables.add(table);
            String key = table + "#" + food;
            counts.merge(key, 1, Integer::sum);
        }
        List<List<String>> answer = new ArrayList<>();
        List<String> header = new ArrayList<>();
        header.add("Table");
        header.addAll(foods);
        answer.add(header);
        for (int table : tables) {
            List<String> row = new ArrayList<>();
            row.add(String.valueOf(table));
            for (String food : foods) {
                row.add(String.valueOf(counts.getOrDefault(table + "#" + food, 0)));
            }
            answer.add(row);
        }
        return answer;
    }
}

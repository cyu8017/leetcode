// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class SQL {
    private final Map<String, List<List<String>>> tables = new HashMap<>();
    private final Map<String, Integer> nextID = new HashMap<>();

    public SQL(String[] names, int[] columns) {
        for (String name : names) {
            tables.put(name, new ArrayList<>());
            nextID.put(name, 1);
        }
    }

    public boolean ins(String name, List<String> row) {
        if (!tables.containsKey(name)) return false;
        int id = nextID.get(name);
        nextID.put(name, id + 1);
        List<String> full = new ArrayList<>();
        full.add(Integer.toString(id));
        full.addAll(row);
        tables.get(name).add(full);
        return true;
    }

    public void rmv(String name, int rowId) {
        List<List<String>> rows = tables.get(name);
        for (int i = 0; i < rows.size(); i++) {
            if (Integer.parseInt(rows.get(i).get(0)) == rowId) {
                rows.remove(i);
                return;
            }
        }
    }

    public String sel(String name, int rowId, int columnId) {
        for (List<String> r : tables.get(name)) {
            if (Integer.parseInt(r.get(0)) == rowId) {
                if (columnId < 1 || columnId >= r.size()) return "<null>";
                return r.get(columnId);
            }
        }
        return "<null>";
    }

    public List<String> exp(String name) {
        List<String> ans = new ArrayList<>();
        for (List<String> r : tables.get(name)) {
            StringBuilder sb = new StringBuilder(r.get(0));
            for (int j = 1; j < r.size(); j++) sb.append(',').append(r.get(j));
            ans.add(sb.toString());
        }
        return ans;
    }
}

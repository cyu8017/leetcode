// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

import java.util.*;

class Solution {
    private Map<String, Integer> values = new HashMap<>();
    private List<String> tokens = new ArrayList<>();
    private int pos;

    static final class ListKey {
        final List<String> items;
        ListKey(List<String> items) { this.items = items; }
        int count() { return items.size(); }
        @Override public boolean equals(Object o) {
            if (!(o instanceof ListKey)) return false;
            ListKey other = (ListKey) o;
            return items.equals(other.items);
        }
        @Override public int hashCode() { return items.hashCode(); }
    }

    public List<String> basicCalculatorIV(String expression, String[] evalvars, int[] evalints) {
        values.clear();
        for (int i = 0; i < evalvars.length; i++) values.put(evalvars[i], evalints[i]);
        tokens.clear();
        StringBuilder cur = new StringBuilder();
        for (char ch : expression.toCharArray()) {
            if (ch == '(' || ch == ')') {
                if (cur.length() > 0) { tokens.add(cur.toString()); cur.setLength(0); }
                tokens.add(String.valueOf(ch));
            } else if (Character.isWhitespace(ch)) {
                if (cur.length() > 0) { tokens.add(cur.toString()); cur.setLength(0); }
            } else cur.append(ch);
        }
        if (cur.length() > 0) tokens.add(cur.toString());
        pos = 0;
        Map<ListKey, Integer> poly = parseExpr();
        List<Map.Entry<ListKey, Integer>> keys = new ArrayList<>(poly.entrySet());
        keys.sort((a, b) -> {
            if (a.getKey().count() != b.getKey().count()) return Integer.compare(b.getKey().count(), a.getKey().count());
            return compareLists(a.getKey().items, b.getKey().items);
        });
        List<String> answer = new ArrayList<>();
        for (Map.Entry<ListKey, Integer> kv : keys) {
            if (kv.getValue() == 0) continue;
            if (kv.getKey().count() == 0) answer.add(String.valueOf(kv.getValue()));
            else {
                StringBuilder term = new StringBuilder(String.valueOf(kv.getValue()));
                for (String var : kv.getKey().items) { term.append('*'); term.append(var); }
                answer.add(term.toString());
            }
        }
        return answer;
    }

    private int compareLists(List<String> a, List<String> b) {
        int n = Math.min(a.size(), b.size());
        for (int i = 0; i < n; i++) {
            int cmp = a.get(i).compareTo(b.get(i));
            if (cmp != 0) return cmp;
        }
        return Integer.compare(a.size(), b.size());
    }

    private Map<ListKey, Integer> parseExpr() {
        Map<ListKey, Integer> poly = parseTerm();
        while (pos < tokens.size() && (tokens.get(pos).equals("+") || tokens.get(pos).equals("-"))) {
            String op = tokens.get(pos++);
            Map<ListKey, Integer> right = parseTerm();
            poly = add(poly, op.equals("+") ? right : negate(right));
        }
        return poly;
    }

    private Map<ListKey, Integer> parseTerm() {
        Map<ListKey, Integer> poly = parseFactor();
        while (pos < tokens.size() && tokens.get(pos).equals("*")) {
            pos++;
            poly = mul(poly, parseFactor());
        }
        return poly;
    }

    private Map<ListKey, Integer> parseFactor() {
        if (tokens.get(pos).equals("(")) {
            pos++;
            Map<ListKey, Integer> poly = parseExpr();
            pos++;
            return poly;
        }
        return atom(tokens.get(pos++));
    }

    private Map<ListKey, Integer> atom(String token) {
        Map<ListKey, Integer> poly = new HashMap<>();
        if (Character.isLetter(token.charAt(0))) {
            if (values.containsKey(token)) poly.put(new ListKey(new ArrayList<>()), values.get(token));
            else poly.put(new ListKey(new ArrayList<>(Collections.singletonList(token))), 1);
        } else poly.put(new ListKey(new ArrayList<>()), Integer.parseInt(token));
        return clean(poly);
    }

    private Map<ListKey, Integer> add(Map<ListKey, Integer> left, Map<ListKey, Integer> right) {
        Map<ListKey, Integer> result = new HashMap<>(left);
        for (Map.Entry<ListKey, Integer> kv : right.entrySet()) {
            result.put(kv.getKey(), result.getOrDefault(kv.getKey(), 0) + kv.getValue());
        }
        return clean(result);
    }

    private Map<ListKey, Integer> negate(Map<ListKey, Integer> poly) {
        Map<ListKey, Integer> result = new HashMap<>();
        for (Map.Entry<ListKey, Integer> kv : poly.entrySet()) result.put(kv.getKey(), -kv.getValue());
        return result;
    }

    private Map<ListKey, Integer> mul(Map<ListKey, Integer> left, Map<ListKey, Integer> right) {
        Map<ListKey, Integer> result = new HashMap<>();
        for (Map.Entry<ListKey, Integer> lk : left.entrySet()) {
            for (Map.Entry<ListKey, Integer> rk : right.entrySet()) {
                List<String> keyList = new ArrayList<>(lk.getKey().items);
                keyList.addAll(rk.getKey().items);
                Collections.sort(keyList);
                ListKey key = new ListKey(keyList);
                result.put(key, result.getOrDefault(key, 0) + lk.getValue() * rk.getValue());
            }
        }
        return clean(result);
    }

    private Map<ListKey, Integer> clean(Map<ListKey, Integer> poly) {
        poly.entrySet().removeIf(kv -> kv.getValue() == 0);
        return poly;
    }
}

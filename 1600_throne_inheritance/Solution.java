// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

import java.util.*;

class ThroneInheritance {
    private final String king;
    private final Map<String, List<String>> children = new HashMap<>();
    private final Set<String> dead = new HashSet<>();

    public ThroneInheritance(String kingName) {
        this.king = kingName;
    }

    public void birth(String parentName, String childName) {
        children.computeIfAbsent(parentName, k -> new ArrayList<>()).add(childName);
    }

    public void death(String name) {
        dead.add(name);
    }

    public List<String> getInheritanceOrder() {
        List<String> order = new ArrayList<>();
        visit(king, order);
        return order;
    }

    private void visit(String name, List<String> order) {
        if (!dead.contains(name)) order.add(name);
        for (String child : children.getOrDefault(name, Collections.emptyList())) {
            visit(child, order);
        }
    }
}

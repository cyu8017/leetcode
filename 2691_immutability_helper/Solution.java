// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

import java.util.*;
import java.util.function.Consumer;

// JS immutability helper stand-in
class Solution {
    public List<TreeMap<String, Integer>> immutableHelper(
            TreeMap<String, Integer> obj,
            List<Consumer<TreeMap<String, Integer>>> mutators) {
        List<TreeMap<String, Integer>> out = new ArrayList<>();
        for (Consumer<TreeMap<String, Integer>> m : mutators) {
            TreeMap<String, Integer> copy = new TreeMap<>(obj);
            m.accept(copy);
            out.add(copy);
        }
        return out;
    }
}

// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

import java.util.*;

class CombinationIterator {
    private final String[] items;
    private int index = 0;

    public CombinationIterator(String characters, int combinationLength) {
        List<String> built = new ArrayList<>();
        build(characters, combinationLength, 0, new char[combinationLength], 0, built);
        items = built.toArray(new String[0]);
    }

    public String next() {
        return items[index++];
    }

    public boolean hasNext() {
        return index < items.length;
    }

    private void build(String characters, int k, int start, char[] path, int depth, List<String> out) {
        if (depth == k) {
            out.add(new String(path));
            return;
        }
        for (int i = start; i < characters.length(); i++) {
            path[depth] = characters.charAt(i);
            build(characters, k, i + 1, path, depth + 1, out);
        }
    }
}

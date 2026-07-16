// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed

// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/



import java.util.ArrayList;

import java.util.HashMap;

import java.util.HashSet;

import java.util.List;

import java.util.Map;

import java.util.Set;



class RandomizedCollection {

    private final List<Integer> values = new ArrayList<>();

    private final Map<Integer, Set<Integer>> indicesByValue = new HashMap<>();



    public RandomizedCollection() {

    }



    public boolean insert(int val) {

        if (!indicesByValue.containsKey(val)) {

            indicesByValue.put(val, new HashSet<>());

        }

        indicesByValue.get(val).add(values.size());

        values.add(val);

        return indicesByValue.get(val).size() == 1;

    }



    public boolean remove(int val) {

        if (!indicesByValue.containsKey(val) || indicesByValue.get(val).isEmpty()) {

            return false;

        }



        int index = indicesByValue.get(val).iterator().next();

        int lastIndex = values.size() - 1;

        int lastValue = values.get(lastIndex);

        values.set(index, lastValue);

        indicesByValue.get(lastValue).remove(lastIndex);

        indicesByValue.get(lastValue).add(index);

        values.remove(lastIndex);

        indicesByValue.get(val).remove(index);

        if (indicesByValue.get(val).isEmpty()) {

            indicesByValue.remove(val);

        }

        return true;

    }



    public int getRandom() {

        return values.get(values.size() - 1);

    }

}

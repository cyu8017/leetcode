// LeetCode 0380 - Insert Delete GetRandom O(1)

// https://leetcode.com/problems/insert-delete-getrandom-o1/



import java.util.ArrayList;

import java.util.HashMap;

import java.util.List;

import java.util.Map;

import java.util.Random;



class RandomizedSet {

    private final List<Integer> values = new ArrayList<>();

    private final Map<Integer, Integer> indexByValue = new HashMap<>();

    private final Random random = new Random();



    public RandomizedSet() {

    }



    public boolean insert(int val) {

        if (indexByValue.containsKey(val)) {

            return false;

        }

        indexByValue.put(val, values.size());

        values.add(val);

        return true;

    }



    public boolean remove(int val) {

        if (!indexByValue.containsKey(val)) {

            return false;

        }



        int index = indexByValue.get(val);

        int lastValue = values.get(values.size() - 1);

        values.set(index, lastValue);

        indexByValue.put(lastValue, index);

        values.remove(values.size() - 1);

        indexByValue.remove(val);

        return true;

    }



    public int getRandom() {

        return values.get(random.nextInt(values.size()));

    }

}

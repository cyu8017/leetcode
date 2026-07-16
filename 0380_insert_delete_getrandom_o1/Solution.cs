// LeetCode 0380 - Insert Delete GetRandom O(1)

// https://leetcode.com/problems/insert-delete-getrandom-o1/



using System.Collections.Generic;



public class RandomizedSet {

    private readonly List<int> values = new();

    private readonly Dictionary<int, int> indexByValue = new();



    public RandomizedSet() {

    }



    public bool Insert(int val) {

        if (indexByValue.ContainsKey(val)) {

            return false;

        }

        indexByValue[val] = values.Count;

        values.Add(val);

        return true;

    }



    public bool Remove(int val) {

        if (!indexByValue.ContainsKey(val)) {

            return false;

        }



        int index = indexByValue[val];

        int lastValue = values[^1];

        values[index] = lastValue;

        indexByValue[lastValue] = index;

        values.RemoveAt(values.Count - 1);

        indexByValue.Remove(val);

        return true;

    }



    public int GetRandom() {

        return values[Random.Shared.Next(values.Count)];

    }

}

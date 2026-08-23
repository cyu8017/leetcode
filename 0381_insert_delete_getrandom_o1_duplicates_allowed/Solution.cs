// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed

// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/



using System.Collections.Generic;



public class RandomizedCollection {

    private readonly List<int> values = new();

    private readonly Dictionary<int, HashSet<int>> indicesByValue = new();



    public RandomizedCollection() {

    }



    public bool Insert(int val) {

        if (!indicesByValue.ContainsKey(val)) {

            indicesByValue[val] = new HashSet<int>();

        }

        indicesByValue[val].Add(values.Count);

        values.Add(val);

        return indicesByValue[val].Count == 1;

    }



    public bool Remove(int val) {

        if (!indicesByValue.ContainsKey(val) || indicesByValue[val].Count == 0) {

            return false;

        }



        int index = 0;

        foreach (int candidate in indicesByValue[val]) {

            index = candidate;

            break;

        }

        int lastIndex = values.Count - 1;

        int lastValue = values[lastIndex];

        values[index] = lastValue;

        indicesByValue[lastValue].Remove(lastIndex);

        indicesByValue[lastValue].Add(index);

        values.RemoveAt(lastIndex);

        indicesByValue[val].Remove(index);

        if (indicesByValue[val].Count == 0) {

            indicesByValue.Remove(val);

        }

        return true;

    }



    public int GetRandom() {

        return values[^1];

    }

}

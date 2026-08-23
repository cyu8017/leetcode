// LeetCode 0379 - Design Phone Directory

// https://leetcode.com/problems/design-phone-directory/



using System.Collections.Generic;



public class PhoneDirectory {

    private readonly SortedSet<int> available = new();



    public PhoneDirectory(int maxNumbers) {

        for (int index = 0; index < maxNumbers; index++) {

            available.Add(index);

        }

    }



    public int Get() {

        if (available.Count == 0) {

            return -1;

        }

        int number = available.Min;

        available.Remove(number);

        return number;

    }



    public bool Check(int number) {

        return available.Contains(number);

    }



    public void Release(int number) {

        available.Add(number);

    }

}

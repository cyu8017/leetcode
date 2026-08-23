// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

using System;
using System.Collections.Generic;

public class FoodRatings {
    private readonly Dictionary<string, string> cuisineOf = new();
    private readonly Dictionary<string, int> ratingOf = new();
    private readonly Dictionary<string, SortedSet<(int rating, string food)>> heaps = new();

    private static int Cmp((int rating, string food) a, (int rating, string food) b) {
        int c = b.rating.CompareTo(a.rating);
        if (c != 0) return c;
        return string.CompareOrdinal(a.food, b.food);
    }

    public FoodRatings(string[] foods, string[] cuisines, int[] ratings) {
        var cmp = Comparer<(int, string)>.Create(Cmp);
        for (int i = 0; i < foods.Length; i++) {
            cuisineOf[foods[i]] = cuisines[i];
            ratingOf[foods[i]] = ratings[i];
            if (!heaps.ContainsKey(cuisines[i])) heaps[cuisines[i]] = new SortedSet<(int, string)>(cmp);
            heaps[cuisines[i]].Add((ratings[i], foods[i]));
        }
    }

    public void ChangeRating(string food, int newRating) {
        string cuisine = cuisineOf[food];
        int old = ratingOf[food];
        heaps[cuisine].Remove((old, food));
        ratingOf[food] = newRating;
        heaps[cuisine].Add((newRating, food));
    }

    public string HighestRated(string cuisine) {
        return heaps[cuisine].Min.food;
    }
}

// LeetCode 2353 - Design a Food Rating System
// https://leetcode.com/problems/design-a-food-rating-system/

import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

class FoodRatings {
    private final Map<String, String> cuisineOf = new HashMap<>();
    private final Map<String, Integer> ratingOf = new HashMap<>();
    private final Map<String, TreeSet<String>> heaps = new HashMap<>();

    private int cmp(String a, String b) {
        int ra = ratingOf.get(a), rb = ratingOf.get(b);
        if (ra != rb) return Integer.compare(rb, ra);
        return a.compareTo(b);
    }

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        for (int i = 0; i < foods.length; i++) {
            cuisineOf.put(foods[i], cuisines[i]);
            ratingOf.put(foods[i], ratings[i]);
            heaps.computeIfAbsent(cuisines[i], k -> new TreeSet<>(this::cmp)).add(foods[i]);
        }
    }

    public void changeRating(String food, int newRating) {
        String cuisine = cuisineOf.get(food);
        TreeSet<String> set = heaps.get(cuisine);
        set.remove(food);
        ratingOf.put(food, newRating);
        set.add(food);
    }

    public String highestRated(String cuisine) {
        return heaps.get(cuisine).first();
    }
}

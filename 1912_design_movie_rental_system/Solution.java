// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

import java.util.*;

class MovieRentingSystem {
    private final Map<Long, Integer> price = new HashMap<>();
    private final Map<Integer, TreeSet<long[]>> available = new HashMap<>();
    private final TreeSet<long[]> rented = new TreeSet<>((a, b) -> {
        if (a[0] != b[0]) return Long.compare(a[0], b[0]);
        if (a[1] != b[1]) return Long.compare(a[1], b[1]);
        return Long.compare(a[2], b[2]);
    });

    public MovieRentingSystem(int n, int[][] entries) {
        Comparator<long[]> cmp = (a, b) -> {
            if (a[0] != b[0]) return Long.compare(a[0], b[0]);
            return Long.compare(a[1], b[1]);
        };
        for (int[] e : entries) {
            int shop = e[0], movie = e[1], p = e[2];
            price.put(key(shop, movie), p);
            available.computeIfAbsent(movie, k -> new TreeSet<>(cmp)).add(new long[]{p, shop});
        }
    }

    public List<Integer> search(int movie) {
        List<Integer> res = new ArrayList<>();
        TreeSet<long[]> set = available.get(movie);
        if (set == null) return res;
        int i = 0;
        for (long[] e : set) {
            if (i++ == 5) break;
            res.add((int) e[1]);
        }
        return res;
    }

    public void rent(int shop, int movie) {
        int p = price.get(key(shop, movie));
        available.get(movie).remove(new long[]{p, shop});
        rented.add(new long[]{p, shop, movie});
    }

    public void drop(int shop, int movie) {
        int p = price.get(key(shop, movie));
        rented.remove(new long[]{p, shop, movie});
        available.get(movie).add(new long[]{p, shop});
    }

    public List<List<Integer>> report() {
        List<List<Integer>> res = new ArrayList<>();
        int i = 0;
        for (long[] e : rented) {
            if (i++ == 5) break;
            res.add(Arrays.asList((int) e[1], (int) e[2]));
        }
        return res;
    }

    private long key(int shop, int movie) {
        return ((long) shop << 20) | movie;
    }
}

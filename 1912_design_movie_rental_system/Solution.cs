// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

using System;
using System.Collections.Generic;
using System.Linq;

public class MovieRentingSystem {
    private readonly Dictionary<(int shop, int movie), int> price = new();
    private readonly Dictionary<int, SortedSet<(int price, int shop)>> available = new();
    private readonly SortedSet<(int price, int shop, int movie)> rented = new();

    public MovieRentingSystem(int n, int[][] entries) {
        foreach (var e in entries) {
            int shop = e[0], movie = e[1], p = e[2];
            price[(shop, movie)] = p;
            if (!available.ContainsKey(movie))
                available[movie] = new SortedSet<(int, int)>();
            available[movie].Add((p, shop));
        }
    }

    public IList<int> Search(int movie) {
        if (!available.ContainsKey(movie)) return new List<int>();
        return available[movie].Take(5).Select(x => x.shop).ToList();
    }

    public void Rent(int shop, int movie) {
        int p = price[(shop, movie)];
        available[movie].Remove((p, shop));
        rented.Add((p, shop, movie));
    }

    public void Drop(int shop, int movie) {
        int p = price[(shop, movie)];
        rented.Remove((p, shop, movie));
        available[movie].Add((p, shop));
    }

    public IList<IList<int>> Report() {
        return rented.Take(5).Select(x => (IList<int>)new List<int> { x.shop, x.movie }).ToList();
    }
}
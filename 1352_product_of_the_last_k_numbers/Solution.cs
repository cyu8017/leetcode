// LeetCode 1352 - Product Of The Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

using System.Collections.Generic;
public class ProductOfNumbers {
    List<int> p = new List<int> { 1 };
    public ProductOfNumbers() {}
    public void Add(int num) {
        if (num == 0) p = new List<int> { 1 };
        else p.Add(p[p.Count - 1] * num);
    }
    public int GetProduct(int k) {
        return k >= p.Count ? 0 : p[p.Count - 1] / p[p.Count - 1 - k];
    }
}

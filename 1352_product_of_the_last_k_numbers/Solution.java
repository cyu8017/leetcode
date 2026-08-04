// LeetCode 1352 - Product Of The Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

import java.util.*;

class ProductOfNumbers {
    private List<Integer> p = new ArrayList<>();

    public ProductOfNumbers() {
        p.add(1);
    }

    public void add(int num) {
        if (num == 0) {
            p = new ArrayList<>();
            p.add(1);
        } else {
            p.add(p.get(p.size() - 1) * num);
        }
    }

    public int getProduct(int k) {
        if (k >= p.size()) return 0;
        return p.get(p.size() - 1) / p.get(p.size() - 1 - k);
    }
}

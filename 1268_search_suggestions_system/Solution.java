// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

import java.util.*;

class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products);
        List<List<String>> answer = new ArrayList<>();
        String prefix = "";
        for (char ch : searchWord.toCharArray()) {
            prefix += ch;
            int i = lowerBound(products, prefix);
            List<String> row = new ArrayList<>();
            for (int j = i; j < products.length && j < i + 3; j++) {
                if (products[j].startsWith(prefix)) row.add(products[j]);
                else break;
            }
            answer.add(row);
        }
        return answer;
    }

    private int lowerBound(String[] arr, String target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid].compareTo(target) < 0) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}

// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

class Solution {
    public String discountPrices(String sentence, int discount) {
        String[] parts = sentence.split(" ");
        for (int i = 0; i < parts.length; i++) {
            String part = parts[i];
            if (part.length() >= 2 && part.charAt(0) == '$') {
                boolean ok = true;
                for (int j = 1; j < part.length(); j++)
                    if (part.charAt(j) < '0' || part.charAt(j) > '9') {
                        ok = false;
                        break;
                    }
                if (ok) {
                    long val = Long.parseLong(part.substring(1));
                    double price = val * (100.0 - discount) / 100.0;
                    parts[i] = String.format("$%.2f", price);
                }
            }
        }
        return String.join(" ", parts);
    }
}

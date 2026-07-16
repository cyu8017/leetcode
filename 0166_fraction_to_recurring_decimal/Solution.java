import java.util.*;
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0"; StringBuilder result = new StringBuilder(); long n = numerator, d = denominator; if ((n < 0) ^ (d < 0)) result.append('-'); n = Math.abs(n); d = Math.abs(d); result.append(n / d); long remainder = n % d; if (remainder == 0) return result.toString(); result.append('.'); Map<Long, Integer> seen = new HashMap<>();
        while (remainder != 0) { Integer index = seen.putIfAbsent(remainder, result.length()); if (index != null) { result.insert(index, '('); result.append(')'); break; } remainder *= 10; result.append(remainder / d); remainder %= d; } return result.toString();
    }
}
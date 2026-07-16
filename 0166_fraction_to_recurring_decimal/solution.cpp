// LeetCode 0166 - Fraction to Recurring Decimal
#include <cstdlib>
#include <string>
#include <unordered_map>
using namespace std;
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        long long n = numerator, d = denominator;
        string result = (n < 0) ^ (d < 0) ? "-" : "";
        n = llabs(n); d = llabs(d);
        result += to_string(n / d);
        long long remainder = n % d;
        if (!remainder) return result;
        result += '.';
        unordered_map<long long, int> seen;
        while (remainder) {
            if (seen.count(remainder)) {
                result.insert(seen[remainder], "("); return result + ")";
            }
            seen[remainder] = result.size();
            remainder *= 10;
            result += to_string(remainder / d);
            remainder %= d;
        }
        return result;
    }
};
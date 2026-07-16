// LeetCode 0166 - Fraction to Recurring Decimal
import "strconv"
func fractionToDecimal(numerator int, denominator int) string {
    if numerator == 0 { return "0" }
    n, d := int64(numerator), int64(denominator)
    result := ""
    if (n < 0) != (d < 0) { result = "-" }
    if n < 0 { n = -n }; if d < 0 { d = -d }
    result += strconv.FormatInt(n/d, 10)
    remainder := n % d
    if remainder == 0 { return result }
    result += "."
    seen := map[int64]int{}
    for remainder != 0 {
        if position, ok := seen[remainder]; ok { return result[:position] + "(" + result[position:] + ")" }
        seen[remainder] = len(result)
        remainder *= 10
        result += strconv.FormatInt(remainder/d, 10)
        remainder %= d
    }
    return result
}
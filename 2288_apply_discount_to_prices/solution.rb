# LeetCode 2288 - Apply Discount to Prices
# https://leetcode.com/problems/apply-discount-to-prices/

# @param {String} sentence
# @param {Integer} discount
# @return {String}
def discount_prices(sentence, discount)
  parts = sentence.split(" ")
  parts.each_with_index do |part, i|
    next unless part.length >= 2 && part[0] == "$"

    ok = true
    (1...part.length).each do |j|
      if part[j] < "0" || part[j] > "9"
        ok = false
        break
      end
    end
    next unless ok

    val = part[1..].to_i
    price = val * (100 - discount) / 100.0
    parts[i] = format("$%.2f", price)
  end
  parts.join(" ")
end

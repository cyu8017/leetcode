# LeetCode 1169 - Invalid Transactions
# https://leetcode.com/problems/invalid-transactions/

# @param {String[]} transactions
# @return {String[]}
def invalid_transactions(transactions)
  parsed = transactions.map do |t|
    name, time, amount, city = t.split(",")
    [name, time.to_i, amount.to_i, city, t]
  end
  invalid = {}
  parsed.each_with_index do |(name, time, amount, city, raw), i|
    invalid[raw] = true if amount > 1000
    parsed.each_with_index do |(name2, time2, _, city2, raw2), j|
      next if i == j
      if name == name2 && city != city2 && (time - time2).abs <= 60
        invalid[raw] = true
        invalid[raw2] = true
      end
    end
  end
  invalid.keys
end

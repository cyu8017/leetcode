# LeetCode 2887 - Fill Missing Data
# https://leetcode.com/problems/fill-missing-data/

# @param {Object[]} products
# @return {Object[]}
def fill_missing_values(products)
  products.map do |r|
    if r.is_a?(Array)
      q = r[1]
      [r[0], q.nil? ? 0 : q, r[2]]
    else
      row = r.dup
      row["quantity"] = r["quantity"].nil? ? 0 : r["quantity"]
      row
    end
  end
end

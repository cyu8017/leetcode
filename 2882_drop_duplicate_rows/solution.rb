# LeetCode 2882 - Drop Duplicate Rows
# https://leetcode.com/problems/drop-duplicate-rows/

# @param {Object[]} customers
# @return {Object[]}
def drop_duplicate_emails(customers)
  seen = {}
  out = []
  customers.each do |r|
    email = r.is_a?(Array) ? r[2] : r["email"]
    next if seen[email]

    seen[email] = true
    out << r
  end
  out
end

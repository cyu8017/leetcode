# LeetCode 3606 - Coupon Code Validator
# https://leetcode.com/problems/coupon-code-validator/

# @param {String[]} code
# @param {String[]} business_line
# @param {Boolean[]} is_active
# @return {String[]}
def validate_coupons(code, business_line, is_active)
  check = lambda do |s|
    return false if s.nil? || s.empty?
    s.each_char { |c| return false unless c.match?(/[A-Za-z0-9_]/) }
    true
  end
  bs = { "electronics" => true, "grocery" => true, "pharmacy" => true, "restaurant" => true }
  idx = []
  (0...code.length).each do |i|
    idx << i if is_active[i] && bs[business_line[i]] && check.call(code[i])
  end
  idx.sort_by! { |i| [business_line[i], code[i]] }
  idx.map { |i| code[i] }
end

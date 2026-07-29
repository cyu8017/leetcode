# LeetCode 1058 - Minimize Rounding Error to Meet Target
# https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

# @param {String[]} prices
# @param {Integer} target
# @return {String}
def minimize_error(prices, target)
  floors = 0
  fracs = []
  prices.each do |p|
    value = p.to_f
    floor = value.to_i
    floors += floor
    frac = value - floor
    fracs << frac if frac > 1e-9
  end
  ceil_count = target - floors
  return "-1" if ceil_count < 0 || ceil_count > fracs.length

  fracs.sort!.reverse!
  error = fracs[0...ceil_count].sum { |f| 1 - f } + fracs[ceil_count..].sum
  format("%.3f", error)
end

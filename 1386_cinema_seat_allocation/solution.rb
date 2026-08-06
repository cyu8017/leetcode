# LeetCode 1386 - Cinema Seat Allocation
# https://leetcode.com/problems/cinema-seat-allocation/

def max_number_of_families(n, reserved_seats)
  rows = {}
  reserved_seats.each do |r, c|
    next unless c >= 2 && c <= 9
    rows[r] = (rows[r] || 0) | (1 << (c - 2))
  end
  ans = 2 * (n - rows.length)
  rows.each_value do |m|
    left = (m & 0b00001111) == 0
    right = (m & 0b11110000) == 0
    middle = (m & 0b00111100) == 0
    ans += left && right ? 2 : (left || right || middle ? 1 : 0)
  end
  ans
end

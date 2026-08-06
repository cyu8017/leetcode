# LeetCode 1419 - Minimum Number Of Frogs Croaking
# https://leetcode.com/problems/minimum-number-of-frogs-croaking/

def min_number_of_frogs(croak_of_frogs)
  order = { 'c' => 0, 'r' => 1, 'o' => 2, 'a' => 3, 'k' => 4 }
  counts = Array.new(5, 0)
  active = answer = 0
  croak_of_frogs.each_char do |char|
    i = order[char]
    return -1 if i.nil? || (i > 0 && counts[i - 1] == 0)
    counts[i - 1] -= 1 if i > 0
    counts[i] += 1
    if i == 0
      active += 1
      answer = [answer, active].max
    elsif i == 4
      counts[4] -= 1
      active -= 1
    end
  end
  active == 0 ? answer : -1
end

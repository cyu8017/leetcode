# LeetCode 0846 - Hand of Straights
# https://leetcode.com/problems/hand-of-straights/

# @param {Integer[]} hand
# @param {Integer} group_size
# @return {Boolean}
def is_n_straight_hand(hand, group_size)
  return false if hand.length % group_size != 0

  count = Hash.new(0)
  hand.each { |x| count[x] += 1 }
  count.keys.sort.each do |start|
    while count[start].positive?
      (start...start + group_size).each do |x|
        return false if count[x].zero?

        count[x] -= 1
      end
    end
  end
  true
end

# LeetCode 0841 - Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/

# @param {Integer[][]} rooms
# @return {Boolean}
def can_visit_all_rooms(rooms)
  seen = { 0 => true }
  stack = [0]
  until stack.empty?
    room = stack.pop
    rooms[room].each do |key|
      next if seen[key]

      seen[key] = true
      stack << key
    end
  end
  seen.length == rooms.length
end

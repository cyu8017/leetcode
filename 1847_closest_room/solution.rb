
# @param {Integer[][]} rooms
# @param {Integer[][]} queries
# @return {Integer[]}
def closest_room(rooms, queries)
  rooms = rooms.sort_by { |_, size| size }
  indexed_queries = queries.each_with_index.map { |q, i| [i, q] }.sort_by { |_, q| -q[1] }

  available_ids = []
  room_index = rooms.length - 1
  answer = Array.new(queries.length, -1)

  indexed_queries.each do |query_index, (preferred, min_size)|
    while room_index >= 0 && rooms[room_index][1] >= min_size
      insert_sorted(available_ids, rooms[room_index][0])
      room_index -= 1
    end
    next if available_ids.empty?

    pos = available_ids.bsearch_index { |id| id >= preferred } || available_ids.length
    best_id = -1
    best_dist = Float::INFINITY

    if pos < available_ids.length
      room_id = available_ids[pos]
      dist = (room_id - preferred).abs
      if dist < best_dist || (dist == best_dist && room_id < best_id)
        best_id = room_id
        best_dist = dist
      end
    end

    if pos > 0
      room_id = available_ids[pos - 1]
      dist = (room_id - preferred).abs
      if dist < best_dist || (dist == best_dist && room_id < best_id)
        best_id = room_id
      end
    end

    answer[query_index] = best_id
  end
  answer
end

def insert_sorted(arr, value)
  idx = arr.bsearch_index { |x| x >= value } || arr.length
  arr.insert(idx, value)
end

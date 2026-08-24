# LeetCode 0913 - Cat and Mouse
# https://leetcode.com/problems/cat-and-mouse/

# @param {Integer[][]} graph
# @return {Integer}
def cat_mouse_game(graph)
  n = graph.length
  draw = 0
  mouse_win = 1
  cat_win = 2
  states = Array.new(n) { Array.new(n) { [draw, draw] } }
  out_degree = Array.new(n) { Array.new(n) { [0, 0] } }
  queue = []

  n.times do |cat|
    n.times do |mouse|
      out_degree[cat][mouse][0] = graph[mouse].length
      out_degree[cat][mouse][1] = graph[cat].length - graph[cat].count(0)
    end
  end

  (1...n).each do |cat|
    2.times do |move|
      states[cat][0][move] = mouse_win
      queue << [cat, 0, move, mouse_win]
      states[cat][cat][move] = cat_win
      queue << [cat, cat, move, cat_win]
    end
  end

  until queue.empty?
    cat, mouse, move, state = queue.shift
    return state if cat == 2 && mouse == 1 && move == 0

    prev_move = move ^ 1
    src = prev_move == 1 ? graph[cat] : graph[mouse]
    src.each do |prev|
      prev_cat = prev_move == 1 ? prev : cat
      next if prev_cat == 0

      prev_mouse = prev_move == 1 ? mouse : prev
      next if states[prev_cat][prev_mouse][prev_move] != 0

      if (prev_move == 0 && state == mouse_win) ||
         (prev_move == 1 && state == cat_win) ||
         out_degree[prev_cat][prev_mouse][prev_move] == 1
        states[prev_cat][prev_mouse][prev_move] = state
        queue << [prev_cat, prev_mouse, prev_move, state]
      else
        out_degree[prev_cat][prev_mouse][prev_move] -= 1
      end
    end
  end

  states[2][1][0]
end

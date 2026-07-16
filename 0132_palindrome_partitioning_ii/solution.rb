class Solution
  def min_cut(s)
    n = s.length
    return 0 if n.zero?

    is_palindrome = Array.new(n) { Array.new(n, false) }
    (n - 1).downto(0) do |start|
      (start...n).each do |finish|
        is_palindrome[start][finish] = s[start] == s[finish] &&
                                       (finish - start < 2 || is_palindrome[start + 1][finish - 1])
      end
    end

    cuts = (0...n).to_a
    (0...n).each do |finish|
      if is_palindrome[0][finish]
        cuts[finish] = 0
      else
        (0...finish).each do |start|
          cuts[finish] = [cuts[finish], cuts[start] + 1].min if is_palindrome[start + 1][finish]
        end
      end
    end
    cuts[-1]
  end
end